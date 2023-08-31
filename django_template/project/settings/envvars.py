from django_template.core.utils.collections import deep_update
from django_template.core.utils.settings import get_settings_from_enviroment

deep_update(globals(), get_settings_from_enviroment(ENVVAR_PREFIX))  # type: ignore
