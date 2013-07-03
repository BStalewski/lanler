#!/usr/bin/python
# -*- coding: utf-8 -*-


dead_keys = {u'~', u'^', u'´', u'`', u'¨', }

def map_pl_to_br(msg):
    msg_br_layout = LayoutMapper().change_layout(msg)
    return DeadKeyEater().process_msg(msg_br_layout)


class LayoutMapper:
    mapped_keys = {u';', u':', u"'", u'"', u'{', u'[', u'^', }

    pl_pt_kbmap = {
        u';': u'ç',
        u':': u'Ç',
        u"'": u'~',
        u'"': u'^',
        u'{': u'´',
        u'[': u'`',
        u'^': u'¨',
    }

    def change_layout(self, msg):
        mapped_pt_msg_array = []
        for key in msg:
            try:
                mapped_pt_msg_array.append(self.pl_pt_kbmap[key])
            except KeyError:
                mapped_pt_msg_array.append(key)

        return u''.join(mapped_pt_msg_array)


class DeadKeyEater:
    tilde_map = {
        u'a': u'ã',
        u'A': u'Ã',
        u'o': u'õ',
        u'O': u'Õ',
    }
    circumflex_map = {
        u'a': u'â',
        u'A': u'Â',
        u'e': u'ê',
        u'E': u'Ê',
        u'o': u'ô',
        u'O': u'Ô',
    }
    acute_map = {
        u'a': u'á',
        u'A': u'Á',
        u'e': u'é',
        u'E': u'É',
        u'i': u'í',
        u'I': u'Í',
        u'o': u'ó',
        u'O': u'Ó',
        u'u': u'ú',
        u'U': u'Ú',
    }
    grave_map = {
        u'a': u'à',
        u'A': u'À',
    }
    diaeresis_map = {
        u'u': u'ü',
        u'U': u'Ü',
    }
    keys_maps = {
        u'~': tilde_map,
        u'^': circumflex_map,
        u'´': acute_map,
        u'`': grave_map,
        u'¨': diaeresis_map,
    }

    def process_msg(self, msg):
        processed_msg_array = []
        recently_eaten = False
        for i in range(len(msg)):
            if recently_eaten:
                recently_eaten = False
                continue

            fst = msg[i]
            try:
                sec = msg[i + 1]
                processed_key = self.eat(fst, sec)
            except (IndexError, KMapperException, ):
                processed_msg_array.append(fst)
            else:
                processed_msg_array.append(processed_key)
                recently_eaten = True

        processed_msg = ''.join(processed_msg_array)
        return processed_msg

    def can_eat(self, fst, sec):
        if fst not in self.keys_maps.keys():
            return False

        available_eaters = self.keys_maps[fst].keys()
        return sec.lower() in available_eaters

    def eat(self, fst, sec):
        try:
            key_map = self.keys_maps[fst]
        except KeyError:
            msg = 'Not dead key: %s' % (fst.encode('utf-8'))
            raise KMapperException(msg)

        try:
            key = key_map[sec]
        except KeyError:
            msg = 'Unable to eat %s with %s' % (fst.encode('utf-8'), sec.encode('utf-8'))
            raise KMapperException(msg)

        return key

    
class KMapperException(Exception):
    pass

