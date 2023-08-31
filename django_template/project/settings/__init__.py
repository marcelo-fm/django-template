import os.path
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# Namespacing our own custom enviroment variables
ENVVAR_PREFIX = "DJANGO_TEMPLATE_"

include("base.py", "custom.py", optional("settings.dev.py"), "envvars.py")
