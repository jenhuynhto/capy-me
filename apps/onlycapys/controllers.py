"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.form import Form, FormStyleBulma
import requests
from py4web.utils.url_signer import URLSigner
from py4web import response
from .models import get_username
import datetime
url_signer = URLSigner(session)
MAX_RETURNED_USERS = 20 # Our searches do not return more than 20 users.

# Index Page
@action("index",  method=["GET", "POST"])
@action.uses("index.html", auth, T)
def index():
    return dict(form=form)

# Our Team Page
@action("about")
@action.uses("about.html", auth, T)
def about():
    return dict( about_us_url = URL('about'))

# Contact Us Page
@action("form", method=["GET", "POST"])
@action.uses("Forum.html", db, session, T)
def form():
    return dict()

#Capy Fact Page
@action("zoos", method=["GET", "POST"])
@action.uses("zoos.html", db, auth.user, T)
def zoo():
    
    form = Form(db.capyfacts, csruf_session=session, formstyle=FormStyleBulma)
    if form.accepted:
        redirect(URL('zoos'))
    return dict(form=form,
                get_capyfacts_url = URL('capyfact'),
                add_post_url = URL('add_post'),
                get_posts_url = URL('get_posts'),  
                )
    

@action("capyfact", method=["GET", "POST"])
@action.uses(db)
def facts():
    facts = db(db.capyfacts).select(orderby=~db.capyfacts.id)
    
    return dict(facts=facts)