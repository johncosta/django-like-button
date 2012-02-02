===============
django-intercom
===============

django-like-button makes it easy to use a facebook like button in your django application. You just need to do the following.

Installation
============
1. Install django-like-button using easy_setup or pip::

    pip install django-like-button

2. add like_button to your INSTALLED_APPS in your django settings file::

    INSTALLED_APPS = (
        # all
        # other 
        # apps
        'like_button',
    )

3. Add "FACEBOOK_APP_ID" setting to your django settings file with your facebook application Id.

    in settings.py::

        FACEBOOK_APP_ID = "your appID"

4. Add the template tag code into your base template before the body tag.

    At the top of the page put this::

    {% load like_button %}

    At the bottom of the page before the </body> tag put this::

    {% like_button_tag %}
