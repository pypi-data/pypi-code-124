"""dotnet module literals"""

from devops_toolset.core.app import App
from devops_toolset.core.ValueDictsBase import ValueDictsBase

app: App = App()


class Literals(ValueDictsBase):
    """ValueDicts for the dotnet module."""

    _info = {
        "dotnet_build_before": "Launching dotnet build inside {path}. Please wait..",
        "dotnet_ef_database_drop": "Dropping the database...",
        "dotnet_ef_database_reset": "Reverting all migrations...",
        "dotnet_ef_first_migration_not_applied": "First migration not applied: {migration_name} ({migration_date})",
        "dotnet_ef_got_environments": "I got these environments:\n{environments}.",
        "dotnet_ef_migrations_info":
            "Number of migrations: {number}, applied migrations: {applied}, last applied migration: {name}",
        "dotnet_ef_migrations_list": "Listing migrations (will take a while)...",
        "dotnet_ef_migrations_list_output": "I got this output getting the migration's list:\n{output}",
        "dotnet_ef_migrations_script": "Generating SQL script (will take a while)...",
        "dotnet_ef_no_pending_migrations": "There are no pending migrations to be applied.",
        "dotnet_ef_script_being_generated": "SQL migration script being generated: {script_path}",
        "dotnet_ef_script_for_environment": "Generating SQL migration script for {environment} environment...",
        "dotnet_project_version": "The project version is {version}",
        "dotnet_restore_before": "Launching dotnet restore inside {path}. Please wait..",
    }
    _errors = {
        "dotnet_restore_err": "Something went wrong while restoring {path}. Please check the logs and try again.",
        "dotnet_build_err": "Something went wrong while building {path}. Please check the logs and try again.",
    }
