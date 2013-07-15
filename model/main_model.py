#!/usr/bin/python
# -*- coding: utf-8 -*-

import consts
import gui.consts as gui_consts

from db import DB
from kmapper import map_pl_to_br

from PyQt4.QtCore import Qt, QAbstractTableModel, QString, QVariant


ALL_POS = ['NOUN', 'VERB', 'ADJECTIVE', 'PRONOUN', ]

def get_pos_mapping(mod_from, mod_to):
    return {mod_from.__dict__[pos]: mod_to.__dict__[pos] for pos in ALL_POS}

pos_gui_model_dict = get_pos_mapping(gui_consts, consts)
pos_model_gui_dict = get_pos_mapping(consts, gui_consts)


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


def throw_on_empty(*check_args):
    def ext_wrapper(fun):
        def wrapper(*args, **kwargs):
            fun_args = fun.func_code.co_varnames
            for arg_name in check_args:
                if arg_name not in fun_args:
                    raise ValueError('Argument %s is not %s()\'s argument' % (arg_name, fun.func_code.co_name))
                index = fun_args.index(arg_name)
                if index < len(args):
                    value = args[index]
                elif arg_name in kwargs:
                    value = kwargs[arg_name]
                else:
                    import inspect
                    arg_spec = inspect.get_argspec(fun)
                    passed_args_count = len(args) + len(kwargs)
                    value = arg_spec.defaults[index - passed_args_count + 1]

                if not value:
                    raise ModelException(u'%s empty' % arg_name)

            return fun(*args, **kwargs)

        return wrapper

    return ext_wrapper


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
    @throw_on_empty('polish', 'portuguese')
    def add_noun(self, polish, portuguese, gender):
        self.db.add_noun(self.current_user_name, polish, portuguese, gender)

    @to_model_format
    @assert_user
    @throw_on_empty('polish', 'portuguese')
    def add_verb(self, polish, portuguese):
        self.db.add_verb(self.current_user_name, polish, portuguese)

    @to_model_format
    @assert_user
    @throw_on_empty('polish', 'portuguese')
    def add_adjective(self, polish, portuguese):
        self.db.add_adjective(self.current_user_name, polish, portuguese)

    @to_model_format
    @assert_user
    @throw_on_empty('polish', 'portuguese')
    def add_pronoun(self, polish, portuguese):
        self.db.add_pronoun(self.current_user_name, polish, portuguese)


    @to_model_format
    @assert_user
    @throw_on_empty('test_type', 'pos', 'count')
    def generate_test_words(self, test_type, days, pos, count):
        self.test_words = self.db.generate_test_words(self.current_user_name, days, pos, count)
        self.test_type = test_type

    @assert_user
    def get_next_test_word(self):
        key = 'polish' if self.test_type == gui_consts.PL_PT_TEST else 'portuguese'
        return next(self.test_words)[key]


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
