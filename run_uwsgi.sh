#!/bin/sh
sudo uwsgi -M -p 8 -x conf/vmmanager.xml --plugin python3 --pidfile uwsgi.pid
