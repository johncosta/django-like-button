import logging
import hashlib
from django.template import Library, Node
from django.conf import settings
from django.utils import simplejson
from django.utils.importlib import import_module

register = Library()
log = logging.getLogger(__name__)

FACEBOOK_APP_ID = getattr(settings, 'FACEBOOK_APP_ID', None)
FACEBOOK_SHOW_SEND = getattr(settings, 'FACEBOOK_SHOW_SEND', True)
FACEBOOK_LIKE_WIDTH = getattr(settings, 'FACEBOOK_LIKE_WIDTH', '450')
FACEBOOK_SHOW_FACES = getattr(settings, 'FACEBOOK_SHOW_FACES', True)
FACEBOOK_FONT = getattr(settings, 'FACEBOOK_FONT', 'arial')

def my_import(name):
    """ dynamic importing """
    module, attr = name.rsplit('.', 1)
    mod = __import__(module, fromlist=[attr])
    klass = getattr(mod, attr)
    return klass()

def true_false_converter(value):
    return 'true' if value else 'false'

@register.inclusion_tag('like_button/like_button_js_tag.html', takes_context=False)
def like_button_js_tag():
    """ This tag will check to see if they have the FACEBOOK_LIKE_APP_ID setup
        correctly in the django settings, if so then it will pass the data along
        to the intercom_tag template to be displayed.
        
        If something isn't perfect we will return False, which will then not 
        install the javascript since it isn't needed.

    """

    if FACEBOOK_APP_ID is None:
        log.warning("FACEBOOK_APP_ID isn't setup correctly in your settings")

    # make sure FACEBOOK_APP_ID is setup correct and user is authenticated
    if FACEBOOK_APP_ID:

        return {"LIKE_BUTTON_IS_VALID" : True,
                "facebook_app_id":FACEBOOK_APP_ID,
                }

    # if it is here, it isn't a valid setup, return False to not show the tag.
    return {"LIKE_BUTTON_IS_VALID" : False}

@register.inclusion_tag('like_button/like_button_tag.html', takes_context=True)
def like_button_tag(context):
    """ This tag will check to see if they have the FACEBOOK_APP_ID setup
        correctly in the django settings, if so then it will pass the data along
        to the intercom_tag template to be displayed.

        If something isn't perfect we will return False, which will then not
        install the javascript since it isn't needed.
s
    """

    if FACEBOOK_APP_ID is None:
        log.warning("FACEBOOK_APP_ID isn't setup correctly in your settings")

    # make sure INTERCOM_APPID is setup correct and user is authenticated
    if FACEBOOK_APP_ID:

        request = context['request']
        path_to_like = request.get_host() + request.get_full_path()
        show_send = true_false_converter(FACEBOOK_SHOW_SEND)
        like_width = FACEBOOK_LIKE_WIDTH
        show_faces = true_false_converter(FACEBOOK_SHOW_FACES)
        font = FACEBOOK_FONT

        return {"LIKE_BUTTON_IS_VALID" : True,
                "path_to_like": path_to_like,
                "show_send": show_send,
                "like_width": like_width,
                "show_faces": show_faces,
                "font": font,
        }

    # if it is here, it isn't a valid setup, return False to not show the tag.
    return {"LIKE_BUTTON_IS_VALID" : False}