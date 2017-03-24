""""
Sulfur py.test plugin.
"""

# We don't want to import sulfur here in order to preserve the coverage stats
# for the sulfur package. If we import the sulfur module, parts of it will be
# loaded before coverage starts its tracer, hence many lines will not be
# counted when coverage runs.
import pytest


@pytest.fixture
def driver(driver):
    import sulfur
    return sulfur.Driver()


@pytest.fixture
def client(driver):
    import sulfur.client
    return sulfur.Driver()


@pytest.fixture
def urlchecker():
    """
    Return the sulfur.urlchecker module.
    """

    import sulfur.urlchecker
    return sulfur.urlchecker
