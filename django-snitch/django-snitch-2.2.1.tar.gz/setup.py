# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snitch',
 'snitch.migrations',
 'snitch.schedules',
 'snitch.schedules.migrations']

package_data = \
{'': ['*'], 'snitch': ['locale/es_ES/LC_MESSAGES/*']}

install_requires = \
['bleach>=4.1.0',
 'celery>=5.0.0,<6.0.0',
 'django-celery-beat>=2.2.0,<3.0.0',
 'django-model-utils>=4.1.1,<5.0.0',
 'django-push-notifications>=2.0.0',
 'django>=3.0.0']

setup_kwargs = {
    'name': 'django-snitch',
    'version': '2.2.1',
    'description': 'Django app made to integrate generic events that create notifications that can be sent to users using several backends.',
    'long_description': '=============\nDjango Snitch\n=============\n\n.. image:: https://travis-ci.org/marcosgabarda/django-snitch.svg?branch=master\n    :target: https://travis-ci.org/marcosgabarda/django-snitch\n\n.. image:: https://coveralls.io/repos/github/marcosgabarda/django-snitch/badge.svg?branch=master\n    :target: https://coveralls.io/github/marcosgabarda/django-snitch?branch=master\n\n.. image:: https://img.shields.io/badge/code_style-black-000000.svg\n   :target: https://github.com/ambv/black\n\n.. image:: https://readthedocs.org/projects/django-snitch/badge/?version=latest\n    :target: https://django-snitch.readthedocs.io/en/latest/?badge=latest\n    :alt: Documentation Status\n\nDjango app made to integrate generic events that create notifications that\ncan be sent to users using several backends.\n\nBy default, it integrates **push notifications** and **email** to send the\nnotifications.\n\nMade with Python 3 and Django with :heart:.\n\nQuick start\n-----------\n\n**1** Install using pip:\n\n.. code-block:: bash\n\n    pip install django-snitch\n\n**2** Add "snitch" to your INSTALLED_APPS settings like this:\n\n.. code-block:: python\n\n    INSTALLED_APPS += (\'snitch\',)\n\n**3** Create an ``events.py`` file in your app to register the events:\n\n.. code-block:: python\n\n    import snitch\n    from snitch.backends import PushNotificationBackend, EmailNotificationBackend\n\n    ACTIVATED_EVENT = "activated"\n    CONFIRMED_EVENT = "confirmed"\n\n\n    @snitch.register(ACTIVATED_EVENT)\n    class ActivatedHandler(snitch.EventHandler):\n        title = "Activated!"\n\n\n    @snitch.register(CONFIRMED_EVENT)\n    class ConfirmedHandler(snitch.EventHandler):\n        title = "Confirmed!"\n        notification_backends = [PushNotificationBackend, EmailNotificationBackend]\n\n        # Custom configuration for email backend\n        template_email_kwargs = {"template_name": "email.html"}\n        template_email_async = False\n\n        def audience(self):\n            return get_user_model().objects.all()\n\n\n**4** Use ``dispatch`` decorator to dispatch the event when a function is called:\n\n.. code-block:: python\n\n    from django.db import models\n    from django.utils import timezone\n\n    import snitch\n    from snitch.models import AbstractNotification\n    from tests.app.events import ACTIVATED_EVENT, CONFIRMED_EVENT\n\n\n    class Stuff(models.Model):\n        """Simple stuff model with status."""\n\n        IDLE, ACTIVE, CONFIRMED = 0, 1, 2\n        status = models.PositiveIntegerField(default=IDLE)\n        activated_at = models.DateTimeField(null=True, blank=True)\n        confirmed_at = models.DateTimeField(null=True, blank=True)\n\n        @snitch.dispatch(ACTIVATED_EVENT)\n        def activate(self):\n            self.activated_at = timezone.now()\n\n        @snitch.dispatch(CONFIRMED_EVENT)\n        def confirm(self):\n            self.confirmed_at = timezone.now()\n\n\nCustom Notification model\n-------------------------\n\nYou can, in the same way that ``django.contrib.auth.model.User`` works, swap the\nNotification model, to customize it.\n\nIn order to do that, you should create a model that inherits from\n``AbstractNotification``:\n\n.. code-block:: python\n\n    from django.db import models\n\n    from snitch.models import AbstractNotification\n\n\n    class Notification(AbstractNotification):\n        """Custom notification."""\n\n        extra_field = models.BooleanField(default=False)\n\n\nAnd after that, specify it in the settings:\n\n.. code-block:: python\n\n    SNITCH_NOTIFICATION_MODEL = "app.Notification"\n',
    'author': 'Marcos Gabarda',
    'author_email': 'hey@marcosgabarda.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/marcosgabarda/django-snitch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
