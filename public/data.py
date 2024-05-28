from dataclasses import dataclass, field

@dataclass
class Feature:
    title: str
    active: bool
    name: str
    description: str
    code_example: str 

@dataclass
class Features:
    features: list[Feature]
