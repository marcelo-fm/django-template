import os.path
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# Namespacing our own custom enviroment variables
ENVVAR_PREFIX = "DJANGO_TEMPLATE_"


LOCAL_SETTINGS_PATH = os.getenv(
    f"{ENVVAR_PREFIX}LOCAL_SETTINGS_PATH", "local/settings.dev.py"
)

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, LOCAL_SETTINGS_PATH)

include(
    "base.py",
    optional(LOCAL_SETTINGS_PATH),
)
