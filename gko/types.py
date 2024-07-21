from typing import Dict, Optional, TypedDict


class AliasDetails(TypedDict, total=False):
    command: str
    description: Optional[str]
    relative: bool


Aliases = Dict[str, AliasDetails]


class Settings(TypedDict):
    currentAliases: str
    defaultRelative: bool
