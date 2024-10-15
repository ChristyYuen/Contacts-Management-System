"""
This file defines the database models
"""
import datetime

from . common import db, Field, auth
from pydal.validators import *

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#

def get_user_email():
	return auth.current_user.get('email') #getting user's email 


db.define_table('contacts',
	Field('first_name'),
	Field('last_name'),
	Field('user_email', default=get_user_email)
)

#Phone Table(phone_number, kind, contact_id)
db.define_table('phone',
    Field('phone_number'),
    Field('kind'),
    Field('contact_id', 'reference contacts')
)


db.contacts.id.readable = False #checking that only the user can change the data
db.contacts.user_email.readable = False
db.contacts.id.readable = False 
db.contacts.user_email.readable = False
db.phone.id.readable = False
db.phone.contact_id.readable = False

db.commit() #commiting the changes to the database
