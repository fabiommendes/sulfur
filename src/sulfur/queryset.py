from collections import Sequence


class QuerySet(Sequence):
    """
    A query set of elements in a page.

    Queries can be filtered and iterated. Most query methods can be chained
    as in the example:

    >>> q = ...  # driver method that return a query set object
    >>> q.filter('div').click()                                  # pytest: +SKIP
    """

    @property
    def is_visible(self):
        return all(x.is_visible for x in self)

    @property
    def is_enabled(self):
        return all(x.is_enabled for x in self)

    @property
    def is_selected(self):
        return all(x.is_selected for x in self)

    def __init__(self, parent, elements):
        self.parent = parent
        self.elements = elements

    def __repr__(self):
        data = ', '.join(repr(x) for x in self)
        return '<QuerySet: [%s]>' % data

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, i):
        return self.elements[i]

    def click(self):
        """
        Clicks on all selected elements.
        """

        [x.click() for x in self]
        return self
