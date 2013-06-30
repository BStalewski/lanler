#!/usr/bin/python
# -*- coding: utf-8 -*-

from user import User

from pymongo import MongoClient

class DB:
    instance = None

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['lanler']
        self.users = self.db['users']
        self.words = self.db['words']

        if self.is_db_clean():
            print 'INIT DB'
            self.init_db()

    def get_users_names(self):
        return [user['name'] for user in self.users.find()]

    def clean(self):
        self.users.remove()
        self.words.remove()

    def close(self):
        self.client.close()

    def init_db(self):
        self.create_user(u'Gość', [])

    def is_db_clean(self):
        return self.users.count() == self.words.count() == 0

    def create_user(self, name, vocabulary_import_users):
        if name in self.get_users_names():
            raise DBException('User name {0} already in db'.format(name.encode('utf-8')))

        '''
        sorted_ids = sorted([int(uid) for uid in self.data.keys()])
        try:
            next_id = sorted_ids[-1] + 1
        except IndexError:
            next_id = 1

        self.data[str(next_id)] = User(next_id, name, vocabulary)
        '''
        if vocabulary_import_users:
            raise DBException('Copying vocabulary not implemented yet')

        new_user = {
            u'name': name
        }
        self.users.insert(new_user)

    def add_noun(self, username, polish, portuguese, gender):
        user = self.users.find_one({'name': username})
        if not user:
            raise DBException('Unknown user')

        new_noun = {
            u'user': user['_id'],
            u'polish': polish,
            u'portuguese': portuguese,
            u'gender': gender, 
        }

        self.words.insert(new_noun)
        

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = DB()

        return cls.instance


class DBException(Exception):
    pass
