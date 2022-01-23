Dict = {"coding": "try to make pasion",
"vivek": "down to earth person",
"marks" : [2,4,2,4] , 
 "anotherDict" : {'viv' : 'pepole'}
}
print (Dict["coding"])

print(Dict["vivek"])
print(Dict["marks"])
print(Dict["anotherDict"]["viv"])
Dict["marks"] = [12,23,34]
print(Dict["marks"]) 

#METHOD 
print(Dict.keys())   #print the keys of the dict
print(Dict.values())  #print the values of the dict
print(Dict.items())   #print the values and keys of the dict

print(Dict)
updateMydict = {
    "ramu": "samu",
    "kamu": "tamu",
    "vivek": "angry man"
}
Dict.update(updateMydict)
print(Dict)

print(Dict.get("vivek"))        #print value of vivek 
print(Dict["vivek"])            #print value of vivek

#diffrence btwn .get and [] syntax in dictionary
print(Dict.get("vivek2"))    #returns non as vivek2 is not present in dict
print(Dict["vivek2"])        #though an error as vivek2 is not present in dict