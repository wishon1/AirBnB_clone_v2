# AirBnB Clone - Deploy Static

## Intoduction
This project is the first deployment phase of the AirBnB clone, focusing on deploying static content using Fabric, Python, and Nginx. The project aims to set up web servers, compress content, and deploy archives seamlessly.

## Concepts
Key concepts covered in this project include:
- Continuous Integration and Continuous Deployment (CI/CD)
- AirBnB clone architecture
- Fabric for deployment automation
- Nginx configuration

## Background Context
The project builds on previous knowledge gained from the SysAdmin track, particularly project 0x0F. Load balancer. It involves deploying web\_static content using Fabric, a Python library for streamlining SSH usage in deployment or system administration tasks.

## Resources
- [How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
- [Fabric Documentation](https://docs.fabfile.org/en/2.6/)
- [CI/CD concept page](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)
- [Nginx configuration for beginners](https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms)
- [Difference between root and alias on NGINX](https://www.digitalocean.com/community/questions/nginx-alias-and-root-not-working)
- [Fabric for Python 3](https://pypi.org/project/Fabric3/)
  
## Learning Objectives
By the end of this project, participants should be able to:
- Explain Fabric and its usage
- Deploy code to servers easily using Fabric
- Understand the purpose of a tgz archive
- Execute Fabric commands locally and remotely
- Transfer files using Fabric
- Manage Nginx configuration effectively
- Differentiate between root and alias in Nginx configuration

## Requirements
### Python Scripts
- Editors: vi, vim, emacs
- Ubuntu 20.04 LTS with Python 3.4.0
- PEP 8 style (version 1.7.*)
- Fabric 3 version 1.14.post1
- Documentation for all functions
### Bash Scripts
- Editors: vi, vim, emacs
- Ubuntu 20.04 LTS
- Pass Shellcheck (version 0.3.3-1~ubuntu20.04.1)
- The first line should be `#!/usr/bin/env bash`
- Documentation in README.md
### Installation
```bash
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev libssl-dev build-essential python3.4-dev libpython3-dev
$ pip3 install pyparsing appdirs setuptools==40.1.0 cryptography==2.8 bcrypt==3.1.7 PyNaCl==1.3.0 Fabric3==1.14.post1
```

## Tasks
### Prepare your web servers
- Write a Bash script to set up web servers
- Install Nginx, create directories, fake HTML file, and symbolic links
- Update Nginx configuration
- Ensure recursive ownership of directories
### Compress before sending
- Write a Fabric script to generate a .tgz archive from web_static folder
- Archive name: `web_static_<year><month><day><hour><minute><second>.tgz`
- Return archive path if generated correctly
### Deploy archive!
- Write a Fabric script to distribute archive to web servers
- Upload, uncompress, and create symbolic links
- Ensure proper cleanup after deployment
### Full deployment
- Write a Fabric script to automate full deployment
- Call do_pack() and do_deploy() functions
- Deploy on both web servers
