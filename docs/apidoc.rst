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


Forms interface
---------------



Window control
--------------

The ``Driver.window`` attribute controls the browser window. These methods are
disabled in headless drivers such as 'phantomjs'

.. autoclass:: sulfur.driver.WindowManager
   :members:


Managing cookies
----------------

The ``Driver.cookie`` attribute allows to modify and retrieve data stored as
cookies.

.. autoclass:: sulfur.driver.CookieManager
   :members:


Url checker
===========




