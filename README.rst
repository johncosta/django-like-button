==================
django-like-button
==================

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
        FACEBOOK_SHOW_SEND = "true"   # or "false, default is "true"
        FACEBOOK_LIKE_WIDTH = "450"   # "numeric value for width", default is 450
        FACEBOOK_SHOW_FACES = "true"  # or "false, default is "true"
        FACEBOOK_FONT = "font"        # default is "arial"

4. Add the template tag code into your base template before the body tag.

    In the template, in which you want to add button load tags:
    
    {% load like_button %}

    Where you need the like button::

    {% like_button_tag %}

    At the bottom of the page before the </body> tag put this (you only need to do this once)::

    {% like_button_js_tag %}

5. Add the url into your urls file.  This tries to address the issue identified
with facebooks like button here: http://stackoverflow.com/questions/2955012/facebook-javascript-sdk-fb-xd-fragment

    in urls.py::

        url(r'', include('like_button.urls')),
