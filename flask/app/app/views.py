from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import BaseView, expose, has_access, ModelView, ModelRestApi

from . import appbuilder, db


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
