
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import BaseView, expose, has_access, ModelView, ModelRestApi

from . import appbuilder, db

"""
    Create your Model based REST API::
    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)
    appbuilder.add_api(MyModelApi)
    Create your Views::
    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)
    Next, register your Views::
    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )



class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and return to previous page or index

        return 'Hello'


appbuilder.add_view(MyView, "Method1", category='My View')



db.create_all()