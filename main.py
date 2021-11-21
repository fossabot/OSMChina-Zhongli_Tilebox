import os

from Src.Requester import taskGenerator

if __name__ == "__main__":
    TASK_MODE = "Backup"
    # ÍÆ¼öµÄTASK_MODE: Backup, Debug, Development£¬PressureTest
    os.system("mkdir OSMChina_" + TASK_MODE)
    os.chdir("OSMChina_" + TASK_MODE)
    LOW_ZOOM = 1
    HIGH_ZOOM = 3
    for i in range(LOW_ZOOM, HIGH_ZOOM + 1):
        taskGenerator(i, "OSMChina", "OSMChina_" + TASK_MODE + "_" + str(i), "Full")
