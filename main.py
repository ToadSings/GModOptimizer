import os
import shutil
import json

def writeAutoExec():
    f = open('ressources/config.json')

    data = json.load(f)

    try:
        file = open(data['pathAutoExec'], "a")
        file.write("gmod_mcore_test 1\nmat_queue_mode -1\ncl_threaded_bone_setup 1\ncl_smooth 0\nmat_mipmaptextures 0\nr_decal_cullsize 1\nfog_enable 0\nmp_decals 3\n")
        file.close()
    except OSError as e:
        print(e)

    f.close()

def deleteCache():
    f = open('ressources/config.json')

    data = json.load(f)

    try:
        shutil.rmtree(data['pathLua'])
    except OSError as e:
        print(e)
    else:
        print("Le répertoire à bien été supprimé")

    for i in os.listdir(data['pathWorkshop']):
        filename, fileExtension = os.path.splitext(i)

        if (fileExtension == ".gma" or fileExtension == ".cache"):
            try:
                os.remove(os.path.join(data['PathWorkshop'], i))
            except OSError as e:
                print(e)

    f.close()