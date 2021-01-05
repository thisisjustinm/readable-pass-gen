# Python port of Niceware implemented with help of Hades

from wordlist import WORD_LIST
from hades import hades
from textwrap import wrap


def gen_pass_text(seed, length):
    word_list = ' '.join(WORD_LIST[i] for i in [int(i, 16) for i in wrap(hades(seed, length), 4)])
    return word_list


def text_to_pass(word_list):
    hex_password = ''.join(hex(WORD_LIST.index(i))[2:].zfill(4) for i in word_list.split())
    return hex_password


def pass_to_text(password):
    word_list = ' '.join(WORD_LIST[i] for i in [int(i, 16) for i in wrap(password, 4)])
    return word_list


print(gen_pass_text('Guido van Rossum', 3))  # cyclizing hotfoot explode monthly prorogue benthal
print(text_to_pass('cyclizing hotfoot explode monthly prorogue benthal')) #311a663c4a658a20ab541026
print(pass_to_text('311a663c4a658a20ab541026')) # cyclizing hotfoot explode monthly prorogue benthal
