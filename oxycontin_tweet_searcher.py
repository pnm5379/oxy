import json
import codecs

tweets_file = file("1year_filtered.json")
tweet_keyword_file = file("Oxycontin_Keywords.json")

k = json.load(tweet_keyword_file)
tweet_keyword_file.close()
keys = set(k["key_words"])

pain = set(k["pain"])
killer = set(k["killer"])
hills = set(k["hills"])
heroin = set(k["heroin"])

keys.union(killer)
keys.union(hills)

#oxy_tweets = set()
#double_tweets = set()
flagged_users = set()

count = 0
file = open("Flagged_Oxycontin_Tweets_Filtered.txt","w")
raws = open("Flagged_Oxycontin_Tweets_Filtered.json","w")
line = tweets_file.readline()
while line != "":
	try:
		j = json.loads(line)
		#if j["id"] not in oxy_tweets:
		tweet = set(j["text"].encode('unicode-escape').replace('\\',' ').replace('#',' ').split())
		temp = keys.intersection(tweet)
		if temp:
			kill = killer.intersection(temp)
			hillbill = hills.intersection(temp)
			if kill:
				p = pain.intersection(tweet)
				if p:
					file.write(str(j["id"]))
					file.write(";")
					file.write(str(j["user"]["id_str"]))
					file.write(";")
					file.write(str(temp))
					file.write(";")
					file.write(str(j["created_at"])[5:25])
					file.write(";")
					file.write(str(j["text"].encode('unicode-escape')))
					file.write("\n")
					#oxy_tweets.add(j["id"])
					flagged_users.add(str(j["user"]["id_str"]))
					count = count + 1
					json.dump(j,raws)
					raws.write("\n")
			elif hillbill:
				h = heroin.intersection(temp)
				if h:
					file.write(str(j["id"]))
					file.write(";")
					file.write(str(j["user"]["id_str"]))
					file.write(";")
					file.write(str(temp))
					file.write(";")
					file.write(str(j["created_at"])[5:25])
					file.write(";")
					file.write(str(j["text"].encode('unicode-escape')))
					file.write("\n")
					#oxy_tweets.add(j["id"])
					flagged_users.add(str(j["user"]["id_str"]))
					count = count + 1
					json.dump(j,raws)
					raws.write("\n")
			else:
				file.write(str(j["id"]))
				file.write(";")
				file.write(str(j["user"]["id_str"]))
				file.write(";")
				file.write(str(temp))
				file.write(";")
				file.write(str(j["created_at"])[5:25])
				file.write(";")
				file.write(str(j["text"].encode('unicode-escape')))
				file.write("\n")
				#oxy_tweets.add(j["id"])
				flagged_users.add(str(j["user"]["id_str"]))
				count = count + 1
				json.dump(j,raws)
				raws.write("\n")
		# else:
		# 	double_tweets.add(j["id"])		
	except ValueError:
		pass
		file.write("\n")
	line = tweets_file.readline()	
tweets_file.close()
file.close()
raws.close
	
print "Number of Flagged Tweets:"	
print count

count = 0
file = open("Flagged_Oxycontin_Users.txt","w")
for users in flagged_users:
	file.write(str(users))
	file.write("\n")
	count = count + 1
file.close()

print "Number of Flagged Users"
print count