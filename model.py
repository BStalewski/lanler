#!/usr/bin/python
# -*- coding: utf-8 -*-

from db import DB

class Model:
    def __init__(self):
        self.db = DB.get_instance()
        self.current_user_name = None

    def set_current_user(self, name):
        if name not in self.get_users_names():
            raise ModelException()

        self.current_user_name = name

    def get_users_names(self):
        return self.db.get_users_names()

    def create_user(self, qname, import_user_names):
        name = qname.__str__()
        self.db.create_user(name, import_user_names)

    def is_user_name_unique(self, qname):
        user_name = qname.__str__()
        return user_name not in self.get_users_names()

    def add_noun(self, polish, portuguese, gender):
        raise ModelException()


class ModelException(Exception):
    pass
