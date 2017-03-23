Sulfur is a simplified web driver interface for python-selenium. Sulfur has
a more pleasant (and less java-esque) interface and also uses BeautifulSoup
to make an even tastier API.

Sulfur's main goal is to help writing tests for Web applications. It has
a builtin pytest plugin that defines a few useful fixtures, but it can also be
used with other testing libraries.

You can use Sulfur anywhere that Selenium would be used. Besides the obvious
use case of writing integration tests for web development, Sulfur can be used on
automation, data-mining, presentations, etc.


Basic Usage
===========

Let us start a new webdriver (sulfur uses PhantomJS by default):

>>> from sulfur import Driver
>>> driver = Driver('chrome', home='http://www.python.org')      # doctest: +SKIP

.. invisible-code-block:: python
    driver = Driver('phantomjs', home='http://www.python.org')

The driver object is used to control the web browser. Now you can send commands,
inspect the page, and interact with the browser in many ways. First say hello :)

>>> driver.script('alert("Hello World!")')

And now goodbye!

>>> driver.close()

Basic actions
=============

Sulfur supports basic navegations actions by the :meth:`sulfur.Driver.back`,
:meth:`sulfur.Driver.forward`, :func:`sulfur.Driver.home`, :meth:`sulfur.Driver.refresh`, and
:meth:`sulfur.Driver.open` methods.

User input can be simulated with the :meth:`sulfur.Driver.click`,
:meth:`sulfur.Driver.send_keys` methods. Sulfur also makes it possible to execute
scripts (:meth:`sulfur.Driver.script`), take screen shots (:meth:`Driver.screenshot`)
and fetch the page HTML source (:meth:`sulfur.Driver.source`).

The full API is covered at :class:`sufur.Driver`.

Selectors and queries
=====================


Page objects
============


Beautiful soup
==============


URL checkers
============



Testing in Django
=================



What's up with this name?
=========================

Sulfur is the element that sits just on top of Selenium in the periodic table.
Elements within the same column share many chemical and electronic properties,
but since Sulfur has an atomic number of only 16 (vs. 34 for Selenium), it is
considerably lighter ;)