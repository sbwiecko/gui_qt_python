# without knowing any option, we can run a first pass of pyinstaller

pyinstaller.exe .\calculator.py

# it will generate a build and dist directories, but also a calculator.spec file
# in the current directory that can be modified to add additional options, e.g.,
# the datas list that will contain tuple of arguments such as 
# ('/home/cine-club/data', './data')
# with the original and output locations for attached folders,
# or the option "console=False,"

# ! Here again, the virtual environment context doesn't allow a smooth
# conversion into an EXE, please use pyinstaller out of this context.