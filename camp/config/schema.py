# Copyright (c) 2025 iiPython

# Modules
import re
from typing import Self

from pydantic import BaseModel, NameEmail, field_validator
from pydantic_extra_types.country import CountryAlpha2

# Initialization
HOSTNAME_REGEX = re.compile(
    r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*$"
)

class SerializableContact(NameEmail):
    def serialize(self) -> list[str]:
        return [self.name, self.email]

class CabinSchema(BaseModel):
    region:   CountryAlpha2
    contact:  SerializableContact
    database: str

class GroupSchema(BaseModel):
    rooms:          list[str]
    database:       str
    allowed_cabins: list[str]

    @field_validator("allowed_cabins")
    def validate_cabins(cls: Self, value: list[str]) -> list[str]:
        if value == ["*"]:
            return []

        for hostname in value:
            if not HOSTNAME_REGEX.match(hostname):
                raise ValueError(f"invalid hostname: {hostname}")

        return value

class BaseSchema(BaseModel):
    cabin: CabinSchema
    group: GroupSchema
