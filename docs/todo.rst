TODO
====

Run through these options and suport them

* href - the URL to like. The XFBML version defaults to the current page.
* send - specifies whether to include a Send button with the Like button. This only works with the XFBML version.
* layout - there are three options.
* standard - displays social text to the right of the button and friends' profile photos below. Minimum width: 225 pixels. Minimum increases by 40px if action is 'recommend' by and increases by 60px if send is 'true'. Default width: 450 pixels. Height: 35 pixels (without photos) or 80 pixels (with photos).
* button_count - displays the total number of likes to the right of the button. Minimum width: 90 pixels. Default width: 90 pixels. Height: 20 pixels.
* box_count - displays the total number of likes above the button. Minimum width: 55 pixels. Default width: 55 pixels. Height: 65 pixels.
* show_faces - specifies whether to display profile photos below the button (standard layout only)
* width - the width of the Like button.
* action - the verb to display on the button. Options: 'like', 'recommend'
* font - the font to display in the button. Options: 'arial', 'lucida grande', 'segoe ui', 'tahoma', 'trebuchet ms', 'verdana'
* colorscheme - the color scheme for the like button. Options: 'light', 'dark'
* ref - a label for tracking referrals; must be less than 50 characters and can contain alphanumeric characters and some punctuation (currently +/=-.:_). The ref attribute causes two parameters to be added to the referrer URL when a user clicks a link from a stream story about a Like action:
* fb_ref - the ref parameter
* fb_source - the stream type ('home', 'profile', 'search', 'other') in which the click occurred and the story type ('oneline' or 'multiline'), concatenated with an underscore.