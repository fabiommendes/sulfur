import collections
import re


class QueriableMixin:
    """
    Mixin that defines the .get() and .query() methods for subclasses.
    """

    _query_tests = collections.OrderedDict()

    def elem(self, query, raises=True):
        """
        Returns the first element that satisfy the given query.
        """

        wrapper = self._wrap_element
        return self.__worker('find_element_by_', wrapper, query)

    def query(self, query):
        """
        QuerySet current page for the CSS selector pattern.
        """

        wrapper = self._wrap_query
        return self.__worker('find_elements_by_', wrapper, query)

    def _get_query_facade_delegate(self):
        raise NotImplementedError('must be implemented in subclasses')

    def _wrap_element(self, element):
        raise NotImplementedError('must be implemented in subclasses')

    def _wrap_query(self, query):
        raise NotImplementedError('must be implemented in subclasses')

    def _get_query_type(self, query):
        for func, name in self._query_tests.items():
            if func(query):
                return name
        return 'css'

    def __worker(self, base, wrapper, query):
        delegate = self._get_query_facade_delegate()
        query_type = self._get_query_type(query)
        method = getattr(delegate, base + query_type)
        return wrapper(method(query))


#
# Utility functions
#
TAG_SELECTOR_REGEX = re.compile(r'^(\w|-)+$')
ID_SELECTOR_REGEX = re.compile(r'^\#(\w|-)+$')
CLASS_SELECTOR_REGEX = re.compile(r'^\.(\w|-)+$')


def is_id_selector(selector):
    """
    Return True if CSS selector is of the form #id-name.
    """

    return ID_SELECTOR_REGEX.match(selector) is not None


def is_class_selector(selector):
    """
    Return True if CSS selector is of the form #id-name.
    """

    return CLASS_SELECTOR_REGEX.match(selector) is not None


def is_tag_selector(selector):
    """
    Return True if CSS selector is of the form #id-name.
    """

    return TAG_SELECTOR_REGEX.match(selector) is not None


def is_xpath_selector(selector):
    """
    Return True if selector defines an xpath.
    """

    #TODO: Fixme
    return False


def is_link_selector(selector):
    """
    Return True if receives a link selector.
    """

    #TODO: Fixme
    return False


def is_partial_link_selector(selector):
    """
    Return True if receives a partial link selector.
    """

    #TODO: Fixme
    return False


def is_name_selector(selector):
    """
    Return True if receives a name selector.
    """

    #TODO: Fixme
    return False


QueriableMixin._query_tests.update([
    (is_id_selector, 'id'),
    (is_class_selector, 'class_name'),
    (is_tag_selector, 'tag_name'),
    (is_partial_link_selector, 'partial_link_name'),
    (is_link_selector, 'link_name'),
    (is_xpath_selector, 'xpath'),
    (is_name_selector, 'name'),
])
