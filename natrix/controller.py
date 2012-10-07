'''
USAGE: `from natrix.controller import *`

Example controller:
```
# File: users_controller.py
@get('/users')
def index():
    if not GET.sort_by in ['rank', 'name']:
        return abort(403, 'wrong request')

    v.title = 'Our users'
    v.item_list = Article.all().order('-%s' % GET.sort_by)

    # return render('index.html')
    # will render 'users/index.html'
    # but `return render` is optional. returned None.
    # automatically render 'users/index.html'
    # ("controller name"/"function name")
```

ROUTE
=====

route  - general route
get    - get only route (shortcut)
post   - post only route (shortcut)
put    - put method only route (shortcut)
delete - delete method only route (shortcut)
... other methods has no shortcut (head, option)

@route('/hello/world', methods=['get', 'post'])
@get('/hello/world')
@post('/hello/world')


REQUEST
=======

Required actions: set session key, get session key

session - session dotdict
flash   - flash session dotdict
GET     - get request dotdict
POST    - post request dotdict


TEMPLATE
========

v - view context dotdict


FUNCTIONS
=========

abort - abort(404), abort(403), abort(404, 'hello'), abort(500, 'Sorry')
render - render('template_name.html')
redirect - redirect('users:index')  <= redirect to "users:index" route
         - redirect(':index')       <= redirect to "[CONTROLLER]:index"
         - redirect('/users/index') <= redirect to string link
         - redirect('users/index')  <= redirect to string link
'''
