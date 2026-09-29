import re

from selenium.common.exceptions import NoSuchElementException

from sulfur import exceptions


class QueriableMixin:
    """
    Mixin that defines the .get() and .find() methods for subclasses.
    """

    def elem(self, selector, unique=False, raises=False):
        """
        Returns the first element that satisfy the given selector.

        Return None if element is not found or raise a NotFoundError exception
        if raises=True.
        """

        if unique:
            qs = self.find(selector)
            if len(qs) == 1:
                return qs[0]
            msg = 'query %r returned %s elements' % (selector, len(qs))
            raise exceptions.MultipleElementsFoundError(msg)
        try:
            wrapper = self._wrap_element
            return wrapper(self._find_raw(selector, single=True))
        except NoSuchElementException:
            if raises:
                raise exceptions.NotFoundError('no element %r found' % selector)

    def find(self, selector):
        """
        QuerySet current page for the CSS selector pattern.

        Args:
            selector (str):
                A css or xpath selector.
        """
        wrapper = self._wrap_queryset
        return wrapper(self._find_raw(selector))

    def _get_selenium_queryset_object(self):
        raise NotImplementedError('must be implemented in subclasses')

    def _wrap_element(self, element):
        raise NotImplementedError('must be implemented in subclasses')

    def _wrap_queryset(self, selector):
        raise NotImplementedError('must be implemented in subclasses')

    def _find_raw(self, selector, single=False):
        delegate = self._get_selenium_queryset_object()
        attr, transform = get_selenium_method(selector, single=single)
        method = getattr(delegate, attr)
        return method(transform(selector))


#
# Utility functions
#

# CSS Grammar: https://www.w3.org/TR/CSS21/grammar.html#scanner
NONASCII = r'[\240-\377]'
UNICODE = r'\\[0-9a-f]{1,6}(\r\n|[ \t\r\n\f])?'
ESCAPE = r'{unicode}|\\[^\r\n\f0-9a-f]'.format(unicode=UNICODE)
NMSTART = r'[_a-z]|{nonascii}|{escape}'.format(nonascii=NONASCII, escape=ESCAPE)
NMCHAR = r'[_a-z0-9-]|{nonascii}|{escape}'.format(nonascii=NONASCII, escape=ESCAPE)
IDENT = r'-?{nmstart}(?:{nmchar})*'.format(nmstart=NMSTART, nmchar=NMCHAR)
NAME = r'(?:{nmchar})+'.format(nmchar=NMCHAR)

# Selectors regexes
CLASS_SELECTOR_REGEX = re.compile(r'\.{ident}'.format(ident=IDENT))
ID_SELECTOR_REGEX = re.compile(r'#{name}'.format(name=NAME))
TAG_SELECTOR_REGEX = re.compile(r'{ident}|\*'.format(ident=IDENT))
LINK_SELECTOR_RE = re.compile(r'(http://|https://|link:).*')

# Function factories
predicate_from_re = (lambda re: lambda x: re.fullmatch(x) is not None)
predicate_from_re_casefold = (lambda re: lambda x: re.fullmatch(x.casefold()) is not None)
is_false = (lambda x: False)

# Transformations
identity = (lambda x: x)
strip_n = (lambda n: lambda x: x[n:])
strip = (lambda st: strip_n(len(st)))
clean_link = (lambda x: x[5:] if x.startswith('link:') else x)
clean_xpath = strip('xpath:')
clean_name = strip('name:')
clean_css = strip('css:')
clean_plink = strip('~link:')

# Predicate functions
is_id_selector = predicate_from_re_casefold(ID_SELECTOR_REGEX)
is_class_selector = predicate_from_re_casefold(CLASS_SELECTOR_REGEX)
is_tag_selector = predicate_from_re_casefold(TAG_SELECTOR_REGEX)
is_link_selector = predicate_from_re(LINK_SELECTOR_RE)
is_xpath_selector = (lambda x: x.startswith('xpath:'))
is_partial_link_selector = (lambda x: x.startswith('~link:'))
is_name_selector = (lambda x: x.startswith('name:'))
is_css_selector = (lambda x: x.startswith('css:'))

# Priority list for css selectors
SELECTOR_TESTS = [
    (is_xpath_selector, clean_xpath, 'find_elements_by_xpath'),
    (is_name_selector, clean_name, 'find_elements_by_name'),
    (is_css_selector, clean_css, 'find_elements_by_css_selector'),
    (is_partial_link_selector, clean_plink, 'find_elements_by_partial_link_name'),
    (is_link_selector, clean_link, 'find_elements_by_link_name'),
    (is_id_selector, identity, 'find_elements_by_id'),
    (is_class_selector, identity, 'find_elements_by_class_name'),
    (is_tag_selector, identity, 'find_elements_by_tag_name'),
]


def get_selenium_method(selector, single=False):
    for predicate, transform, name in SELECTOR_TESTS:
        if predicate(selector):
            method = name, transform
            break
    else:
        method = 'find_elements_by_css_selector', clean_css
    if single:
        name, transform = method
        method = name.replace('find_elements', 'find_element'), transform
    elif method == 'find_elements_by_id':
        method = 'find_elements_by_css_selector', identity
    return method
