#!/usr/bin/python3
"""Fabric script to create and distribute an archive to web servers"""
import os
from fabric.api import env, local, put, run
from datetime import datetime


# Set the user and host IP addresses for web-01 and web-02
env.user = "ubuntu"
env.hosts = ['54.144.139.197', '34.203.29.50']


def do_pack():
    """Create a .tgz archive of the web_static directory"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(timestamp)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(file_path))
    if result.failed:
        return None
    return file_path


def do_deploy(archive_path):
    """Distribute the archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    file_no_ext = file_name.split('.')[0]
    remote_path = "/data/web_static/releases/{}/".format(file_no_ext)

    try:
        # Transfer the archive to the server
        put(archive_path, '/tmp/')

        # Create directory for new version
        run('mkdir -p {}'.format(remote_path))

        # Extract archive into new directory
        run('tar -xzf /tmp/{} -C {}'.format(file_name, remote_path))

        # Delete temporary archive file
        run('rm /tmp/{}'.format(file_name))

        # Move contents to proper location
        run('mv {}web_static/* {}'.format(remote_path, remote_path))

        # Remove old symbolic link
        run('rm -rf /data/web_static/current')

        # Create new symbolic link
        run('ln -s {} /data/web_static/current'.format(remote_path))
        print("New version deployed!")
        return True

    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to web servers.

    Usage:
    fab -f <script_file> deploy -i <SSH_private_key> -u <username>

    Arguments:
    <script_file>: Path to the Fabric script file.
    <SSH_private_key>: Path to the SSH private key for server access.
    <username>: Username for server access.

    Example:
    fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu

    This function performs the following steps:
    1. Calls the do_pack() function and stores the path of the created archive.
    2. Returns False if no archive has been created.
    3. Calls the do_deploy(archive_path) function using the new path
    of the archive.
    4. Returns the return value of do_deploy.
    All remote commands are executed on both web servers specified in
    env.hosts.

    Note: Make sure to replace <script_file>, <SSH_private_key>, and <username>
    with appropriate values.

    """
    # Call do_pack() to create the archive
    archive_path = do_pack()

    # Return False if no archive is created
    if archive_path is None:
        return False
    return do_deploy(archive_path)
