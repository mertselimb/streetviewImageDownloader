import shutil
import requests
import os

API_KEY = 
SIGNATURE = 
SIZE = "640x640"
URL = 'https://maps.googleapis.com/maps/api/streetview?&size=' + SIZE
SAVE_LOC = "downloads"
TYPE = ".jpeg"
WARNING = '\033[93m'
GREEN = "\033[92m"
UNIMPORTANT = '\033[95m'
BLUE = '\033[94m'

if not os.path.exists(SAVE_LOC):
    os.makedirs(SAVE_LOC)

class link:
    def __init__(self, address, name):
        self.address = address
        self.name = name

def createLinks(location):
    links = []
    for heading in [0,90,180,270]:
        address = URL + "&location=" + location + "&heading=" + str(heading) + "&key=" + API_KEY + "&signature=" + SIGNATURE
        name = location + "_" + str(heading) + TYPE
        links.append(link(address,name))
    return links

def downloadImage(location):
    links = createLinks(location)
    for link in links:
        response = requests.get(link.address, stream=True)
        print(UNIMPORTANT + "Sent GET request to " + link.address)
        if(response.status_code == 200):
        	print(GREEN + "Response " + str(response.status_code))
        	with open(SAVE_LOC + "/" +link.name, 'wb') as out_file:
        		shutil.copyfileobj(response.raw, out_file)
        else:
        	print(WARNING + "Request failed status code " + str(response.status_code))
    del response

with open('koü.txt') as f:
    lines = f.readlines()
locations = [w.replace('\n', '') for w in lines]


def percentage(part, whole):
  return str(round(100 * float(part)/float(whole), 2))
length = len(locations)

print("Api key: " + API_KEY)
print("Signature: " + SIGNATURE)

i = 0
for location in locations:
    print(GREEN + "At " + percentage(i,length) + "%")
    print(BLUE + "Location : " + location)
    downloadImage(location)
    i += 1