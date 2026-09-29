import string
from random import choice


def normalize_url(url):
    """
    Forces url to have a correct protocol specification.

    Examples:
        >>> normalize_url('google.com')
        'http://google.com'
    """

    if '://' not in url:
        return 'http://' + url
    return url


def select_hostname(url):
    """
    Return hostname from url.

    Examples:
        >>> select_hostname('http://python.org/about.html')
        'python.org'
        >>> select_hostname('python.org/foo')
        'python.org'
    """
    protocol, sep, host = url.rpartition('://')
    return host.partition('/')[0]


def select_url(base_url, new_url):
    """
    Select final URL from current url and new url fragment.
    """

    # Check if url starts with http://... This is a fully normalized url.
    protocol, sep, host = new_url.rpartition('://')
    if protocol:
        return new_url

    # Fetch absolute url from host
    if new_url.startswith('/'):
        protocol, sep, host = base_url.rpartition('://')
        return '%s://%s%s' % (protocol, select_hostname(base_url), new_url)

    # Fetches relative url
    else:
        protocol, sep, url = base_url.rpartition('://')
        url = url.rpartition('/')[0]
        if protocol:
            url = '%s://%s' % (protocol, url)
        return normalize_url('%s/%s' % (url, new_url))


def random_id():
    """
    Return a random string of text that can be used as an id.
    """
    return ''.join(choice(c) for c in string.ascii_letters)
