dropmanager
===========

This a very much a work in progress.

A Python script for managing Drops on Digital Ocean.

The main prompt (a downpour is a set of vms, <name>000-<name>xyz:<br>
Options:<br>
1) List Active Droplets<br>
2) List Available Sizes<br>
3) List Available Images<br>
4) List Available Regions<br>
5) Create Drop<br>
6) Destroy Drop<br>
10) Create Downpour<br>
11) Display Downpour<br>
12) Destroy Downpour<br>
q) Quit<br>

Prereqs: pip, dop

Install/Configure/Run:

pip install dop

cd /<directory with dropmanager>

cp config-example.ini config.ini

vim config.ini

python dropmanager.py
