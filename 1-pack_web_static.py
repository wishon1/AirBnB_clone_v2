#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder"""
from datetime import datetime
from fabric.api import local


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
