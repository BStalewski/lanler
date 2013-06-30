#!/usr/bin/python
# -*- coding: utf-8 -*-

from db import DB

from PyQt4.QtCore import QString


class Model:
    def __init__(self):
        self.db = DB.get_instance()
        self.current_user_name = None

    def assert_user(fun):
        def wrapper(self, *args, **kwargs):
            if not self.current_user_name:
                raise ModelException('User is none')

            return fun(self, *args, **kwargs)

        return wrapper

    def to_model_format(fun):
        def wrapper(self, *args, **kwargs):
            new_args = []
            for arg in args:
                new_arg = arg.__str__() if isinstance(arg, QString) else arg
                new_args.append(new_arg)

            new_kwargs = {}
            for key, value in kwargs.items():
                new_key = key.__str__() if isinstance(key, QString) else key
                new_value = value.__str__() if isinstance(value, QString) else value
                new_kwargs[new_key] = new_value

            return fun(self, *new_args, **new_kwargs)

        return wrapper

    @to_model_format
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

    @to_model_format
    @assert_user
    def add_noun(self, polish, portuguese, gender):
        print 'type(polish)', type(polish)
        #polish = qpolish.__str__()
        #portuguese = qportuguese.__str__()
        #gender = qgender.__str__()
        if not polish:
            raise ModelException('Polish empty')

        if not portuguese:
            raise ModelException('Portuguese empty')

        self.db.add_noun(self.current_user_name, polish, portuguese, gender)


class ModelException(Exception):
    pass
