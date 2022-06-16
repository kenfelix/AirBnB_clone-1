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


def delpoy():
    """
    Calls the above functions
    to create an archive and
    deploy it on the servers
    """
    path_to_archive = do_pack()
    if not path_to_archive:
        return False
    return do_deploy(path_to_archive)
