dropmanager
===========

This a very much a work in progress.

A Python script for managing Drops on Digital Ocean.

The main prompt:
Options:
1) List Active Droplets
2) List Available Sizes
3) List Available Images
4) List Available Regions
5) Create Drop
6) Destroy Drop
10) Create Downpour
11) Display Downpour
12) Destroy Downpour
q) Quit

Prereqs: pip, dop

Install/Configure/Run:

pip install dop

cd /<directory with dropmanager>

cp config-example.ini config.ini

vim config.ini

python dropmanager.py
