Modules
=======

This page documents the main modules of the **OC_lettings** project.

Overview
--------

The project is structured as a Django application with the following main modules:

- :ref:`oc_lettings_site`
- :ref:`lettings`
- :ref:`profiles`

Module Details
--------------

.. _oc_lettings_site:

oc_lettings_site
================

This is the main Django project module, containing:

- `settings.py`: project settings, configuration, and environment variables
- `urls.py`: main URL routing for the project
- `wsgi.py`: WSGI entry point for deployment
- `asgi.py`: ASGI entry point for asynchronous support

.. _lettings:

lettings
========

This Django app handles rental listings. It includes:

- Models for property listings
- Views for displaying listings
- Templates for user interface

.. _profiles:

profiles
========

This Django app manages user profiles. It includes:

- Models for users and profile information
- Views for displaying profiles
- Templates for user interface
