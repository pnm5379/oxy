import json
import codecs

tweets_file = file("1year_filtered.json")
# flagged_users_file = file("Flagged_Oxycontin_Users.txt")
#flagged_users_file = file("Oxycontin_Yes_Histogram.txt")
flagged_users_file = file("Hand_Flagged_Users.txt")

#oxy_tweets = set()
flagged_users = set()

line = flagged_users_file.readline()
while line != "":
	try:
		flagged_users.add(int(line))
		line = flagged_users_file.readline()
	except ValueError:
		pass
		line = flagged_users_file.readline()
flagged_users_file.close()

#print flagged_users

file = open("Flagged_Users_Tweets.txt","w")
line = tweets_file.readline()
while line != "":
	try:
		j = json.loads(line)
		#if j["id"] not in oxy_tweets:
			#print j["user"]
		if int(j["user"]["id_str"]) in flagged_users:
			file.write(str(j["id"]))
			file.write(";")
			file.write(str(j["user"]["id_str"]))
			file.write(";")
			file.write(str(j["created_at"])[5:25])
			file.write(";")
			file.write(str(j["text"].encode('unicode-escape')))
			file.write("\n")
			#oxy_tweets.add(j["id"])		
	except ValueError:
		pass
		file.write("\n")
	line = tweets_file.readline()	
tweets_file.close()
file.close()
