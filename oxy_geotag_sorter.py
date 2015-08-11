import networkx as nx
import json
import pickle

tweet_ids_file = file("Flagged_Oxy_Tweet_Ids.txt")
tweet_set_1 = file("Flagged_Oxycontin_Tweets_Filtered.json")
tweet_set_2 = file("Flagged_Oxycontin_Tweets_Filtered_Large.json")

tweet_ids = set()

line = tweet_ids_file.readline()
while line != "":
    try:
        tweet_ids.add(int(line))
        line = tweet_ids_file.readline()
    except ValueError:
        pass
        line = tweet_ids_file.readline()
tweet_ids_file.close()

count = 0
file = open("Oxy_Geotags.txt",'w')
file.write(str("Latitude, Longitude"))
file.write(str("\n"))
while True:
    line = tweet_set_1.readline()
    if line == "":
        break
    try:
        j = json.loads(line)
        if int(j["id"]) in tweet_ids:
            if j["user"]["geo_enabled"]:
                #file.write(str("["))
                file.write(str(j["geo"]["latitude"]))
                file.write(str(", "))
                file.write(str(j["geo"]["longitude"]))
                #file.write(str("]"))
                file.write(str("\n"))
                count = count + 1
    except ValueError:
        pass
tweet_set_1.close()

while True:
    line = tweet_set_2.readline()
    if line == "":
        break
    try:
        j = json.loads(line)
        if int(j["id"]) in tweet_ids:
            if j["user"]["geo_enabled"]:
                if j["geo"] != None:
                    try:
                        #print j["id"]
                        #print j["geo"]["coordinates"]
                        file.write(str(j["geo"]["coordinates"]))
                        #file.write(str(" "))
                        #file.write(str(j["geo"]["longitude"]))
                        file.write(str("\n"))
                        count = count + 1
                    except KeyError:
                        pass
    except ValueError:
        pass
tweet_set_2.close()    

print "Number of Oxy Tweets:"
print len(tweet_ids)
print "Number of Oxy Tweets with Geotags:"
print count 