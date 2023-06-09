"""
This file defines the database models
"""

from .common import db, Field, auth
from pydal.validators import *
import json
import os

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#


try:
    with open('../apps/onlycapys/data/capybara_zoos.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

except FileNotFoundError:
    with open('apps/onlycapys/data/capybara_zoos.json', 'rb', encoding='utf-8') as file:
        data = json.load(file)

db.define_table('contact',
                Field('fullname', requires=IS_NOT_EMPTY(), label="Full Name"),
                Field('email', requires=IS_NOT_EMPTY(), label="E-mail"),
                Field('message', requires=IS_NOT_EMPTY(), label="Message")
                )

db.define_table('zoo',
                Field('name'),
                Field('address'),
                Field('lat'),
                Field('long'),
                Field('likes', default=0)
                )

db.define_table('userAddress',
                Field('userid', 'reference auth_user'),
                Field('address'),
                )

query = db(db.zoo.id > 0)
if query.isempty():
   for item in data:
    db.zoo.insert(
        name=item['zoo'],
        address=item['address'],
        lat=item['lat'],
        long=item['long']
    )

# db(db.zoo).delete()

db.commit()