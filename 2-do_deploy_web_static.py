#!/usr/bin/python3
# distributes an archive to your web servers, using the function do_deploy
from fabric.api import *
import os

env.hosts = [
        'ubuntu@3.239.85.196',
        'ubuntu@3.233.221.194'
]

env.user = "ubuntu"
env.key_filename = "~/school"


def do_deploy(archive_path):
    """
    distributes an archive to servers
    """
    if not archive_path:
        return False

    if os.path.isfile(archive_path) is False:
        return False

    path_ext = archive_path.split("/")[-1]
    upload = put(archive_path, '/tmp/{}'.format(path_ext))
    if upload.failed:
        return False

    path_no_ext = path_ext.split('.')[0]
    if run("mkdir -p /data/web_static/releases/{}/".
            format(path_no_ext)).failed:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(path_ext, path_no_ext)).failed:
        return False

    if run("rm -r /tmp/{}".format(path_ext)).failed:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(path_no_ext, path_no_ext)).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(path_no_ext)).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(path_no_ext)).failed:
        return False

    return True
