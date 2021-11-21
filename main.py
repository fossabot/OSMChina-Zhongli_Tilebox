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


def fullURL(x: int, y: int, z: int, name):
    PROTOCOL_PREFIX_HTTPS = "https://"
    PROTOCOL_PREFIX_HTTP = "http://"
    PROTOCOL_PREFIX_FTP = "ftp://"
    URL = TILE_SERVER[name][0]
    Protocol_list = TILE_SERVER[name][1]
    if TILE_SERVER[name][2] != "":
        Random_list = [TILE_SERVER[name][2].split("-")[0], TILE_SERVER[name][2].split("-")[1]]
    else:
        Random_list = ""
    if Protocol_list[0] == "https":
        URL = URL.replace("{protocol}", PROTOCOL_PREFIX_HTTPS)
    elif Protocol_list[0] == "ftp":
        URL = URL.replace("{protocol}", PROTOCOL_PREFIX_FTP)
    else:
        URL = URL.replace("{protocol}", PROTOCOL_PREFIX_HTTP)
    if Random_list != "":
        URL = URL.replace("{random}", RandomChar(Random_list[0], Random_list[1]) + ".")
    else:
        URL = URL.replace("{random}", "")
    URL = URL.replace("{x}", str(x))
    URL = URL.replace("{y}", str(y))
    URL = URL.replace("{z}", str(z))
    print(URL)
    return URL


def RandomChar(begin: str, end: str):
    Range = int(ord(end) - ord(begin))
    tmp = random.randint(0, Range - 1)
    return chr(ord(begin) + tmp)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Cookie": "",
}

def task(x,y,z,name):
    img=requests.get(url=fullURL(x,y,z,name),headers=headers)
    filename=str(z)+".png"
    with open(filename,"wb") as f:
        f.write(img.content)

task(107, 50, 7, "OSMChina")