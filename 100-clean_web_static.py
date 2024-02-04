#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives

Usage:
    ./3-clean_old_versions.py [number]

Arguments:
    number (int): The number of the archives, including the most recent,
    to keep.
                  If number is 0 or 1, keep only the most recent version of
                  your archive.
                  If number is 2, keep the most recent, and second most recent
                  versions of your archive. etc.

Deletes all unnecessary archives (all archives minus the number to keep) in
the versions folder and /data/web_static/releases folder of both of your web
servers. All remote commands are executed on both of your web servers (using
the env.hosts variable in your script).

Example:
    ./3-clean_old_versions.py 2
"""
from fabric.api import *
import os

env.hosts = ['54.144.139.197', '34.203.29.50']


def do_clean(number=0):
    """
    Deletes out-of-date archives from the versions folder and
    /data/web_static/releases folder

    Args:
        number (int): The number of archives to keep.

    Returns:
        None
    """
    # If number is 0, keep only the most recent version
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))

    # Remove the old archives, leaving only the specified number
    for i in range(number):
        archives.pop()

    with lcd("versions"):
        # Delete the old archives
        [local("rm ./{}".format(a)) for a in archives]

    # Remote cleanup of old archives
    with cd("/data/web_static/releases"):

        # Get a list of all archives in the releases folder
        archives = run("ls -tr").split()

        # Filter only web_static_ archives
        archives = [a for a in archives if "web_static_" in a]

        # Remove the old archives, leaving on the specified number
        for i in range(number):
            archives.pop()

        # Delete the old archives
        [run("rm -rf ./{}".format(a)) for a in archives]
