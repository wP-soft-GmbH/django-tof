![GitHub issues](https://img.shields.io/github/issues/danilovmy/django-tof.svg)
![GitHub stars](https://img.shields.io/github/stars/danilovmy/django-tof.svg)
![GitHub Release Date](https://img.shields.io/github/release-date/danilovmy/django-tof.svg)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/danilovmy/django-tof/latest.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/danilovmy/django-tof.svg)
[![GitHub license](https://img.shields.io/github/license/danilovmy/django-tof)](https://github.com/danilovmy/django-tof/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ef1b0b5bb51048a6a03f3cc87798f9f9)](https://www.codacy.com/manual/danilovmy/django-tof?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=danilovmy/django-tof&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/danilovmy/django-tof/branch/master/graph/badge.svg)](https://codecov.io/gh/danilovmy/django-tof)

[![PyPI](https://img.shields.io/pypi/v/django-tof.svg)](https://pypi.python.org/pypi/django-tof)
[![PyPI](https://img.shields.io/pypi/pyversions/django-tof.svg)]()
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-tof.svg?label=pip%20installs&logo=python)

# django-tof
Django models translation on fly 🛸️
THIS FORK IS THE NEXT VERSION OF DJANGO_TOF V 1.0
----
This project was initiated, promoted and accompanied by winePad GmbH (winePad.at). All development based on ideas, experience and support from Maxim Danilov (winePad GmbH).
----

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/i0QJJJEMKSU/0.jpg)](https://www.youtube.com/watch?v=i0QJJJEMKSU)

_[Russian readme](README_ru.md)_

----
The background and objectives of this projects are described [here](https://github.com/danilovmy/django-tof/wiki/django-tof)

An Application for dynamic translation of existing Django models into any number of languages.

  - without need to change existing model classes
  - without need to reboot servers
  - without changing the use of translated fields
  - ready to work after install and indicated in INSTALLED_APPS
  - fully integrated in Django modelAdmin, and ModelInline

## Installation

`pip install git+https://github.com/danilovmy/django-tof.git`
`python manage.py migrate tof`

~~~python
# settings.py
...
INSTALLED_APPS = [
...
'tof',
...
]
~~~

Don't forget to do if it necessary:
`python manage.py collectstatic`

## How to use

  1. In the simplest use case django-tof allows you to store translation into the current language.
You don't need special settings for this, just add this field into admin panel to the "Translatable fields" model.
In this case if current language is 'en', then the value saved in the model will be displayed only if the current language is 'en'.
  1. If you need to support a certain number of languages and add them at the same time, you can use `TofAdmin`.
Using the `class CustomModelAdmin(TofAdmin)` will cause the translated fields (added to the "Translatable fields") will be able to specify a specific language.

At the same time, it is possible to leave some fields in the previous form by specify them in `TofAdmin` with attribute `only_current_lang = ('description', )`. <br>

![Widget for translatable fields](https://raw.githubusercontent.com/danilovmy/django-tof/master/docs/images/field_with_langs.jpeg)
  1. You can also use inline translation submission forms. To do this, specify admin class (always inherited from "TofAdmin") `inlines = (TranslationTabularInline, )`
or `inlines = (TranslationStackedInline, )`

## Programmatic use
Like a standard using, but it is possible to get a specific translation.

~~~python
from django.utils.translation import activate

activate('en')
book = Book.objects.first()
book.title  # => Title en
book.title.de  # => Title de
~~~

## Settings

_The value for these variables can be specified in your settings.py_

DEFAULT_LANGUAGE: _default_ "en" - Default language is stub, used if not other translations is found.

FALLBACK_LANGUAGES: _default_ `{SITE_ID: ('en', 'de', 'ru'), 'fr': ('nl', ),}` - Determinate the order of search of languages for translation if the translation is in desired
no language. The key can be SITE_ID, None or language.

The processing order is this, if a translation into current/requested language is not found, then first we checked by the language key, if there is, looking translations for requested languages,
if not - we take the SIDE_ID key.
For example:

  - if current language "fr", then searching order will be next: "fr" -> "nl" -> DEFAULT_LANGUAGE -> then if there is an original value that was before the declaration of this field like translatable.
  - if current language "en", then searching order will be next "en" -> "de" -> "ru" -> DEFAULT_LANGUAGE -> then if there is an original value that was before the declaration of this field like translatable.

DEFAULT_FILTER_LANGUAGE: _default_ "current" - Indicates in which translations search/filter values. May be in the next forms `__all__`, `current`, `['en', 'de']`, `{'en', ('en', 'de', 'ru')}`

  - `current` - if this value is assigned, the filtering is occurs only on the translation into the current language. This is a default value.
  - `__all__` - if this value is assigned, the filtering is occurs for all translations.
  - `['en', 'de']` - if this value is assigned, the filtering is occurs according to translations of the specified languages.
  - `{'en', ('en', 'de', 'ru')}` - if this value is assigned, the filtering is occurs according to translations of languages received by the key of current language.

CHANGE_DEFAULT_MANAGER: _default_ "True" - Changing the default manager of the model. If it True, then standard manager is transferred into class attribute "objects_origin",
and "objects" becomes the standard manager inherited from standard with adding the functionality that recognized translated fields and takes into account settings from  DEFAULT_FILTER_LANGUAGE.

## Requirements

  - Python (\>=3.9)
  - Django (\>=4.0)