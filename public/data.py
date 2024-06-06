from dataclasses import dataclass, field

@dataclass
class Feature:
    title: str
    active: bool
    name: str
    description: str
    code_example: str 
    class_name: str = ""
    idx: 0 = 0

@dataclass
class Features:
    features: list[Feature]
