#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import pytz
import random
from pymongo import MongoClient

from consts import *
from commons import *
from user import User


class DB:
    instance = None

    def __init__(self, clean=False):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['lanler']
        self.users = UsersCollection(self.db['users'])
        self.words = WordsCollection(self.db['words'])

        if clean:
            self.clean()

        if self.is_db_clean():
            print 'INIT DB'
            self.init_db()

    def clean(self):
        self.users.clean()
        self.words.clean()

    def close(self):
        self.client.close()

    def init_db(self):
        self.users.init_coll()
        self.words.init_coll()

    def is_db_clean(self):
        return self.users.is_coll_clean() and self.words.is_coll_clean()

    def create_user(self, name, vocabulary_import_users):
        self.users.create_user(name, vocabulary_import_users)

    def get_user(self, username):
        return self.users.get_user(username)

    def get_users_names(self):
        return self.users.get_users_names()

    def add_noun(self, username, polish, portuguese, gender):
        user = self.get_user(username)
        self.words.add_noun(user['_id'], polish, portuguese, gender)

    def add_verb(self, username, polish, portuguese):
        user = self.get_user(username)
        self.words.add_pos(user['_id'], polish, portuguese, VERB)

    def add_adjective(self, username, polish, portuguese):
        user = self.get_user(username)
        self.words.add_pos(user['_id'], polish, portuguese, ADJECTIVE)

    def add_pronoun(self, username, polish, portuguese):
        user = self.get_user(username)
        self.words.add_pos(user['_id'], polish, portuguese, PRONOUN)

    def get_words(self, username, sort_key=None, **query_conds):
        user = self.get_user(username)
        return self.words.get_words(user['_id'], sort_key, **query_conds)

    def generate_test_words(self, username, days, pos, count):
        user = self.get_user(username)
        user_words = self.get_words(username, pos=pos, days=days)
        words_count = len(user_words)
        if not words_count:
            raise DBException('Empty words list')

        for _ in range(count):
            yield user_words[random.randint(0, words_count - 1)]

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
    LAST_MODIFICATION = u'last_modification'

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
            self.LAST_MODIFICATION: get_current_utcdatetime(),
        }

        self.words.insert(new_noun)

    def add_pos(self, user_id, polish, portuguese, pos):
        new_pos = {
            self.USER: user_id,
            self.POLISH: polish,
            self.PORTUGUESE: portuguese,
            self.POS: pos,
            self.LAST_MODIFICATION: get_current_utcdatetime(),
        }

        self.words.insert(new_pos)

    def add_verb(self, user_id, polish, portuguese):
        self.add_pos(user_id, polish, portuguese, VERB)

    def add_adjective(self, user_id, polish, portuguese):
        self.add_pos(user_id, polish, portuguese, ADJECTIVE)

    def add_pronoun(self, user_id, polish, portuguese):
        self.add_pos(user_id, polish, portuguese, PRONOUN)

    def get_words(self, user_id, sort_key=None, **query_conds):
        query_dict = {self.USER: user_id}
        pos = query_conds.get('pos', None)
        days = query_conds.get('days', None)

        if pos:
            query_dict.update({self.POS: {'$in': pos }})
        if days:
            start_datetime = get_past_utcdatetime(days=days)
            query_dict.update({self.LAST_MODIFICATION: {'$gt': start_datetime}})

        cursor = self.words.find(query_dict)
        if sort_key:
            cursor = cursor.sort(sort_key)

        return list(cursor)


class DBException(Exception):
    pass
