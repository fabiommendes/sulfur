Sulfur is a simplified web driver interface for python-selenium. Sulfur has
a more pleasant and Pythonic interface and also uses BeautifulSoup
to build an even tastier API.

Sulfur's main goal is to help writing tests for Web applications. It has
a builtin pytest plugin that defines a few useful fixtures, but it can also be
used with other testing libraries.

You can use Sulfur anywhere that Selenium would be used. Besides the obvious
use case of writing integration tests for web development, Sulfur can be used on
automation, data-mining, presentations, spamming websites etc.


Basic Usage
===========

Let us start a new webdriver (sulfur uses PhantomJS by default):

>>> import sulfur
>>> driver = sulfur.open('http://www.python.org', driver='chrome')  # doctest: +SKIP

.. invisible-code-block:: python

    driver = sulfur.open('http://www.python.org')

The driver object is used to control the web browser. You can send commands,
inspect the page, and interact with the browser in many ways. First, lets say
hello :)

>>> driver.script('alert("Hello World!")')

And now goodbye!

>>> driver.close()

Actions
=======

Sulfur supports basic navegations actions (:meth:`sulfur.Driver.back`,
:meth:`sulfur.Driver.forward`, :func:`sulfur.Driver.home`, :meth:`sulfur.Driver.refresh`, and
:meth:`sulfur.Driver.open`).

User input can be simulated with the :meth:`sulfur.Driver.click`,
:meth:`sulfur.Driver.send_keys` methods. Sulfur also makes it possible to execute
scripts (:meth:`sulfur.Driver.script`), take screen shots (:meth:`Driver.screenshot`)
and fetch the page HTML source (:meth:`sulfur.Driver.source`).

The full API is covered at :class:`sufur.Driver`.

Selectors and queries
=====================

You can query elements in the current web page using a familiar CSS selector
syntax. The :meth:`driver.Driver.elem` method retrieves a single element and
:meth:`driver.Driver.query` returns a queryset with all matches to that query
selector.

>>> driver.find('p')  # fetches all <p>'s in page               # doctest: +SKIP
<QuerySet: [...]>

Queries can be nested just like jQuery.

>>> driver.query('div').find('p').filter('.emph')               # doctest: +SKIP
<QuerySet: [...]>

This finds all <divs>'s in the page, selects their <p>'s children and then
filters the result to paragraphs with the "emph" class.


What's up with this name?
=========================

Sulfur is the element right above Selenium in the periodic table. Elements
within the same column share many chemical and electronic properties.
Since Sulfur has an atomic number of only 16 (vs. 34 for Selenium), it can
replace Selenium in many places, but is considerably lighter ;)