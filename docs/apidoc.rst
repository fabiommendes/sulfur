=============
API Reference
=============

API documentation for the sulfur module.

.. automodule:: sulfur
   :members:

Sulfur driver
=============

The sulfur web driver abstract many separate web drivers implemented in
Selenium using a single class. This is the main entry point for controlling the
navigator.

.. autoclass:: sulfur.Driver
   :members:
   :member-order: bysource


Forms interface
---------------

#TODO

Window control
--------------

The ``Driver.window`` attribute controls the browser window. These methods are
disabled in headless drivers such as 'phantomjs'

.. autoclass:: sulfur.driver.WindowManager
   :members:
   :inherited-members:



Managing cookies
----------------

The ``Driver.cookie`` attribute allows to modify and retrieve data stored as
cookies.

.. autoclass:: sulfur.driver.CookieManager
   :members:


Url checker
===========

The most basic URL check functionality is in the :mod:`sulfur.urlchecker`
module. It defines a function-based interface to check common mistakes in some
url.

.. automodule:: sulfur.urlchecker
   :members:
   :member-order: bysource

All these functions receive an optional ``client`` attribute that defines which
client object is used to fetch urls from a server. Sulfur provides clients
that makes real HTTP requests (ex.: :class:`sulfur.client.HTTPClient`) and clients
that mock those requests (ex.: :class:`sulfur.client.DjangoClient`).

Usually you want to provide this argument, unless you are satisfied with the
default client, which expects an HTTP server running on http://localhost:8000.

Clients
=======





