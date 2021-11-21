import os
import random
import requests

TILE_SERVER = {
    "OSMChina": ["{protocol}{random}tile.osmchina.org/{z}/{x}/{y}.png",
                 ["https", "http"],
                 "",
                 ""],
    "Teacestrack": ["{protocol}{random}tile.tracestrack.org/{z}/{x}/{y}.png{apikey}",
                    ["https", "http"],
                    "a-c"
                    "?apikey=9f8f8f8f-9f8f-9f8f-9f8f-9f8f8f8f8f8"],
}

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "User-Agent": "OSMChina-TileRequest/0.2.0",
    "Cookie": "",
}


def RandomChar(begin: str, end: str):
    Range = int(ord(end) - ord(begin))
    tmp = random.randint(0, Range - 1)
    return chr(ord(begin) + tmp)


def fullURL(x: int, y: int, z: int, tile_name):
    # PREFIX
    PROTOCOL_PREFIX_HTTPS = "https://"
    PROTOCOL_PREFIX_HTTP = "http://"
    PROTOCOL_PREFIX_FTP = "ftp://"
    # 开始组装准备
    URL = TILE_SERVER[tile_name][0]
    if "osmchina.org" not in URL:
        print("Error: Not OSMChina tile service!")
    Protocol_list = TILE_SERVER[tile_name][1]
    if TILE_SERVER[tile_name][2] != "":
        Random_list = [TILE_SERVER[tile_name][2].split("-")[0], TILE_SERVER[tile_name][2].split("-")[1]]
    else:
        Random_list = ""
    # 组装协议
    if Protocol_list[0] == "https":
        URL = URL.replace("{protocol}", PROTOCOL_PREFIX_HTTPS)
    elif Protocol_list[0] == "ftp":
        URL = URL.replace("{protocol}", PROTOCOL_PREFIX_FTP)
    else:
        URL = URL.replace("{protocol}", PROTOCOL_PREFIX_HTTP)
    # 组装负载均衡
    if Random_list != "":
        URL = URL.replace("{random}", RandomChar(Random_list[0], Random_list[1]) + ".")
    else:
        URL = URL.replace("{random}", "")
    # 组装瓦片坐标
    URL = URL.replace("{x}", str(x))
    URL = URL.replace("{y}", str(y))
    URL = URL.replace("{z}", str(z))
    # 组装APIKEY
    if TILE_SERVER[tile_name][3] != "":
        URL = URL.replace("{apikey}", TILE_SERVER[tile_name][3])
    return URL


def atomicTask(x: int, y: int, z: int, tile_name: str):
    TaskURL = fullURL(x, y, z, tile_name)
    img = requests.get(url=TaskURL, headers=headers)
    filename = str(y) + ".png"
    with open(filename, "wb") as f:
        f.write(img.content)
    print(TaskURL)


def multipleTask(x_min, x_max, y_min, y_max, z, tile_name, task_name):
    x_max += 1
    y_max += 1
    os.system("mkdir " + task_name)
    os.chdir(task_name)
    for x in range(x_min, x_max):
        os.system("mkdir " + str(x))
        os.chdir(str(x))
        for y in range(y_min, y_max):
            atomicTask(x, y, z, tile_name)
        os.chdir("..")
    os.chdir("..")


def taskGenerator(zoom, tile_name, task_name, Mode="Region", x_min=0, x_max=0, y_min=0, y_max=0):
    if Mode == "Region":
        if zoom == 0:
            print("Error: zoom must be greater than 0 in Region Mode")
        else:
            if x_min == 0 and x_max == 0 and y_min == 0 and y_max == 0:
                x_min = int(input("请输入x_min:"))
                x_max = int(input("请输入x_max:"))
                y_min = int(input("请输入y_min:"))
                y_max = int(input("请输入y_max:"))
            Count = (x_max - x_min + 1) * (y_max - y_min + 1)
            print("Total tiles:", Count)
            multipleTask(x_min, x_max, y_min, y_max, zoom, tile_name, task_name)
    elif Mode == "Full":
        if zoom == 0:
            Count = 1
            print("Total tiles:", Count)
            multipleTask(0, 0, 0, 0, 0, tile_name, task_name)
        else:
            Count = pow(2, zoom * 2)
            print("Total tiles:", Count)
            multipleTask(0, pow(2, zoom) - 1, 0, pow(2, zoom) - 1, zoom, tile_name, task_name)
    else:
        print("Error: Mode Error")


if __name__ == "__main__":
    os.system("mkdir OSMChina_Backup")
    os.chdir("OSMChina_Backup")
    for i in range(10):
        taskGenerator(i, "OSMChina", "OSMChina_Backup_" + str(i), "Full")
