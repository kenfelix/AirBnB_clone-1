#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static
# of airbnb clone repo
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Creates .tgz using local fabric command
    """
    if local('mkdir -p versions').failed:
        return None
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_{}.tgz'.format(timestamp)
    if local('tar -cvzf {} web_static'.format(path)).failed:
        return None
    return path
