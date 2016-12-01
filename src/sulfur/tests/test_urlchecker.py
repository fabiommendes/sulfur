import pytest

from sulfur import *


@pytest.fixture
def url(port):
    return 'http://localhost:%s/base.html' % port


@pytest.mark.usefixtures('server')
def test_url_checker(port, url):
    assert check_ok(url)
    assert check_success(url)
    assert check_2xx(url)
    assert not check_4xx(url)
    assert not check_3xx(url)
    assert not check_client_error(url)
    assert not check_server_error(url)
    assert check_404('http://localhost:%s/does-not-exist.html' % port)


def test_raises_on_error(url):
    with pytest.raises(ValidationError):
        check_server_error(url, raises=True)


def test_check_valid_html5(server):
    assert check_ok(server.base_url + 'base.html', html5=True)
    assert not check_ok(server.base_url + 'bad.html', html5=True)
    with pytest.raises(ValidationError):
        check_ok(server.base_url + 'bad.html', html5=True, raises=True)


def test_failed_post(url):
    assert check_5xx(url, post={'foo': 'bar'})


def test_multiple_urls(url, port):
    urls = [url, url[:-9] + 'bad.html']
    assert check_ok(urls)
    assert not check_ok(urls, html5=True)
