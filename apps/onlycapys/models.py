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



db.commit()