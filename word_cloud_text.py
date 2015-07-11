import json
import codecs

tweets_file_1 = file("Flagged_Oxycontin_Tweets_Filtered.json")
tweets_file_2 = file("Flagged_Oxycontin_Tweets_Filtered_Large.json")


flagged_tweets_file = file("Hand_Flagged_Tweets.txt")

#oxy_tweets = set()
flagged_tweets = set()
found_tweets = set()

line = flagged_tweets_file.readline()
while line != "":
	try:
		flagged_tweets.add(int(line))
		line = flagged_tweets_file.readline()
	except ValueError:
		pass
		line = flagged_tweets_file.readline()
flagged_tweets_file.close()

file = open("Word_Cloud.txt","w")

line = tweets_file_1.readline()
while line != "":
	try:
		j = json.loads(line)
		if int(j["id"]) in flagged_tweets:
			if int(j["id"]) not in found_tweets:
				found_tweets.add(int(j["id"]))
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
		if int(j["id"]) in flagged_tweets:
			if int(j["id"]) not in found_tweets:
				found_tweets.add(int(j["id"]))
				file.write(str(j["text"].encode('unicode-escape')))
				file.write("\n")
	except ValueError:
		pass
		file.write("\n")
	line = tweets_file_2.readline()	
tweets_file_2.close()

file.close()

print "How many tweets wanted:"
print len(flagged_tweets)
print "How many tweets were found:"
print len(found_tweets)

