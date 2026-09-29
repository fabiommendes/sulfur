import functools

import selenium.common


def wrap_selenium_timeout_error(func):
    """
    Decorator that wraps a function that may emmit a selenium timeout error to
    use Python's native TimeoutError.
    """

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except selenium.common.exceptions.TimeoutException as ex:
            raise TimeoutError(ex)

    return decorated


def get_driver_class_from_string(name):
    """
    Select driver class from name.
    """

    mapping = {
        'firefox': 'selenium.webdriver.Firefox',
        'chrome': 'selenium.webdriver.Chrome',
        'ie': 'selenium.webdriver.Ie',
        'edge': 'selenium.webdriver.Edge',
        'opera': 'selenium.webdriver.Opera',
        'safari': 'selenium.webdriver.Safari',
        'blackberry': 'selenium.webdriver.BlackBerry',
        'phantomjs': 'selenium.webdriver.PhantomJS',
        'android': 'selenium.webdriver.Android',
    }

    mod, _, cls = mapping[name].rpartition('.')
    mod = __import__(mod, fromlist=[cls])
    return getattr(mod, cls)


def open(url=None, driver='phantomjs', wait=0):
    """
    Opens a new web driver instance.

    Args:
        url: Home page url.
        driver: A string with the selected web driver (defaults to PhantomJS)
        wait: A timeout before making the driver active.

    Returns:
        A new Driver instance.
    """
    from .driver import Driver

    return Driver(driver, home=url, wait=wait)
