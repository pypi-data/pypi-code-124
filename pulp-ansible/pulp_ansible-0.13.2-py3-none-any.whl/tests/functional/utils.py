"""Utilities for tests for the ansible plugin."""
from dynaconf import Dynaconf
from functools import partial
from time import sleep
import json
import os
import subprocess
import unittest

from pulp_smash import api, cli, config, selectors, utils
from pulp_smash.pulp3.bindings import delete_orphans, monitor_task, PulpTestCase
from pulp_smash.pulp3.utils import (
    gen_distribution,
    gen_remote,
    gen_repo,
    gen_publisher,
    get_content,
    require_pulp_3,
    require_pulp_plugins,
    sync,
)

from pulp_ansible.tests.functional.constants import (
    ANSIBLE_ROLE_NAME,
    ANSIBLE_ROLE_CONTENT_PATH,
    ANSIBLE_FIXTURE_URL,
    ANSIBLE_REMOTE_PATH,
    ANSIBLE_REPO_PATH,
)

from pulpcore.client.pulpcore import (
    ApiClient as CoreApiClient,
    TasksApi,
    SigningServicesApi,
    StatusApi,
)
from pulpcore.client.pulp_ansible import (
    ApiClient as AnsibleApiClient,
    ContentCollectionVersionsApi,
    DistributionsAnsibleApi,
    PulpAnsibleApiV3CollectionsApi,
    PulpAnsibleApiV3CollectionsVersionsApi,
    RepositoriesAnsibleApi,
    RemotesCollectionApi,
    RemotesGitApi,
    RemotesRoleApi,
    AnsibleRepositorySyncURL,
    PulpAnsibleArtifactsCollectionsV3Api,
    RepositoriesAnsibleVersionsApi,
)

from orionutils.generator import build_collection, randstr


cfg = config.get_config()
configuration = cfg.get_bindings_config()


def is_galaxy_ng_installed():
    """Returns whether or not the galaxy_ng plugin is installed."""
    configuration = cfg.get_bindings_config()
    core_client = CoreApiClient(configuration)
    status_client = StatusApi(core_client)

    status = status_client.status_read()

    for plugin in status.versions:
        if plugin.component == "galaxy":
            return True
    return False


def set_up_module():
    """Skip tests Pulp 3 isn't under test or if pulp_ansible isn't installed."""
    require_pulp_3(unittest.SkipTest)
    require_pulp_plugins({"ansible"}, unittest.SkipTest)


def gen_ansible_client():
    """Return an OBJECT for ansible client."""
    return AnsibleApiClient(configuration)


def gen_ansible_remote(url=ANSIBLE_FIXTURE_URL, include_pulp_auth=False, **kwargs):
    """Return a semi-random dict for use in creating a ansible Remote.

    :param url: The URL of an external content source.
    """
    if include_pulp_auth:
        kwargs["username"] = cfg.pulp_auth[0]
        kwargs["password"] = cfg.pulp_auth[1]

    if "rate_limit" not in kwargs:
        kwargs["rate_limit"] = 5

    return gen_remote(url, **kwargs)


def gen_ansible_publisher(**kwargs):
    """Return a semi-random dict for use in creating a Remote.

    :param url: The URL of an external content source.
    """
    return gen_publisher(**kwargs)


def get_ansible_content_paths(repo):
    """Return the relative path of content units present in an ansible repository.

    :param repo: A dict of information about the repository.
    :returns: A list with the paths of units present in a given repository.
    """
    # FIXME
    return [content_unit["relative_path"] for content_unit in get_content(repo)[ANSIBLE_ROLE_NAME]]


def gen_ansible_content_attrs(artifact):
    """Generate a dict with content unit attributes.

    :param: artifact: A dict of info about the artifact.
    :returns: A semi-random dict for use in creating a content unit.
    """
    # FIXME: add content specific metadata here
    return {"artifact": artifact["pulp_href"]}


def populate_pulp(cfg, url=ANSIBLE_FIXTURE_URL):
    """Add ansible contents to Pulp.

    :param pulp_smash.config.PulpSmashConfig: Information about a Pulp application.
    :param url: The ansible repository URL. Defaults to
        :data:`pulp_smash.constants.ANSIBLE_FIXTURE_URL`
    :returns: A list of dicts, where each dict describes one file content in Pulp.
    """
    client = api.Client(cfg, api.json_handler)
    remote = {}
    repo = {}
    try:
        remote.update(client.post(ANSIBLE_REMOTE_PATH, gen_ansible_remote(url)))
        repo.update(client.post(ANSIBLE_REPO_PATH, gen_repo()))
        sync(cfg, remote, repo)
    finally:
        if remote:
            client.delete(remote["pulp_href"])
        if repo:
            client.delete(repo["pulp_href"])
    return client.get(ANSIBLE_ROLE_CONTENT_PATH)["results"]


skip_if = partial(selectors.skip_if, exc=unittest.SkipTest)
"""The ``@skip_if`` decorator, customized for unittest.

:func:`pulp_smash.selectors.skip_if` is test runner agnostic. This function is
identical, except that ``exc`` has been set to ``unittest.SkipTest``.
"""


core_client = CoreApiClient(configuration)
tasks = TasksApi(core_client)
signing = SigningServicesApi(core_client)


def wait_tasks():
    """Polls the Task API until all tasks are in a completed state."""
    running_tasks = tasks.list(state="running")
    while running_tasks.count:
        sleep(1)
        running_tasks = tasks.list(state="running")


def gen_collection_in_distribution(
    base_path, name=None, namespace=None, versions=None, **cfg_kwargs
):
    """
    Generate a randomized collection and upload it to the specified repository.

    Params:
        - base_path: distribtion base path for the repository to upload the
          collection to.
        - name: Name of the collection. If none is provided a random name will
          be generated.
        - namespace: Namespace of the collection. If none is provided a random
          name will be generated.
        - versions: A list of versions to create for the collection. If none
          are specified the collection will be generated with version 1.0.0

        Additional galaxy.yaml configuration options can be added as kwargs.
        For example dependencies={"foo.bar": "1.0.0"} will set foo.bar as a
        dependency for the newly generated collection

    Returns: a dictionary with the name and namespace names of the newly generated
    collection.
    """
    if versions is None:
        versions = ["1.0.0"]
    namespace = namespace or randstr()
    name = name or randstr()

    ansible_client = gen_ansible_client()
    upload = PulpAnsibleArtifactsCollectionsV3Api(ansible_client)

    for version in versions:
        artifact = build_collection(
            "skeleton",
            config={"namespace": namespace, "name": name, "version": version, **cfg_kwargs},
        )

        upload.create(path=base_path, file=artifact.filename)

        wait_tasks()

        os.remove(artifact.filename)

    return {"name": name, "namespace": namespace}


class TestCaseUsingBindings(PulpTestCase):
    """A parent TestCase that instantiates the various bindings used throughout tests."""

    @classmethod
    def setUpClass(cls):
        """Create class-wide variables."""
        cls.client = gen_ansible_client()
        cls.repo_api = RepositoriesAnsibleApi(cls.client)
        cls.repo_version_api = RepositoriesAnsibleVersionsApi(cls.client)
        cls.remote_collection_api = RemotesCollectionApi(cls.client)
        cls.remote_git_api = RemotesGitApi(cls.client)
        cls.remote_role_api = RemotesRoleApi(cls.client)
        cls.distributions_api = DistributionsAnsibleApi(cls.client)
        cls.cv_api = ContentCollectionVersionsApi(cls.client)
        cls.collections_v3api = PulpAnsibleApiV3CollectionsApi(cls.client)
        cls.collections_versions_v3api = PulpAnsibleApiV3CollectionsVersionsApi(cls.client)

    @classmethod
    def tearDownClass(cls):
        """Clean class-wide variable."""
        delete_orphans()


class SyncHelpersMixin:
    """A common place for sync helper functions."""

    def _create_repo_and_sync_with_remote(self, remote, **repo_kwargs):
        """
        Create a repository and then sync with the provided `remote`.

        Args:
            remote: The remote to be sync with

        Returns:
            repository: The created repository object to be asserted to.
        """
        # Create the repository.
        repo = self.repo_api.create(gen_repo(**repo_kwargs))
        self.addCleanup(self.repo_api.delete, repo.pulp_href)
        return self._sync_repo(repo, remote=remote.pulp_href)

    def _create_repo_with_attached_remote_and_sync(self, remote, **repo_kwargs):
        """
        Create a repository with the remote attached, and then sync without specifying the `remote`.

        Args:
            remote: The remote to attach to the repository

        Returns:
            repository: The created repository object to be asserted to.
        """
        # Create the repository.
        repo = self.repo_api.create(gen_repo(remote=remote.pulp_href, **repo_kwargs))
        self.addCleanup(self.repo_api.delete, repo.pulp_href)
        return self._sync_repo(repo)

    def _sync_repo(self, repo, **kwargs):
        """
        Sync the repo with optional `kwarg` parameters passed on to the sync method.

        Args:
            repo: The repository to sync

        Returns:
            repository: The updated repository after the sync is complete
        """
        repository_sync_data = AnsibleRepositorySyncURL(**kwargs)
        sync_response = self.repo_api.sync(repo.pulp_href, repository_sync_data)
        monitor_task(sync_response.task)
        repo = self.repo_api.read(repo.pulp_href)
        return repo

    def _create_distribution_from_repo(self, repo, cleanup=True):
        """
        Create an `AnsibleDistribution` serving the `repo` with the `base_path`.

        Args:
            repo: The repository to serve with the `AnsibleDistribution`
            cleanup: Whether the distribution should be cleaned up

        Returns:
            The created `AnsibleDistribution`.
        """
        # Create a distribution.
        body = gen_distribution()
        body["repository"] = repo.pulp_href
        distribution_create = self.distributions_api.create(body)
        created_resources = monitor_task(distribution_create.task).created_resources
        distribution = self.distributions_api.read(created_resources[0])
        if cleanup:
            self.addCleanup(self.distributions_api.delete, distribution.pulp_href)
        return distribution

    def _create_empty_repo_and_distribution(self, cleanup=True):
        """
        Creates an empty `AnsibleRepository` and an `AnsibleDistribution` serving that repository.

        Args:
            cleanup: Whether the repository and distribution should be cleaned up

        Returns:
            Tuple of the created `AnsibleRepository`, `AnsibleDistribution`
        """
        repo = self.repo_api.create(gen_repo())
        if cleanup:
            self.addCleanup(self.repo_api.delete, repo.pulp_href)
        return repo, self._create_distribution_from_repo(repo, cleanup=cleanup)


settings = Dynaconf(
    settings_files=["pulp_ansible/tests/assets/func_test_settings.py", "/etc/pulp/settings.py"]
)


def get_psql_smash_cmd(sql_statement):
    """
    Generate a command in a format for pulp smash cli client to execute the specified SQL statement.

    The implication is that PostgreSQL is always running on localhost.
    Args:
        sql_statement(str): An SQL statement to execute.
    Returns:
        tuple: a command in the format for  pulp smash cli client
    """
    host = "localhost"
    user = settings.DATABASES["default"]["USER"]
    password = settings.DATABASES["default"]["PASSWORD"]
    dbname = settings.DATABASES["default"]["NAME"]
    return ("psql", "-c", sql_statement, f"postgresql://{user}:{password}@{host}/{dbname}")


def run_signing_script(filename):
    """
    Runs the test signing script manually on test calling machine.

    Returns the signature file produced.
    """
    file = os.path.realpath(f"{__file__}/../../assets/sign-metadata.sh")
    script = os.environ.get("TEST_PULP_SIGNING_SCRIPT", file)
    key_id = os.environ.get("TEST_PULP_SIGNING_KEY_ID", "Pulp QE")
    env = {"PULP_SIGNING_KEY_FINGERPRINT": key_id}
    completed_process = subprocess.run(
        [script, filename],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed_process.returncode != 0:
        raise RuntimeError(str(completed_process.stderr))

    try:
        return_value = json.loads(completed_process.stdout)
    except json.JSONDecodeError:
        raise RuntimeError("The signing script did not return valid JSON!")

    return return_value


def create_signing_service():
    """
    Generates an AsciiArmoredSigningService using the signing script in /assets.

    The signing script requires a GPG key and environment variables to be set in order to work.
    TEST_PULP_SIGNING_SCRIPT - Where the signing script exists
    TEST_PULP_SIGNING_KEY_ID - The signing key id used by the signing script
    """
    cli_client = cli.Client(cfg)
    name = utils.uuid4()
    script = os.environ.get("TEST_PULP_SIGNING_SCRIPT", "/var/lib/pulp/sign-metadata.sh")
    key_id = os.environ.get("TEST_PULP_SIGNING_KEY_ID", "Pulp QE")
    cmd = (
        "pulpcore-manager",
        "add-signing-service",
        name,
        script,
        key_id,
    )
    stdout = cli_client.run(cmd).stdout
    if "Successfully added signing service" not in stdout:
        raise Exception("Failed to create a signing service")
    results = signing.list(name=name)
    return results.results[0]


def delete_signing_service(name):
    """
    Deletes a signing service on the test machine.
    """
    python_cmd = (
        "from pulpcore.app.models import SigningService",
        f"SigningService.objects.get(name='{name}').delete()",
    )
    cli_client = cli.Client(cfg)
    utils.execute_pulpcore_python(cli_client, "\n".join(python_cmd))


def get_client_keyring():
    """
    Finds the GPG keyring for the client used in the tests.

    Uses the environment variables to change the default keyring
    TEST_PULP_CLIENT_KEYRING - The location for the GPG keyring
    TEST_PULP_SIGNING_KEY_ID - The signing key id used by the signing script
    """
    keyring = os.environ.get("TEST_PULP_CLIENT_KEYRING", "~/.gnupg/pubring.kbx")
    key_id = os.environ.get("TEST_PULP_SIGNING_KEY_ID", "Pulp QE")

    # Check that key_id is in the keyring
    cmd = ("gpg", "--list-keys", "--keyring", keyring, "--no-default-keyring")
    stdout = subprocess.run(cmd, capture_output=True, check=True).stdout
    if key_id not in stdout.decode():
        raise Exception(f"Key ID: {key_id} not found in keyring: {keyring}")

    return keyring
