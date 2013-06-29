#!/usr/bin/python
# -*- coding: utf-8 -*-

import shelve
from copy import deepcopy

from user import User

from pymongo import MongoClient

class DB:
    db_fname = 'data'
    instance = None

    def __init__(self, fname):
        client = MongoClient('localhost', 27017)
        db = client['lanler']
        users = db['users_coll']

        self.data = shelve.open(fname, writeback=True)
        if self.is_db_clean():
            self.init_db()
        #self.clean()
        #self.init_db()

    def get_users_names(self):
        users_data = [(user.uid, user.name) for user in self.data.values()]
        return [name for (_, name) in sorted(users_data)]

    def clean(self):
        for key in self.data.keys():
            del self.data[key]

    def close(self):
        self.data.close()

    def init_db(self):
        self.create_user(u'Gość')

    def is_db_clean(self):
        return self.data == {}

    def create_user(self, name, vocabulary_import_users):
        if name in self.get_users_names():
            raise DBException('User name {0} already in db'.format(name.encode('utf-8')))

        sorted_ids = sorted([int(uid) for uid in self.data.keys()])
        try:
            next_id = sorted_ids[-1] + 1
        except IndexError:
            next_id = 1

        self.data[str(next_id)] = User(next_id, name, vocabulary)
        

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = DB(cls.db_fname)

        return cls.instance


class DBException(Exception):
    pass
