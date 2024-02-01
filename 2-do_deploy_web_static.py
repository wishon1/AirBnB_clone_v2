#!/usr/bin/python3
""" fabfile that distribute an archive to web servers"""
import os
from datetime import datetime
from fabric.api import *


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

def do_deploy(archive_path):
    """ method that distributes an archive to my web servers"""
    if 0s.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        tmp_obj = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        folder_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, tmp_obj)
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf {} -c {}".format(tmp_obj, folder_path))
        run("rm {}".format(tmp_obj))
        run("mv -f {}web_static/* {}".format(tmp_obj, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        return True
    return False
