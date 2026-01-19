""" """
"""
Data class: simple class that is a collection of fields. 
I see a usage as a DTO.

Class builders shortcuts to write data classes:
- collections.namedtuple The simplest way—available since Python 2.6 (immutable).
- typing.NamedTuple An alternative that requires type hints on the fields—since Python 3.5, with class syntax 
  added in 3.6 (immutable).
- @dataclasses.dataclass A class decorator that allows more customization than previous alternatives, adding lots of 
  options and potential complexity—since Python 3.7 (mutable).
  
Focus on dataclass decorator:
Reads the variable annotations and automatically generates methods for your class.
The @dataclass decorator does not depend on inheritance or a metaclass, so it should not interfere with your own 
use of these mechanisms.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'