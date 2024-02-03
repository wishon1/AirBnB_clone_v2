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
    if os.path.exists(archive_path):
        # Extract the file name from the path
        file_name = archive_path[9:]

        # Define the path where the newest version will be stored
        newest_version_path = "/data/web_static/releases/" + file_name[:-4]

        # Update the path of the archive file
        archive_file_path = "/tmp/" + file_name

        # Transfer the archive file to the server's temporary directory
        put(archive_path, "/tmp/")

        # Create the directory for the newest version
        run("sudo mkdir -p {}".format(newest_version_path))

        # Extract the archive into the newest version directory
        run("sudo tar -xzf {} -C {}/"
            .format(archive_file_path, newest_version_path))

        # Remove the archive file from the server
        run("sudo rm {}".format(archive_file_path))

        # Move the contents of web_static to the newest version directory
        run("sudo mv {}/web_static/* {}"
            .format(newest_version_path, newest_version_path))

        # Remove the web_static directory from the newest version directory
        run("sudo rm -rf {}/web_static"
            .format(newest_version_path))

        # Remove the current symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link to the newest version
        run("sudo ln -s {} /data/web_static/current"
            .format(newest_version_path))

        print("New version deployed!")
        return True

    return False
