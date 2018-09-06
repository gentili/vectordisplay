#!/bin/bash

# vim /etc/tmux.conf
#   new-session -s vectordisplay /home/pi/git/vectordisplay/vectordisplay.sh
#
# sudo systemctl edit getty@tty1.service
# [Service]
# ExecStart=
# ExecStart=-/usr/bin/tmux attach -t vectordisplay
# StandardInput=tty
# StandardOutput=tty
# User=pi
# Group=pi
# sudo systemctl restart getty@tty1.service

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

figlet Booting
while true; do
    echo -n "."
    sleep 1
done &
PID=$!
disown
source /usr/local/bin/virtualenvwrapper.sh
workon vectordisplay
kill $PID
figlet Initializing

while true; do
    ./vectordisplay.py
    sleep 1
done
