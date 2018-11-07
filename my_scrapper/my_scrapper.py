from scrape_linkedin import ProfileScraper
import json
import pymongo
import selenium.common.exceptions


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["profiles"]

mylist = []
with open("profile_names.txt", "r") as ins:
    for line in ins:
        try:
            with ProfileScraper() as scraper:
                profile = scraper.scrape(user=line)
            mylist.append(profile.to_dict()) 
            x = mycol.insert_one(profile.to_dict())
        except ValueError:
            print('Error: invalid profile')
            continue
        except Exception:
            print('Error: invalid profile')
            continue
    r = json.dumps(mylist)
    with open('rsult.json', 'w') as f2:
        f2.write("%s" % r)