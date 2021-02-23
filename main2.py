import os
from xml.dom import minidom
import subprocess

p = subprocess.run("netsh wlan export profile interface=wi-fi key=clear folder=C:\\Cyber3\\challenges\\3")




print("\n moving to phase 2\n")
dictionary = {}

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".xml"): 
        print("\n")
        print(f"{filename} is: {os.path.join(os.getcwd(), filename)}")
        xmldoc = minidom.parse(filename)
        # att = xmldoc.getElementsByTagName('keyMaterial')[0].childNodes[0].nodeValue
        name = xmldoc.getElementsByTagName('name')[0].childNodes[0].nodeValue
        # print(f"name is: {name}")
        keyMaterials = xmldoc.getElementsByTagName('keyMaterial')
        if len(keyMaterials) >= 1: 
            pas = keyMaterials[0].childNodes[0].nodeValue
            # print(f"password: {pas}")
            dictionary.update({f"{name}": f"{pas}"})
        else: print(f"no such tag as keyMaterial in {filename}")
        print("\n")

# for x, y in dictionary.items():
#     print(f"{x} : {y}\n")

with open('output.txt', 'w') as f:  
    for key, val in dictionary.items():
        f.write(f"{key} : {val}\n")




