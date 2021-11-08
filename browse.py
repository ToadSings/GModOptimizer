from PyQt5 import QtWidgets
import json

def writePathConfig(path):
    paths = {
        "pathLua": f"{path}/garrysmod/cache/lua",
        "pathWorkshop": f"{path}/garrysmod/cache/workshop",
        "pathAutoExec": f"{path}/garrysmod/cfg/autoexec.cfg"
    }

    with open("ressources/config.json", "w") as file:
        json.dump(paths, file)

def browseInFolder():
    browsedir = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder')
    writePathConfig(browsedir)