from typing import Dict, Optional, TypedDict


class AliasDetails(TypedDict, total=False):
    command: str
    description: Optional[str]


Aliases = Dict[str, AliasDetails]


class Settings(TypedDict):
    currentAliases: str
