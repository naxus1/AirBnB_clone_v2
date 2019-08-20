#!/usr/bin/python3
""" module that compress in tgz """
from fabric.api import local


def do_pack():
    """compress files """
    local("mkdir -p versions")
    file = local("tar -czvf \"versions/web_static_\
                 $(date '+%Y%m%d%H%M%S').tgz\" web_static")

    if (file.succeeded):
        return local("echo \"versions/web_static_\
                     $(date '+%Y%m%d%H%M%S').tgz\"")
    else:
        print("none")
        return None
