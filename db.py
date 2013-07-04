#!/usr/bin/python
# -*- coding: utf-8 -*-

from user import User

from pymongo import MongoClient


NOUN = 0
VERB = 1
ADJECTIVE = 2
PRONOUN = 3


class DB:
    instance = None
    WORDS_USER = u'user'
    WORDS_PL = u'polish'
    WORDS_PT = u'portuguese'
    WORDS_PT_PLURAL = u'pt_plural'
    WORDS_GEN = u'gender'
    WORDS_POS = u'pos'

    def __init__(self, clean=False):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['lanler']
        self.users = self.db['users']
        self.words = self.db['words']

        if clean:
            self.clean()

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

        if vocabulary_import_users:
            raise DBException('Copying vocabulary not implemented yet')

        new_user = {
            u'name': name
        }
        self.users.insert(new_user)

    def get_user(self, username):
        user = self.users.find_one({'name': username})
        if not user:
            raise DBException('Unknown user')
        else:
            return user


    def add_noun(self, username, polish, portuguese, gender):
        user = self.get_user(username)

        new_noun = {
            u'user': user['_id'],
            u'polish': polish,
            u'portuguese': portuguese,
            u'gender': gender, 
            u'pos': NOUN,
        }

        self.words.insert(new_noun)
        
    def get_words(self, username, sort_key=None):
        user = self.get_user(username)
        cursor = self.words.find({u'user': user['_id']})
        if sort_key:
            cursor = cursor.sort(sort_key)

        return list(cursor)

    @classmethod
    def get_instance(cls, clean=False):
        if not cls.instance:
            cls.instance = DB(clean)

        return cls.instance


class UsersCollection:
    NAME = u'name'
    GUEST_NAME = u'Gość'

    def __init__(self, users_coll):
        self.users = users_coll

    def init_coll(self):
        self.create_user(GUEST_NAME, [])

    def is_coll_clean(self):
        return self.users.count() == 0

    def clean(self):
        self.users.remove()

    def get_user(self, username):
        user = self.users.find_one({self.NAME: username})
        if not user:
            raise DBException('Unknown user')
        else:
            return user

    def create_user(self, name, vocabulary_import_users):
        if name in self.get_users_names():
            raise DBException('User name {0} already in db'.format(name.encode('utf-8')))

        if vocabulary_import_users:
            raise DBException('Copying vocabulary not implemented yet')

        new_user = {
            self.NAME: name
        }
        self.users.insert(new_user)

    def get_users_names(self):
        return [user[self.NAME] for user in self.users.find()]


class WordsCollection:
    USER = u'user'
    POLISH = u'polish'
    PORTUGUESE = u'portuguese'
    GENDER = u'gender'
    POS = u'pos'

    def __init__(self, words_coll):
        self.words = words_coll

    def init_coll(self):
        pass

    def is_coll_clean(self):
        return self.words.count() == 0

    def clean(self):
        self.words.remove()

    def add_noun(self, user_id, polish, portuguese, gender):
        new_noun = {
            self.USER: user_id,
            self.POLISH: polish,
            self.PORTUGUESE: portuguese,
            self.GENDER: gender, 
            self.POS: NOUN,
        }

        self.words.insert(new_noun)
        
    def get_words(self, user_id, sort_key=None):
        user = self.get_user(username)
        cursor = self.words.find({self.USER: user_id})
        if sort_key:
            cursor = cursor.sort(sort_key)

        return list(cursor)


class DBException(Exception):
    pass
