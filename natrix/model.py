'''
USAGE: `from natrix.model import *`

Example model:

# No any class inheritance
username  = StringProperty(default='', unique=True)
firstname = String
level     = Integer
bio       = Text
is_admin  = Boolean
point     = Float
lorem     = DateTime
ipsum     = Date
dolor     = Time
amet      = List
magna     = StringList


CLASS METHODS
=============
def find(**kwargs):
    # Example: user.find(is_admin=True, level=1, point={'>=': 7.8})
    find({'is_admin': True, 'level >=': 1, 'point >=': 7.8})

def get_or_instance(**kwargs):
    # Example: user.get_or_instance(username='hello')

def get_or_create(**kwargs):
    # Example: user.get_or_create(username=blah)

INSTANCE METHODS
================


CUSTOM METHODS
==============
Examples:

def get_articles_by_category_id(cls, category_id):
    return Article.find('category_id =', category_id)

def area(self):
    return self.height * self.width
'''
