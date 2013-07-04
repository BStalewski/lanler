#!/usr/bin/python
# -*- coding: utf-8 -*-

from db import DB
from db import NOUN, VERB, ADJECTIVE, PRONOUN

from kmapper import map_pl_to_br

from PyQt4.QtCore import Qt, QAbstractTableModel, QString, QVariant


def assert_user(fun):
    def wrapper(self, *args, **kwargs):
        if not self.current_user_name:
            raise ModelException(u'User is none')

        return fun(self, *args, **kwargs)

    return wrapper

def to_model_format(fun):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            new_arg = arg.__str__() if isinstance(arg, QString) else arg
            new_args.append(new_arg)

        new_kwargs = {}
        for key, value in kwargs.items():
            new_key = key.__str__() if isinstance(key, QString) else key
            new_value = value.__str__() if isinstance(value, QString) else value
            new_kwargs[new_key] = new_value

        return fun(*new_args, **new_kwargs)

    return wrapper


def has_preposition(pos):
    return pos in {NOUN}


def add_preposition(word, gender):
    return u'o ' + word if gender == u'M' else u'a ' + word


@to_model_format
def pl_to_br_layout(msg):
    return QString(map_pl_to_br(msg))


class Model:
    def __init__(self):
        self.db = DB.get_instance(False)
        self.current_user_name = None

    @to_model_format
    def set_current_user(self, name):
        if name not in self.get_users_names():
            raise ModelException()

        self.current_user_name = name

    @assert_user
    def get_current_user(self):
        return QString(self.current_user_name)

    def get_users_names(self):
        return self.db.get_users_names()

    @to_model_format
    def create_user(self, name, import_user_names):
        self.db.create_user(name, import_user_names)

    @to_model_format
    def is_user_name_unique(self, user_name):
        return user_name not in self.get_users_names()

    @to_model_format
    @assert_user
    def add_noun(self, polish, portuguese, gender):
        if not polish:
            raise ModelException(u'Polish empty')

        if not portuguese:
            raise ModelException(u'Portuguese empty')

        self.db.add_noun(self.current_user_name, polish, portuguese, gender)



class DictionaryModel(QAbstractTableModel):
    POLISH_KEY = u'polish'
    PORTUGUESE_KEY = u'portuguese'
    POLISH_NAME = u'polski'
    PORTUGUESE_NAME = u'portugalski'

    @to_model_format
    def __init__(self, user, parent):
        QAbstractTableModel.__init__(self, parent)
        self.current_user_name = user
        self.db = DB.get_instance()
        self.words = self.get_words()
        self.columns_keys = self.get_columns_keys()
        self.columns_names = self.get_columns_names()
        self.rows_count = len(self.words)
        self.columns_count = len(self.columns_names)
        self.portuguese_index = self.get_portuguese_index()

    def get_portuguese_index(self):
        return self.columns_keys.index(DictionaryModel.PORTUGUESE_KEY)

    def get_columns_keys(self):
        raise ModelException()

    def get_columns_names(self):
        raise ModelException()

    def get_words(self):
        return self.db.get_words(self.current_user_name, self.sort_key)

    def rowCount(self, parent):
        return self.rows_count

    def columnCount(self, parent):
        return self.columns_count

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()

        word = self.words[index.row()]
        key = self.columns_keys[index.column()]
        if has_preposition(word[u'pos']) and index.column() == self.portuguese_index:
            return QVariant(add_preposition(word[key], word[u'gender']))
        else:
            return QVariant(word[key])

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return QVariant(self.columns_names[section])
        else:
            return QAbstractTableModel.headerData(self, section, orientation, role)


class PtPlDictionaryModel(DictionaryModel):
    sort_key = DictionaryModel.PORTUGUESE_KEY

    def __init__(self, user, parent):
        DictionaryModel.__init__(self, user, parent)

    def get_columns_keys(self):
        return [self.PORTUGUESE_KEY, self.POLISH_KEY]

    def get_columns_names(self):
        return [self.PORTUGUESE_NAME, self.POLISH_NAME]


class PlPtDictionaryModel(DictionaryModel):
    sort_key = DictionaryModel.POLISH_KEY

    def __init__(self, user, parent):
        DictionaryModel.__init__(self, user, parent)

    def get_columns_keys(self):
        return [self.POLISH_KEY, self.PORTUGUESE_KEY]

    def get_columns_names(self):
        return [self.POLISH_NAME, self.PORTUGUESE_NAME]


class ModelException(Exception):
    pass

