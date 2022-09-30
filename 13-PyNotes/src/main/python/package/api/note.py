### API ###
import os
import json
from uuid import uuid4
from glob import glob

# the line below will be called from the file main.py
from package.api.constants import NOTES_DIR


def get_notes():
    """
    Scans the NOTE_DIR folder for .json files and populates a list of notes.
    """
    notes = []
    fichiers = glob(os.path.join(NOTES_DIR, "*.json"))
    for fichier in fichiers:
        with open(fichier, "r") as f:
            note_data = json.load(f)
            # retrieve the UUID from the filename, removing the DIR and extension
            note_uuid = os.path.splitext(os.path.basename(fichier))[0]
            note_title = note_data.get("title") # get in case data not exist -> None
            note_content = note_data.get("content")
            note = Note(uuid=note_uuid, title=note_title, content=note_content)
            notes.append(note)

    return notes


class Note:
    def __init__(self, title="", content="", uuid=None):
        if uuid: # if UUID exist, i.e., we load a file
            self.uuid = uuid
        else:
            self.uuid = str(uuid4()) # create UUID if not exists

        self.title = title
        self.content = content

    def __repr__(self):
        """
        Representation of the object, display more technical details using repr().
        """
        return f"{self.title} ({self.uuid})"

    def __str__(self):
        """
        Another display of the object, using print().
        """
        return self.title

    # set a getter and a setter for the content of a note
    # changing the attribute 'content' into a private one '_content'
    # to avoid recursive calls, as the method is called 'content' itself
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self._content = value
        else:
            raise TypeError("Valeur invalide (besoin d'une chaîne de caractères).")

    def delete(self):
        os.remove(self.path)
        if os.path.exists(self.path):
            return False
        return True

    @property
    def path(self):
        """returns the path as a class attribute"""
        return os.path.join(NOTES_DIR, self.uuid + ".json")

    def save(self):
        if not os.path.exists(NOTES_DIR):
            os.makedirs(NOTES_DIR)

        data = {"title": self.title, "content": self.content}
        with open(self.path, "w") as f: # path is a property
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    notes = get_notes()
    print(notes)
