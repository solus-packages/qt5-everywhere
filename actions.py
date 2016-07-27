#!/usr/bin/python

import os
from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    del os.environ["LD_AS_NEEDED"]

    cxxflags = get.CXXFLAGS()
    # Temporary, due to GCC 6. Fixed in Qt 5.7, which will come after we
    # have finished GNOME 3.20 in Solus
    cxxflags += " -fno-delete-null-pointer-checks"
    shelltools.export("CXXFLAGS", cxxflags)

    # NOTE: —no-warnings-are-errors  is due to ld.gold warnings:
    # sqlite3 hidden symbols
    autotools.rawConfigure ("-opensource \
                             -eglfs \
                             -opengl es2 \
                             -xcb \
                             -no-pch \
                             -dbus-linked \
                             -icu \
                             -cups \
                             -nis \
                             -widgets \
                             -gui \
                             -qt-xcb \
                             -openssl-linked \
                             -system-libjpeg \
                             -system-libpng \
                             -system-zlib \
                             -largefile \
                             -c++11 \
                             -shared \
                             -no-static \
                             -confirm-license \
                             -release \
                             -prefix /usr \
                             -archdatadir /usr/lib/qt5 \
                             -datadir /usr/share/qt5 \
                             -docdir /usr/share/doc/qt5 \
                             -sysconfdir /etc/xdg \
                             -nomake tests \
                             -xkb-config-root /usr/share/X11/xkb \
                             -no-warnings-are-errors \
                             -no-use-gold-linker \
                             -skip qtwebengine \
                             -dbus-linked \
                             -openssl-linked  \
                             -examplesdir /usr/lib/qt5/examples")


def build():
    autotools.make ()

def install():
    autotools.rawInstall ("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.remove("/usr/lib/*.prl")
