#!python3.4
#Scratch File Edit API
#Version 0.5

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

obj = open("Maze Starter/project.json", "r+", encoding="utf8")
text = obj.read()

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
        self.origText=text
        self.text=text
        self.sprites=[]
        
        self.modify()
        self.spriteCreate()

    def modify(self):
        self.text=self.text.replace("\t","")
        self.text=self.text.replace("\n","")
        self.sprites = self.text.split("\"children\": [")[1:]
        self.sprites = self.sprites[0].split("{\"objName\"")
        for i,txt in enumerate(self.sprites):
            self.sprites[i]="{\"objName\""+txt
        self.sprites.pop(0)
        
        for i,sprite in enumerate(self.sprites):
            self.sprites[i]=cut(sprite)+"}"

    def spriteCreate(self):
        for i, sprite_data in enumerate(self.sprites):
            self.sprites[i]=Sprite(sprite_data)

    def save(self):
        self.part1 = self.text.split("\"children\": [")[0]+"\"children\": ["
        
        self.allSpriteData=[]
        self.part2=""
        self.converted=""
        
        for s in self.sprites:
            self.allSpriteData.append(s.saveAllKeys())
        
        self.converted = ",".join(self.allSpriteData)
        self.converted=self.converted[:-2]+"]},"

        self.part2=self.text[len(self.part1+self.converted)-1:]
        return (self.part1+self.converted+self.part2)
        
class Sprite:

    def __init__(self,data):
        self.data=data
        self.split_data=data.split(",")
        self.loads=json.loads(data)

        
        self.keys=[
            "scratchX",
            "scratchY",
            "direction",
            "visible",
            "scale",
            "currentCostumeIndex",
            "objName",
            "isDraggable",
            "rotationStyle",
            "indexInLibrary"
            ]
        
        
        #--Positions----------------------------
        self.x=int(self.loads["scratchX"])
        self.y=int(self.loads["scratchY"])
        
        #--Visible Attributes-------------------
        self.direction=int(self.loads["direction"])
        self.visible=self.loads["visible"]
        self.scale=int(self.loads["scale"])
        self.currentCostumeIndex=int(self.loads["currentCostumeIndex"])+1 #Ajust for 0 starting index
        
        #--Non-Visible Attributes---------------
        self.name=self.loads["objName"]
        self.isDraggable=self.loads["isDraggable"]
        self.rotationStyle=self.loads["rotationStyle"]
        self.indexInLibrary=int(self.loads["indexInLibrary"])

    def valOfKey(self,key):
        if key == "scratchX":
            return self.x
        elif key == "scratchY":
            return self.y
        elif key == "direction":
            return self.direction
        elif key == "visible":
            return self.visible
        elif key == "scale":
            return self.scale
        elif key == "currentCostumeIndex":
            return self.currentCostumeIndex
        elif key == "objName":
            return self.name
        elif key == "isDraggable":
            return self.isDraggable
        elif key == "rotationStyle":
            return self.rotationStyle
        elif key == "indexInLibrary":
            return self.indexInLibrary
        else:
            raise KeyError("JSON Key Error: "+key)

    def modifyKey(self,key,value):
        self.temp=self.data.split("\""+key+"\": ")
        self.data=(self.temp[0]+"\""+key+"\": ")+str(value)+","+(",".join(self.temp[1].split(",")[1:]))

    def saveAllKeys(self):
        for key in self.keys:
            self.modifyKey(key,self.valOfKey(key))
        return self.data

#p=API(text)       Debug   
