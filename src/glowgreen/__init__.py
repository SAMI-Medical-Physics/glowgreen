#"""
import importlib.metadata
try:
    __version__ = importlib.metadata.version("glowgreen")
except importlib.metadata.PackageNotFoundError:
    __version__ = None
#"""
#__version__ = "0.0.3"

# import glowgreen.clearance
from .clearance import Clearance_1m

# import glowgreen.close_contact
from .close_contact import (
    ContactPatternRepeating,
    ContactPatternOnceoff,
    cs_restrictions,
    cs_patterns,
    restrictions_for,
)
