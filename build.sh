#!/bin/bash

pyinstaller init.py -F -n "Flappy Bird" --add-data "images:images" --add-data "sounds:sounds" --add-data "/home/atom/.local/lib/python3.9/site-packages/pygame_gui/data:pygame_gui/data"
