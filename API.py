#!python3.4
#Scratch File Edit API
#Version 0.1

#Made By:
#
# /$$$$$$                     /$$          
#|_  $$_/                    | $$          
#  | $$    /$$$$$$$  /$$$$$$ | $$ /$$   /$$
#  | $$   /$$_____/ /$$__  $$| $$| $$  | $$
#  | $$  | $$      | $$$$$$$$| $$| $$  | $$
#  | $$  | $$      | $$_____/| $$| $$  | $$
# /$$$$$$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$
#|______/ \_______/ \_______/|__/ \____  $$
#                                 /$$  | $$
#                                |  $$$$$$/
#       [icelys.github.io]        \______/ 

import json

obj = open("API File/project.json", "r+", encoding="utf8")
text = "{\""+obj.read()+"}"

obj.close()


def section(o,c,text):
    count=0
    indent = 0
    for letter in text:
        if letter == o:
            indent+=1
        if letter == c:
            indent-=1
        if indent==0:
            break

        count+=1
    return count

def cut(text):
    return text[0:section("{","}",text)]

class API:

    def __init__(self,text):
        self.text=text
        self.sprites=[]
        
        self.modify()
        self.spriteCreate()

    def modify(self):
        self.text=self.text.replace("\t","")
        self.text=self.text.replace("\n","")
        self.sprites = self.text.split("\"children\": [")[1:]
        
        for i,sprite in enumerate(self.sprites):
            self.sprites[i]=cut(sprite)+"}"

    def spriteCreate(self):
        for i, sprite_data in enumerate(self.sprites):
            self.sprites[i]=Sprite(sprite_data)

class Sprite:

    def __init__(self,data):
        self.split_data=data.split(",")
        
        
        #--Positions----------------------------
        self.x=int(json.loads(data)["scratchX"])
        self.y=int(json.loads(data)["scratchY"])
        
        #--Visible Attributes-------------------
        self.dir=int(json.loads(data)["direction"])
        self.showing=json.loads(data)["visible"]
        self.sizeScale=int(json.loads(data)["scale"])
        self.costume=int(json.loads(data)["currentCostumeIndex"])+1 #Ajust for 0 starting index
        
        #--Non-Visible Attributes---------------
        self.draggable=json.loads(data)["isDraggable"]
        self.rotStyle=json.loads(data)["rotationStyle"]
        self.libNum=int(json.loads(data)["indexInLibrary"])


    
