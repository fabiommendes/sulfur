==========================
Frequently asked questions
==========================

Usage
=====

Do I have to use pytest and Django during testing?
--------------------------------------------------

For now yes. This is the setup I use and if I assume these settings I can take
some shortcuts during development. That said, it should not be hard to support
other scenarios.

Please contact the developers (or better yet, contribute code!) and explain your
sittuation. We want to make sulfur backend agnostic before v1.0.


Concepts
========

What is a web driver?
---------------------

A web driver is a component that is used to control your web browser from an
external source. Each web browser must have its own driver installed. Sulfur
will not work with a web browser unless the corresponding web driver is
installed.