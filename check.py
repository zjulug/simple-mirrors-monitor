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

def check(tick):
    check_rank = tick % 8
    check_object = None
    check_dist = "Noop"
    # Archlinux
    if check_rank == 0:
        check_object = archlinux
        check_dist = "Arch Linux"
    # Debian
    elif check_rank == 1:
        check_object = debian
        check_dist = "Debian"
    # CentOS
    elif check_rank == 2:
        check_object = centos
        check_dist = "CentOS"
    # Ubuntu
    elif check_rank == 3:
        check_object = ubuntu
        check_dist = "Ubuntu"
    # LinuxMint
    elif check_rank == 4:
        check_object = linuxmint
        check_dist = "LinuxMint"
    # EPEL
    elif check_rank == 5:
        check_object = epel
        check_dist = "EPEL"
    #PostgreSQL
    elif check_rank == 6:
        check_object = postgresql
        check_dist = "PostgreSQL"
    #PostgreSQL
    elif check_rank == 7:
        check_object = openSUSE
        check_dist = "openSUSE"

    result, is_ok= check_object.check_it()
    if not is_ok:
        alert.alert(check_dist, result)
