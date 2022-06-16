#!/usr/bin/python3
# deletes out-of-date archives, using the function do_clean

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['34.139.37.125', '34.75.9.253']


def do_clean(number=0):
    """
    deletes out-of-date archives,
    """
    if int(number) == 0:
        num = 2
    else:
        num = int(number) + 1
    cmd = 'tail -n +{}| xargs rm -rf'.format(num)
    local('cd versions ; ls -t|{}'.format(cmd))
    dir = '/data/web_static/releases'
    run('cd {}; ls -t| grep web_static|{}'.format(dir, cmd))
