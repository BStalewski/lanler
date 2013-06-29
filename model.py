#!/usr/bin/python
# -*- coding: utf-8 -*-

from db import DB

class Model:
    def __init__(self):
        self.db = DB.get_instance()
        pass

    def get_users_names(self):
        return self.db.get_users_names()

    def create_user(self, qname, import_user_names):
        name = qname.__str__()
        self.db.create_user(name, import_user_names)
