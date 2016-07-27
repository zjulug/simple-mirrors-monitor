import archlinux
import debian
import centos
import linuxmint
import ubuntu
import epel
import postgresql
import openSUSE

info, status = archlinux.check_it()
print("Arch Linux Test result: {}, Is_OK: {}".format(info, status))

info, status = debian.check_it()
print("Debian Test result: {}, Is_OK: {}".format(info, status))

info, status = centos.check_it()
print("CentOS Test result: {}, Is_OK: {}".format(info, status))

info, status = linuxmint.check_it()
print("Linux Mint Test result: {}, Is_OK: {}".format(info, status))

info, status = ubuntu.check_it()
print("Ubuntu Test result: {}, Is_OK: {}".format(info, status))

info, status = epel.check_it()
print("EPEL Test result: {}, Is_OK: {}".format(info, status))

info, status = postgresql.check_it()
print("PostgreSQL Test result: {}, Is_OK: {}".format(info, status))

info, status = openSUSE.check_it()
print("openSUSE Test result: {}, Is_OK: {}".format(info, status))
