# simply call the executable after installation via pip and choose the main entry script to convert
#../.env/Scripts/auto-py-to-exe.exe


# follow the instructions, see also https://github.com/brentvollebregt/auto-py-to-exe
# choose "console based" also for debugging
# don't forget to include all associated files and folders

# !!! for unknown reasons, the auto-py-to-exe doesn't seem to work properly
# there are apparently some missing Lib files when executed in a virtual environement,
# but outside this context, e.g., using Python 3.10, the output directory will contain a working EXE

Invoke-Expression auto-py-to-exe
