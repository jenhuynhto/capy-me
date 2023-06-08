"""
This file defines the database models
"""

from .common import db, Field, auth
from pydal.validators import *
import json
<<<<<<< HEAD
import os
=======
>>>>>>> 3d28c3686f2335d714b54b3a7b40a468142d0ca8

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#

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
<<<<<<< HEAD


=======
# Resets zoo in case of edit to json
db['zoo'].truncate()

with open('../apps/onlycapys/data/capybara_zoos.json', encoding='utf-8') as file:
    data = json.load(file)

# Inserts json data
for item in data:
    db.zoo.insert(
        name=item['zoo'],
        address=item['address'],
        lat=item['lat'],
        long=item['long']
    )
>>>>>>> 3d28c3686f2335d714b54b3a7b40a468142d0ca8

db.commit()