#!/bin/bash -e

cd ~pi
source ENV/bin/activate
python server.py &
python wscontroller.py &



