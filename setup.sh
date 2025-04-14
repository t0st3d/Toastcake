#!/bin/bash
pkg update -y && pkg install -y python git clang cmake
pip install -r requirements.txt