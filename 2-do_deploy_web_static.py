#!/usr/bin/python3
""" fabfile that distribute an archive to web servers"""
import os
from datetime import datetime
from fabric.api import *


# host IP addresses for web-01 && web-02
env.hosts = ['54.144.139.197', '34.203.29.50']
env.user = "ubuntu"


def do_pack():
    """ create an a .tgz achive"""
    # get the current date and time
    cur_date_time = datetime.now().strftime("%Y%m%d%H%M%S")

    # path to were the archive will be saved
    archive_path = "versions/web_static_{}.tgz".format(cur_date_time)

    # create directory if it doesn't exist using fabric
    local("mkdir -p versions")

    # create the archieve using tar
    tgz_archive = local("tar -cvzf {} web_static".format(archive_path))

    # check if the archive was created succesfully using return_code()
    if tgz_archive.return_code != 0:
        return None
    else:
        return archive_path


def do_deploy(archive_path):
    """Deploy the archive to web servers."""
    # Check if the archive exists
    if os.path.exists(archive_path):
        # Extract archive and prepare folder paths
        archive = archive_path.split('/')[1]
        tmp_obj = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        folder_path = "/data/web_static/releases/{}/".format(folder)

        # Upload the archive to the server
        put(archive_path, tmp_obj)

        # Create directory to extract archive contents
        run("mkdir -p {}".format(folder_path))

        # Extract archive contents to folder path
        run("tar -xzf {} -C {}".format(tmp_obj, folder_path))

        # Remove the archive from tmp directory
        run("rm {}".format(tmp_obj))

        # Move contents of extracted folder to folder path
        run("mv -f {}* {}".format(folder_path, folder_path))

        # Remove web_static directory from folder path
        run("rm -rf {}web_static".format(folder_path))

        # Remove current symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link to current version
        run("ln -s {} /data/web_static/current".format(folder_path))

        return True  # Deployment successful
    return False  # Archive not found
