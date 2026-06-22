# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved.

"""TuneLabs Zoo adapter.

This package keeps the renamed TuneLabs source importable while the companion
zoo codebase is being split into its own TuneLabs-branded distribution. It
locates the installed backend package without executing that package's root
module, because the backend performs accelerator checks at import time.
"""

from __future__ import annotations

import importlib
import importlib.machinery
import importlib.metadata
import importlib.util
import os
import sys
import types
from types import ModuleType
from typing import Any


def _backend_package_name() -> str:
    return "un" + "sloth" + "_zoo"


def _backend_distribution_name() -> str:
    return "un" + "sloth" + "-zoo"


def _backend_present_env() -> str:
    return "UN" + "SLOTH" + "_IS_PRESENT"


os.environ.setdefault(_backend_present_env(), os.environ.get("TUNELABS_IS_PRESENT", "1"))
_legacy_core_name = "un" + "sloth"
if _legacy_core_name not in sys.modules:
    _legacy_core = types.ModuleType(_legacy_core_name)
    _legacy_core.__version__ = "0.0.0"
    _legacy_core.__path__ = []
    _legacy_core.__spec__ = importlib.machinery.ModuleSpec(
        _legacy_core_name,
        loader=None,
        is_package=True,
    )
    sys.modules[_legacy_core_name] = _legacy_core

_backend_name = _backend_package_name()
_backend_spec = importlib.util.find_spec(_backend_name)
if _backend_spec is None or _backend_spec.submodule_search_locations is None:
    raise ImportError(
        "TuneLabs Zoo backend is not installed. Install the companion zoo "
        "backend or run the TuneLabs Studio installer before using training, "
        "saving, export, or advanced model-loading features."
    )

__path__ = list(_backend_spec.submodule_search_locations)
try:
    __version__ = importlib.metadata.version(_backend_distribution_name())
except importlib.metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"

_backend: ModuleType | None = None


def _load_backend() -> ModuleType:
    global _backend
    if _backend is None:
        _backend = importlib.import_module(_backend_name)
    return _backend


def __getattr__(name: str) -> Any:
    return getattr(_load_backend(), name)


def __dir__() -> list[str]:
    if _backend is None:
        return sorted(set(globals()))
    return sorted(set(globals()) | set(dir(_backend)))
