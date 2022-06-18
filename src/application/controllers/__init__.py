from importlib import import_module
from os.path import dirname as _dirname

from src.utils.module_utils import get_modules_by_pattern as _get_modules_by_pattern

controllers = _get_modules_by_pattern(_dirname(__file__), "*_controller.py")
controllers = [import_module(f"{__name__}.{c}") for c in controllers]
