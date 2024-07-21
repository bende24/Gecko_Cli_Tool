from typing import TypedDict, Optional, Dict


class AliasDetails(TypedDict, total=False):
    command: str
    description: Optional[str]


Aliases = Dict[str, AliasDetails]


class Settings(TypedDict):
    currentAliases: str
