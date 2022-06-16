#!/usr/bin/python3
# deletes out-of-date archives, using the function do_clean

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['3.233.221.194', '3.239.85.196']


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
