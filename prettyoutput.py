#!/usr/bin/env python3.6
import sys
from functools import partial
from time import gmtime, strftime
"""
Pretty Output
Aareon Sullivan - 2017
"""


color = {'red': '\033[0;31;40m',
         'yellow': '\033[1;33;40m',
         'green': '\033[1;32;40m',
         'cyan': '\033[1;36;40m',
         'magenta': '\033[1;35;40m',
         'black': '\033[1;30;40m',
         'reset': '\033[1;37;40m'}

reset = color.get('reset')


def status(**kwargs):
    for key, value in kwargs.items():
        if 'string' in key:
            string = value
        elif 'color_code' in key:
            color_code = value
        elif 'stat_msg' in key:
            stat_msg = value
        elif 'prn_out' in key:
            prn_out = value
        elif 'time' in key:
            time = value
        elif 'space' in key:
            space = value
    message = _format(color_code, stat_msg, string)
    if time:
        message += '('+strftime("%Y-%m-%d %H:%M:%S", gmtime())+')'
    if prn_out:
        print(message)
    return message


def _format(color_code, stat_msg, string):
    color_code = color.get(color_code)
    if not color_code:
        color_code = color.get('yellow')
        error_msg = ('Incorrect color option! A list of options are as follows: '
          + ', '.join(value + key + reset for key, value in color.items()))
        print(color_code + '[PRTTYERR]'.ljust(10) + '| ' + reset + error_msg)
    return color_code + stat_msg.ljust(10) + '| ' + reset + string

error = partial(status, string='An error has ocurred!', color_code='red', stat_msg='[ERROR]', prn_out=True, time=False, space=False)
warning = partial(status, string='Something is not right', color_code='yellow', stat_msg='[WARNING]', prn_out=True, time=False, space=False)
success = partial(status, string='Great success!', color_code='green', stat_msg='[SUCCESS]', prn_out=True, time=False, space=False)
info = partial(status, string='Information:', color_code='cyan', stat_msg='[INFO]', prn_out=True, time=False, space=False)
custom = partial(status, string='Custom text', color_code='magenta', stat_msg='[CUSTOM]', prn_out=True, time=False, space=False)


def color_this(string, color_code):
    return color.get(color_code)+string+reset


def extend(tup, color_code='yellow', extens='>>>', prn_out=True):
    """Takes a tuple, returns a sub-message"""
    string = ''
    for item in tup:
        string += ' '+color_this(extens.ljust(14), color_code)+item+'\n'
    string = string[:-1]
    if prn_out:
        print(string)


def version(color_code='magenta', stat_msg='[PRTTYOUT]', string='Pretty Output version info:', prn_out: bool=True):
    version = {'python': str(sys.version_info[0]) + '.' + str(sys.version_info[1]),
               'output': '2.8.4'}

    pyver = color_this(version.get('python'), 'magenta')
    outver = color_this(version.get('output'), 'magenta')

    status(string, color_code, stat_msg, prn_out)
    extend(('Python Version - ' + pyver, 'PreOut Version - ' + outver))

