import sys
import collections
import itertools
import unicodedata
import bisect

PY_LEGACY = sys.version_info < (3, )

if PY_LEGACY:
    chr = unichr  # noqa
    range = xrange  # noqa
    map = itertools.imap  # noqa


class RangeGroup(tuple):
    '''
    Immutable iterable representing a list of unicode code point ranges.

    Every range is reperesented using a tuple (start, end), with **end** itself
    being outside range for compatibility with python's :func:`range` builtin.

    It is assumed given data does not contain any overlapping range and it is
    already sorted from small to bigger range start. If it is not, use
    :func:`unicategories.merge` to fix values prior to passing to this.
    '''
    def __new__(cls, range_list=()):
        '''
        Create and return a new object.  See help(type) for accurate signature
        '''
        return super(RangeGroup, cls).__new__(cls, map(tuple, range_list))

    def __add__(self, other):
        '''
        Return self+value.
        x.__add__(y) <==> x+y
        '''
        return merge(self, other)

    def __mul__(self, mult):
        '''
        Return self*value.
        x.__mul__(n) <==> x*n
        '''
        return self

    def characters(self):
        '''
        Get iterator with all characters on this range group.

        :yields: iterator of characters (str of size 1)
        :ytype: str
        '''
        return map(chr, self.codes())

    def codes(self):
        '''
        Get iterator for all unicode code points contained in this range group.

        :yields: iterator of character index (int)
        :ytype: int
        '''
        for start, end in self:
            for item in range(start, end):
                yield item

    def has(self, character):
        '''
        Get if character (or character code point) is contained by any range on
        this range group.

        :param character: character or unicode code point to look for
        :type character: str or int
        :returns: True if character is contained by any range, False otherwise
        :rtype: bool
        '''
        if not self:
            return False
        character = character if isinstance(character, int) else ord(character)
        last = self[-1][-1]
        start, end = self[bisect.bisect_right(self, (character, last)) - 1]
        return start <= character < end

    def __repr__(self):
        '''
        Return repr(self).
        repr(object) -> string

        Return the canonical string representation of the object.
        For most object types, eval(repr(object)) == object.
        '''
        return '%s(%s)' % (
            self.__class__.__name__,
            super(RangeGroup, self).__repr__()
            )


def merge(*range_lists, **kwargs):
    '''
    Join given range groups, collapsing their overlapping ranges. If only one
    group is given, this method will still fix it (sort and collapsing).

    No typecheck is performed, so a valid range group will be any iterable
    (or iterator) containing an (start, end) iterable pair. Result type will
    be defined by group_class parameter (defaults to RangeGroup)

    :param *range_lists: several range groups to join
    :type *range_list: iterable of iterables
    :param group_class: result type, defaults to RangeGroup
    :type group_class: type
    :returns: merged range group
    :rtype: taken from group_class
    :
    '''
    group_class = kwargs.pop('group_class', RangeGroup)  # FIXME: python2
    range_list = [
        unirange
        for range_list in range_lists
        for unirange in range_list
        ]
    range_list.sort()
    it = iter(range_list)
    slast, elast = last = list(next(it))
    result = [last]
    for start, end in it:
        if start > elast:
            slast, elast = last = [start, end]
            result.append(last)
        elif end > elast:
            last[1] = elast = end
    return group_class(result)


def generate(categorize=unicodedata.category, group_class=RangeGroup):
    '''
    Generate a dict of RangeGroups for each unicode character category,
    including general ones.

    :param categorize: category function, defaults to unicodedata.category.
    :type categorize: callable
    :param group_class: class for range groups, defaults to RangeGroup
    :type group_class: type
    :returns: dictionary of categories and range groups
    :rtype: dict of RangeGroup
    '''
    categories = collections.defaultdict(list)
    last_category = None
    last_range = None
    for c in range(sys.maxunicode + 1):
        category = categorize(chr(c))
        if category != last_category:
            last_category = category
            last_range = [c, c + 1]
            categories[last_category].append(last_range)
        else:
            last_range[1] += 1
    categories = {k: group_class(v) for k, v in categories.items()}
    categories.update({
        k: merge(*map(categories.__getitem__, g))
        for k, g in itertools.groupby(sorted(categories), key=lambda k: k[0])
        })
    return categories
