# Copyright (c) 2025 iiPython

# Modules
import tomllib
from pathlib import Path

from .schema import BaseSchema

# Initialization
def load_config(file: Path) -> BaseSchema:
    return BaseSchema(**tomllib.loads(file.read_text()))
