django-revkom
=============

This is Adam Wright's 'in vitro' development repository. Code in real
projects which is generic enough gets refactored into this
repository. If it's deemed useful enough, it gets extracted and put into
its own package for redistribution. As such, you can consider this
repository an experimental staging area.

.. Currently, my plans involve:
.. 
.. - revkom-helpers: Software patterns, generic utils, helpful mixins and more
..   
..   Carrying the package name 'revkom', this will be where the most generic
..   constructs live, if they're likely to be used by spin-off projects
..   emerging from this repository.
.. 
.. - django-cinch: Code Is Not Configuration. However...
.. 
..   Modular settings, with a sensible default project configuration.
.. 
.. - django-sassmouth: A Djagno Staticfiles backend for compiling Sass/SCSS
.. 
..   Intended to be a small, standalone, pure-Python backend for compiling
..   Sass et al. Good alternatives exist as extensions for django-pipeline
..   and elsewhere. At the time of writing, pyScss is under heavy development
..   and not quite up to working with Zurb Foundation, so the project's on
..   hold and I'm using Compass to compile my Sassy files.
.. 
.. - django-hostess: Virtual host and subdomain processing for Django
.. 
..   Alternatively, you could use django-subdomains, which is mature. I want
..   to take a philosophically different direction, however...
.. 
.. - django-slater: or maybe woodlouse? For your debugging conveniences.
.. 
.. - django-psst: Project-specific settings toolkit
