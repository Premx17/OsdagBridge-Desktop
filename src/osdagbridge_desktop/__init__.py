"""
OsdagBridge Desktop
Desktop graphical interface and 3D CAD visualization for steel bridges.
"""

import importlib
import sys

__version__ = "1.0.0"

_SUBMODULES = {
    "cad",
    "resources",
    "ui",
}

__all__ = [
    "__version__",
    "cad",
    "resources",
    "ui",
]

# Backward compatibility alias for packages still referencing osdagbridge.desktop
sys.modules.setdefault("osdagbridge.desktop", sys.modules[__name__])


def __getattr__(name: str):
    """Lazy-load submodules when accessed as attributes on the root package."""
    if name in _SUBMODULES:
        mod = importlib.import_module(f".{name}", package=__name__)
        sys.modules[f"{__name__}.{name}"] = mod
        sys.modules[f"osdagbridge.desktop.{name}"] = mod
        globals()[name] = mod
        return mod
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


def __dir__():
    return sorted(list(globals().keys()) + list(_SUBMODULES))
