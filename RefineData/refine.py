import pymongo
from pymongo import MongoClient
import pprint
import json
import csv
import datetime



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
profiles = mydb["profiles"]
print('Total Record for the collection: ' + str(profiles.count()))
profile_list = []
for profile in profiles.find():
    profile['_id'] = str(profile['_id'])
    profile_list.append(profile)
jsondata = json.dumps(profile_list)

now = datetime.datetime.now()
print(now.year)
#with open('data.csv', 'wb') as csvfile:
#    filewriter = csv.writer(csvfile, delimiter=',',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    filewriter.writerow(['Name', 'Profession'])
private_schools = ["esprit","tekup","centrale","ult","privé","prive","leaders "]
degree = ["licence","technicien","master","mastère"]
it_skills = ["network","web","linux","c","c++","python","java","cloud","c#","pl/sql","uml","réseau","jee","sécurité","node.js","angular","html","php","css","mysql","android","javascript"] 
with open('data.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["prive","esprit","licence","graduated","year_after_graduation","skills_score"])
    for i in range(profiles.count()):
        r = json.dumps(profile_list[i])
        jsonobj = json.loads(r)
        if jsonobj["experiences"]["education"] is not None:
            esprit = 0
            prive = 0
            licence = 0
            for edu in jsonobj["experiences"]["education"]:
                if "ESPRIT" in edu['name']: esprit = 1
                for elem in private_schools:
                    if elem in edu['name'].lower():
                        prive = 1
                        break
                if prive==0:
                    for elem in degree:
                        if edu["degree"] is not None:                        
                            if elem in edu['degree'].lower():
                                if "licence" == elem or "technicien" == elem:
                                    licence = 1
                                else:
                                    licence = 0.2

            #print(esprit)
            graduated = 0
            year_after_graduation = 0
            print(jsonobj["experiences"]["education"])
            if len(jsonobj["experiences"]["education"])!=0:
                if jsonobj["experiences"]["education"][0]["date_range"] is not None:
                    dtrange = str(jsonobj["experiences"]["education"][0]["date_range"])
                    date = dtrange[len(dtrange)-4:len(dtrange)]
                    difference = int(now.year) - int(date)
                    if difference > 0:
                        graduated = 1
                    if graduated == 1:
                        year_after_graduation = difference
                    #print(date)
                    #print(graduated)
                #print(licence)
        if jsonobj["skills"] is not None:
            skills_score = 0
            for skill in jsonobj["skills"]:
                for itskill in it_skills:
                    if itskill in skill["name"].lower():
                        skills_score = skills_score + 0.1
            #print("{:10.2f}".format(skills_score))
        filewriter.writerow([str(prive),str(esprit),str(licence),str(graduated),str(year_after_graduation),str("{:.2f}".format(skills_score))])

