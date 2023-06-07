"""
This file defines the database models
"""

from .common import db, Field
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

db.define_table('zoo',
                Field('name'),
                Field('address'),
                Field('lat'),
                Field('long'))

db['zoo'].truncate()

with open('../apps/onlycapys/data/capybara_zoos.json', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    db.zoo.insert(
        name=item['zoo'],
        address=item['address'],
        lat=item['lat'],
        long=item['long']
    )

db.define_table('contact',
                Field('fullname', requires=IS_NOT_EMPTY(), label="Full Name"),
                Field('email', requires=IS_NOT_EMPTY(), label="E-mail"),
                Field('message', requires=IS_NOT_EMPTY(), label="Message"))

db.commit()