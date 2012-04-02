from urlparse import urlparse, urljoin
from flask import request, url_for, redirect
from flaskext.wtf import Form, TextField, HiddenField

# http://flask.pocoo.org/snippets/62/
def is_safe_url(target):
    ''' Ensure that a redirect targets leads to the same server. '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and\
           ref_url.netloc == test_url.netloc


def get_redirect_target():
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


class RedirectForm(Form):
    next = HiddenField()

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        if not self.next.data:
            self.next.data = get_redirect_target() or ''

    def redirect(self, endpoint='home.show_home', force_endpoint=False, **values):
        if force_endpoint:
            return redirect(url_for(endpoint, **values))

        if is_safe_url(self.next.data):
            return redirect(self.next.data)

        target = get_redirect_target()
        return redirect(target or url_for(endpoint, **values))
