#!/usr/bin/python
# -*- coding: utf-8 -*-

class User:
    def __init__(self, uid, name, vocabulary=None):
        self.uid = uid
        self.name = name
        self.vocabulary = vocabulary or {}

    def __str__(self):
        return 'User({0}, {1})'.format(self.name.encode('utf-8'), self.uid)

    def __unicode__(self):
        return self.__str__().decode('utf-8')
