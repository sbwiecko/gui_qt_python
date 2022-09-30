import os
from pathlib import Path

# the idea is to create a directory in the user folder
# so that we avoid access and administration issues
NOTES_DIR = os.path.join(Path.home(), ".notes") # hidden directory