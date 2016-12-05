#!/usr/bin/python
import os
os.system("yum remove deluge -y")
os.system("rm -rf /usr/bin/deluge")
os.system("rm -rf /usr/lib/python2.X/site-packages/deluge*")
os.system("rm -rf /usr/share/deluge/*")
os.system("rm -rf /usr/share/applications/deluge.desktop")
os.system("rm -rf /usr/share/pixmaps/deluge.xpm")
print "\n"
print "deluge was completely removed =)"
