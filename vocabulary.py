#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import pytz

class Vocabulary:
    def __init__(self, data=None):
        self.data = data or {}


class Word:
    def __init__(self, translations):
        self.translations = translations
        self.set_current_time()

    def update(self, translations):
        updated = False
        for translation in translations:
            if translation not in self.translations:
                self.translations.append(translations)
                updated = True

        if updated:
            self.set_current_time()

    def set_current_time():
        self.date = datetime.datetime.utcnow().replace(tzninfo=pytz.utc)

class Translation:
    def __init__(self, trans_word, pos):
        self.trans_word = trans_word
        self.pos = pos
        self.

    def __eq__(self, translation):
        return self.trans_word == translation.trans_word and self.pos == translation.pos

