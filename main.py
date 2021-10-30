import os
import shutil

pathLuaCache = r'C:/Program Files (x86)/Steam/steamapps/common/GarrysMod/garrysmod/cache/lua'
pathWorkshopCache = r'C:/Program Files (x86)/Steam/steamapps/common/GarrysMod/garrysmod/cache/workshop'

print("""  _                  _     _                 
 | |                | |   (_)                
 | |_ ___   __ _  __| |___ _ _ __   __ _ ___ 
 | __/ _ \ / _` |/ _` / __| | '_ \ / _` / __|
 | || (_) | (_| | (_| \__ \ | | | | (_| \__ \\
  \__\___/ \__,_|\__,_|___/_|_| |_|\__, |___/`
                                    __/ |    
                                   |___/     """)

def main():
    answer = input("Taper 1 si vous voulez supprimer les fichiers caches\nTaper 2 si vous voulez modifier le fichier autoexec.cfg\nAppuyer sur ENTREE si vous voulez arreter le programme : ")
    
    if(answer == "1"):
        deleteCache()
    elif(answer == "2"):
        writeAutoExec()
        
def deleteCache():
        try:
            shutil.rmtree(pathLuaCache)
        except OSError as e:
            print(e)
        else:
            print("Le répertoire à bien été supprimé")

        for i in os.listdir(pathWorkshopCache):
            filename, fileExtension = os.path.splitext(i)

            if (fileExtension == ".gma" or fileExtension == ".cache"):
                try:
                    os.remove(os.path.join(pathWorkshopCache, i))
                except OSError as e:
                    print(e)
                else:
                    print("Fichier cache supprimé !")

        answer1 = input("\n\nTaper 1 si vous voulez modifier le fichier autoexec.cfg\nAppuyer sur ENTREE si vous voulez fermer le programme : ")

        if(answer1 == "1"):
            writeAutoExec()

def writeAutoExec():
    try:
        file = open("C:/Program Files (x86)/Steam/steamapps/common/GarrysMod/garrysmod/cfg/autoexec.cfg", "a")
        file.write("gmod_mcore_test 1\nmat_queue_mode -1\ncl_threaded_bone_setup 1\ncl_smooth 0\nmat_mipmaptextures 0\nr_decal_cullsize 1\nfog_enable 0\nmp_decals 3\n")
        file.close()
    except OSError as e:
        print(e)
    else:
        print("\n\nModification du fichier autoexec.cfg terminé !")
    
    answer2 = input("\n\nTaper 1 si vous voulez supprimer tous les fichiers cache\nAppuyer sur ENTREE si vous voulez fermer le programme : ")

    if(answer2 == "1"):
        deleteCache()

if __name__ == "__main__":
    main()