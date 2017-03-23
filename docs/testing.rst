==================
Writing unit tests
==================

Sulfur comes with a pytest plugin that defines a few useful fixtures. For now,
Sulfur depends on Django, but that will change before v1.0.


Django
======

First install `pytest-django`<https://pytest-django.readthedocs.io/en/latest/>
to expose some useful Django-relatd fixtures. Make sure pytest-django works on
your installation and points to the correct DJANGO_SETTINGS_MODULE.

Basic tests
-----------

Once everything works, you can start writing Sulfur-enabled test functions. A
very basic sanity check you should do with your application is to ensure that
the urls works and return valid HTML. This is very easy with Sulfur:

.. code-block:: python

    # tests/test_urls.py

    def test_auth_urls(client, user):
        url = '/auth/{username}/'.format(username=user.username)
        client.check_url(url, html5=True, check_links=True)


This test will check if the given url produces a valid status code and if
the source is a valid HTML5 with no broken links. The client fixture is defined
by Sulfur and returns an instance of a :class:`sulfur.urlcheckerclient.URLChecker`.
If the given url is not valid, it raises a :class:`sulfur.ValidationError`.

URL checking should be considered an "integration test" for your site. You
shouldn't rely on it to account for coverage or run it frequenty in test driven
development, but it is a nice additional check to do before a release.

If you are really lazy about testing your URLs, and you promess not using it
in your main test suite ;-), Sulfur offers the ``follow_links`` option. This
will check validity of all internal urls that can be reached from the given
page. Beware that if your site is very large this will take a very long time.


Web driver
----------

The check_url() method of Sulfur clients is only a very basic sanity check. If
you have a complex page, it will be necessary to use the web driver to interact
with the web page in a more meaningful way.

The web driver opens a browser window that can be controlled and monitored
programmatically. The example bellow opens the login page and tries to enter
a username and password.

.. code-block:: python

    # tests/test_auth.py

    def test_invalid_users_cannot_login(driver):
        driver.open('/login/')
        assert driver('input[type=submit]').is_visible

        driver.submit(
            email='foo@bar.com',
            password='foobar'
        )
        assert 'Invalid e-mail/password' in driver.source()

The web driver is very powerful and can be used to simulate many user
interactions with your web page. We refer to the :class:`sulfur.Driver`
documentation for more details.


Direct HTML inspection
----------------------

