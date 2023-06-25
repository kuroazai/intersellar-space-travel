from dataclasses import dataclass
from typing import List, Optional



@dataclass
class Accelerator:
    """Accelerator data model."""
    name: str
    connections: dict
