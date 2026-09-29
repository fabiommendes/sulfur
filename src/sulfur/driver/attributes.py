import collections

from selenium.webdriver.remote.webdriver import WebDriver

from .. import scripts
from ..element import Element
from ..utils.vector import Shape, Position


class DriverAttributeMixin:
    """
    Base class for several driver attributes.
    """

    _selenium: WebDriver

    def __init__(self, driver):
        self._sulfur = driver
        self._selenium = driver.selenium

    def _wrap_element(self, el):
        if el is None:
            return None
        return Element(el, self._sulfur)


class WindowManager(DriverAttributeMixin):
    """
    Driver .window attribute.
    """

    @property
    def shape(self):
        """
        Window shape as a (width, height) tuple.
        """
        shape = self._selenium.get_window_size()
        return Shape(**shape)

    @shape.setter
    def shape(self, value):
        width, height = value
        self._selenium.set_window_size(width, height)

    @property
    def position(self):
        pos = self._selenium.get_window_position()
        return Position(**pos)

    @position.setter
    def position(self, value):
        x, y = value
        self._selenium.set_window_position(x, y)

    def maximize(self):
        """
        Maximizes browser window.
        """

        self._selenium.maximize_window()

    def minimize(self):
        """
        Minimizes browser window.
        """

        self._sulfur.script(scripts.MINIMIZE_WINDOW, async=True)


class FocusManager(DriverAttributeMixin):
    """
    Driver .switch_to attribute.
    """

    def active(self):
        """
        Focus on active element.

        Selects page <body> if no element is active.
        """
        return self._wrap_element(self._selenium.switch_to)

    def alert(self):
        """
        Focus on an alert on page.
        """
        return self._wrap_element(self._selenium.switch_to.alert)

    def default_frame(self):
        """
        Focus on default frame.
        """
        return self._wrap_element(self._selenium.switch_to.default_content())

    def frame(self, reference):
        """
        Focus on specific frame.

        Reference can be a name, an index or an element.
        """

        return self._selenium.switch_to.frame(reference)

    def window(self, name='main'):
        """
        Switch to window specified by name.
        """

        return self._wrap_element(self._selenium.switch_to.window(name))


class CookieManager(DriverAttributeMixin, collections.Sequence):
    """
    Driver .cookies attribute.
    """

    @property
    def _data(self):
        return self._selenium.get_cookies()

    def __getitem__(self, key):
        if isinstance(key, str):
            return self._selenium.get_cookie(key)
        else:
            return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __setitem__(self, key, value):
        self.create(key, value)

    def __delitem__(self, key):
        self._selenium.delete_cookie(key)

    def clear(self):
        """
        Remove all cookies.
        """

        self._selenium.delete_all_cookies()

    def create(self, name=None, D=None, **kwargs):
        """
        Creates a new cookie with the given name.
        """

        if name is not None:
            kwargs['name'] = name
        if D is not None:
            kwargs = dict(D, **kwargs)
        return self._selenium.add_cookie(kwargs)
