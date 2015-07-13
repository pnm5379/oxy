import json
import codecs

tweets_file_1 = file("Flagged_Oxycontin_Tweets_Filtered.json")
tweets_file_2 = file("Flagged_Oxycontin_Tweets_Filtered_Large.json")


found_tweets = set()

file = open("Oxy_IDs_Correction.txt","w")

line = tweets_file_1.readline()
while line != "":
	try:
		j = json.loads(line)
		if j["id"] not in found_tweets:
			found_tweets.add(j["id"])
			file.write(str(j["id"]))
			file.write(";")
			file.write(str(j["user"]["id_str"]))
			file.write(";")
			file.write(str(j["created_at"])[5:25])
			file.write(";")
			file.write(str(j["text"].encode('unicode-escape')))
			file.write("\n")
	except ValueError:
		pass
		file.write("\n")
	line = tweets_file_1.readline()	
tweets_file_1.close()

line = tweets_file_2.readline()
while line != "":
	try:
		j = json.loads(line)
		if j["id"] not in found_tweets:
			found_tweets.add(j["id"])
			file.write(str(j["id"]))
			file.write(";")
			file.write(str(j["user"]["id_str"]))
			file.write(";")
			file.write(str(j["created_at"])[8:11])
			file.write(str(j["created_at"])[4:8])
			file.write(str(j["created_at"])[26:30])
			file.write(str(j["created_at"])[10:19])
			file.write(";")
			file.write(str(j["text"].encode('unicode-escape')))
			file.write("\n")
	except ValueError:
		pass
		file.write("\n")
	line = tweets_file_2.readline()	
tweets_file_2.close()

file.close()

print "How many tweets were fixed:"
print len(found_tweets)

