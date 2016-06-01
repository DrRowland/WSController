#!/bin/bash -e

cd ~pi
sleep 60
source ENV/bin/activate
python server.py &
python wscontroller.py &



