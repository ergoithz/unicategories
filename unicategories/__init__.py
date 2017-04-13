from . import cache
from .tools import merge, RangeGroup

__all__ = ['categories', 'merge', 'RangeGroup']

categories = \
    cache.load_from_package() or \
    cache.load_from_cache() or \
    cache.generate_and_cache()
