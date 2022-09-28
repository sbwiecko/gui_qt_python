# ! Please use the Pro Edtion of fbs, with the file downloaded after the payment
# pip install fbs_pro-1.1.4.tar.gz
# see also https://build-system.fman.io/manual/

# ! DOESN'T WORK IN A VIRTUAL ENVIRONMENT WITH PYTHON 3.9
# please use outside of the environment context

### get help

fbs --h


### start a project

fbs startproject

# enter the name of the app, author and/or leave default options
# ! fbs doesn't like some encoding such as the French accents, e.g., "Sébastien"...

# this creates a directory structure with a basic app in ./src
# src
# ├───build
# │   └───settings
# └───main
#     ├───icons
#     │   ├───base
#     │   ├───linux
#     │   └───mac
#     └───python


### run the app

fbs run


### modify the minimal app

# create a new directory in the /src/main/python called "package"
# and add all the classes for a customized app, e.g., "main_window.py"
# change the import in main.py


### create an exe
# go to the directory that contains /src

fbs freeze
# fbs freeze --debug

# it has created a "/target/app" folder with the exe


### create an installer
# needs NSIS http://nsis.sourceforge.net/Main_Page
# add to PATH, e.g., "C:\Program Files (x86)\NSIS"
# On Linux, the installer command requires that you have fpm https://github.com/jordansissel/fpm

fbs installer

# in case of issues during the process, e.g., encoding etc.
# run the installer in another prompt outside IDE
# it may be an issue in the "Installer.nsi" file easy to indentify
# for instance, we could solve the issue of the encoding in the Copyright name
# by changing the corresponding option in build/settings/base.json file.


### clean
# clean all files and directories created by fbs freeze

fbs clean
