import os
import random
import requests

TILE_SERVER = {
    "OpenStreetMap Default(Carto)": ["{protocol}{random}tile.openstreetmap.org/{z}/{x}/{y}.png",
                                     ["https", "http"],
                                     "a-c"],
    "OpenStreetMap HOT": ["{protocol}{random}tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
                          ["https", "http"],
                          "a-c"],
    "OSMChina": ["{protocol}{random}tile.osmchina.org/{z}/{x}/{y}.png",
                 ["https", "http"],
                 ""],
}

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "User-Agent": "OSMChina-TileRequest/Debug-0.0.0",
    "Cookie": "",
}

def RandomChar(begin: str, end: str):
    Range = int(ord(end) - ord(begin))
    tmp = random.randint(0, Range - 1)
    return chr(ord(begin) + tmp)

def fullURL(x: int, y: int, z: int, name):
    # PREFIX
    PROTOCOL_PREFIX_HTTPS = "https://"
    PROTOCOL_PREFIX_HTTP = "http://"
    PROTOCOL_PREFIX_FTP = "ftp://"
    # 开始组装准备
    URL = TILE_SERVER[name][0]
    Protocol_list = TILE_SERVER[name][1]
    if TILE_SERVER[name][2] != "":
        Random_list = [TILE_SERVER[name][2].split("-")[0], TILE_SERVER[name][2].split("-")[1]]
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
    return URL


def atomicTask(x:int,y:int,z:int,name:str):
    TaskURL=fullURL(x,y,z,name)
    img=requests.get(url=TaskURL,headers=headers)
    filename=str(y)+".png"
    with open(filename,"wb") as f:
        f.write(img.content)
    print(TaskURL)

def multipleTask(x_min,x_max,y_min,y_max,z,name):
    for x in range(x_min,x_max):
        os.system("mkdir "+str(x))
    for x in range(x_min,x_max):
        os.system("cd "+str(x))
        for y in range(y_min,y_max):
            os.system("mkdir "+str(y))
        for y in range(y_min,y_max):
            os.system("cd "+str(y))
            atomicTask(x,y,z,name)

if __name__ == "__main__":
    os.system("mkdir 0")
    # os.system("cd 0")
    os.chdir("0")
    os.system("echo %cd%")
    # os.system("pwd")
    #multipleTask(0,3,0,3,2,"OSMChina")