#!/bin/bash

pyinstaller -F -w -p "$(pwd)/carrater" -n "car-rater" -i icon.ico carrater/__main__.py
