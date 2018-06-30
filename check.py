__author__ = 'vxst'
import archlinux
import debian
import ubuntu
import centos
import alert
import linuxmint
import epel
import postgresql
import openSUSE
import os

def check(tick):
    check_rank = tick % 8
    check_object = None
    check_dist = "Noop"

    if check_rank == 0:
        check_object = archlinux
        check_dist = "Arch Linux"
        check_name = "archlinux"
    elif check_rank == 1:
        check_object = debian
        check_dist = "Debian"
        check_name = "debian"
    elif check_rank == 2:
        check_object = centos
        check_dist = "CentOS"
        check_name = "centos"
    elif check_rank == 3:
        check_object = ubuntu
        check_dist = "Ubuntu"
        check_name = "ubuntu"
    elif check_rank == 4:
        check_object = linuxmint
        check_dist = "LinuxMint"
        check_name = "linuxmint"
    elif check_rank == 5:
        check_object = epel
        check_dist = "EPEL"
        check_name = "epel"
    elif check_rank == 6:
        check_object = postgresql
        check_dist = "PostgreSQL"
        check_name = "postgresql"
    elif check_rank == 7:
        check_object = openSUSE
        check_dist = "openSUSE"
        check_name = "opensuse"

    result, is_ok= check_object.check_it()
    if not is_ok:
        alert.alert(check_dist, result)

    with open(os.path.join("/srv/mirrors/status", check_name + "_status", w)) as output:
        output.write(result)
