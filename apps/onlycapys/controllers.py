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
from py4web import response



@action("index",  method=["GET", "POST"])
@action.uses("index.html", auth, T)
def index():
    #user = auth.get_user()
    #message = T("Hello {first_name}".format(**user) if user else "Hello")
    #actions = {"allowed_actions": auth.param.allowed_actions}

    #name = 'capybara'
    #api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    #response = requests.get(api_url, headers={'X-Api-Key': 'BvaoaJ22jGIP5JvtVnGW/Q==3Yl87cuMQIHgAN7D'})
    #if response.status_code == requests.codes.ok:
    #    print(response.text)
    #else:
    #    print("Error:", response.status_code, response.text)
    return dict(form=form)


@action("about")
@action.uses("about.html", auth, T)
def about():
    return dict( about_us_url = URL('about'))


@action("form", method=["GET", "POST"])
@action.uses("Forum.html", db, session, T)
def form():
    return dict()


@action("alert")
@action.uses("Alert.html", auth, T)
def form():
    return dict()

@action("zoos", method=["GET", "POST"])
@action.uses("zoos.html", auth, T)
def zoo():
    form = Form(db.capyfacts, csruf_session=session, formstyle=FormStyleBulma)
    if form.accepted:
        redirect(URL('zoos'))
    return dict(form=form,
                get_capyfacts_url = URL('capyfact'))

@action("capyfact", method=["GET", "POST"])
@action.uses(db)
def facts():
    facts = db(db.capyfacts).select()
    print("facts: ", facts)
    return dict(facts=facts)




