from Src.Requester import taskGenerator

import os
import random
import requests

if __name__ == "__main__":
    os.system("mkdir OSMChina_Backup")
    os.chdir("OSMChina_Backup")
    LOW_ZOOM = 1
    HIGH_ZOOM = 3
    for i in range(LOW_ZOOM, HIGH_ZOOM + 1):
        taskGenerator(i, "OSMChina", "tes2t_OSMChina_Backup_" + str(i), "Full")
