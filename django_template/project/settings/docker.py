from django_template.project.settings.base import MIDDLEWARE


if IN_DOCKER:  # type: ignore
    assert MIDDLEWARE[:1] == [
        "django.middleware.security.SecurityMiddleware"
    ], "SecurityMiddleware must be the first middleware in the list"
