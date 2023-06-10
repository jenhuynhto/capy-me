"""
This file defines the database models
"""

from .common import db, Field, auth
from pydal.validators import *
import json
import os
import requests
### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#

def get_username():
    return auth.current_user.get('username') if auth.current_user else None

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

try:
    with open('../apps/onlycapys/data/capybara_zoos.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

except FileNotFoundError:
    with open('apps/onlycapys/data/capybara_zoos.json', 'rb') as file:
        data = json.load(file)

db.define_table('zoo',
                Field('name'),
                Field('address'),
                Field('lat'),
                Field('long'),
                Field('likes', default=0)
                )

db.define_table('capyfacts',
                Field('facts'),
                Field('username', default=get_username, readable=False, writable=False),
                auth.signature,
                )


# Make a GET request to fetch the facts from the API
# response = requests.get("https://api.capy.lol/v1/facts")

# if response.status_code == 200:
#     # Extract the data from the response
#     data = response.json()
#     facts = data["data"]

#     # Process the facts data as needed
#     # For example, you can store the facts in the database
    

# else:
#     # Handle the error if the request fails
#     print("Error loading facts:", response.status_code)

query = db(db.zoo.id > 0)
if query.isempty():
   for item in data:
    db.zoo.insert(
        name=item['zoo'],
        address=item['address'],
        lat=item['lat'],
        long=item['long']
    )
query2 = db(db.capyfacts.id > 0)
# if query2.isempty():
#     for fact in facts:
#         db.capyfacts.insert(facts=fact)
# db(db.zoo).delete()
#db(db.capyfacts).delete()

db.commit()