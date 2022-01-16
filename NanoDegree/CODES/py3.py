# PEP-589 (https://www.python.org/dev/peps/pep-0589/) (landed in Python 3.8)
# introduced typing.TypedDict as a way to annotate dicts:

from typing import TypedDict

class Movie(TypedDict):
  name: str
  year: int

movie: Movie = {
  'name': 'Blade Runner',
  'year': 1982,
}


# It cannot have keys that aren't explicitly specified in the type:

movie: Movie = {
  'name': 'Blade Runner',
  'year': 1982,
  'director': 'Ridley Scott',  # fails type checking
}
# Also, all specified keys are required by default but it can be changed by passing total=False:

movie: Movie = {} # fails type checking

class Movie2(TypedDict, total=False):
  name: str
  year: int

movie2: Movie2 = {} # ok
