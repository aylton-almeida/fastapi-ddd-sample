from importlib import import_module
from os.path import dirname as _dirname

from src.utils.ModuleAll import get_module_all as _get_module_all

controllers = _get_module_all(_dirname(__file__), '*_controller.py')
controllers = [import_module(f'{__name__}.{c}') for c in controllers]
