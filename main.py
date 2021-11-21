from Src import 

if __name__ == "__main__":
    os.system("mkdir OSMChina_Backup")
    os.chdir("OSMChina_Backup")
    for i in range(10):
        taskGenerator(i, "OSMChina", "OSMChina_Backup_" + str(i), "Full")
