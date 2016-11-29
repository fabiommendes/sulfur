import os
import random

import pytest

from sulfur import Driver
from sulfur.test_server import TestServer


@pytest.fixture(scope='session')
def server_path():
    return os.path.join(os.path.dirname(__file__), 'data')


@pytest.yield_fixture(scope='session')
def server(server_path, port):
    server = TestServer(path=server_path, port=port)
    server.start()
    yield
    server.stop()


@pytest.fixture(scope='session')
def port():
    return random.randint(8001, 65000)


@pytest.yield_fixture
@pytest.mark.usefixtures('server')
def driver(port):
    driver = Driver('chrome', url='http://localhost:%s/' % port)
    yield driver
    driver.close()
