django-revkom
=============

Django-revkom is Adam Wright's in vitro development repository. Generic
code in real projects is DRYed out by being refactored to this repository.
Modules of reusable, sharable code may then be extracted from this repo
into MIT-licensed Python packages. As such, this repository should be
considered an experimental staging area.

Currently, my plans involve:

- revkom-helpers: Software patterns, generic utils, helpful mixins and more
  
  Carrying the package name 'revkom', this will be where the most generic
  constructs live, if they're likely to be used by spin-off projects
  emerging from this repository.

- django-cinch: Code Is Not Configuration. However...

  Modular settings, with a sensible default project configuration.

- django-sassmouth: A Djagno Staticfiles backend for compiling Sass/SCSS

  Intended to be a small, standalone, pure-Python backend for compiling
  Sass et al. Good alternatives exist as extensions for django-pipeline
  and elsewhere. At the time of writing, pyScss is under heavy development
  and not quite up to working with Zurb Foundation, so the project's on
  hold and I'm using Compass to compile my Sassy files.

- django-hostess: Virtual host and subdomain processing for Django

  Alternatively, you could use django-subdomains, which is mature. I want
  to take a philosophically different direction, however...
