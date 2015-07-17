import json
import codecs

tweets_file = file("1year_filtered.json")
# flagged_users_file = file("Flagged_Oxycontin_Users.txt")
#flagged_users_file = file("Oxycontin_Yes_Histogram.txt")
flagged_users_file = file("Hand_Flagged_Users.txt")

triangle_users_file = file("Oxycontin_User_Triangle_Thirds.txt")

multi_users_file = file("Oxycontin_Triangle_User_Multiple.txt")

#oxy_tweets = set()
flagged_users = set()
triangle_users = set()
multi_users =set()

line = flagged_users_file.readline()
while line != "":
	try:
		flagged_users.add(int(line))
		line = flagged_users_file.readline()
	except ValueError:
		pass
		line = flagged_users_file.readline()
flagged_users_file.close()

line = triangle_users_file.readline()
while line != "":
	try:
		triangle_users.add(int(line))
		line = triangle_users_file.readline()
	except ValueError:
		pass
		line = triangle_users_file.readline()
triangle_users_file.close()

line = multi_users_file.readline()
while line != "":
	try:
		multi_users.add(int(line))
		line = multi_users_file.readline()
	except ValueError:
		pass
		line = multi_users_file.readline()
multi_users_file.close()

#print flagged_users

found_users = set()
found_tris = set()
found_multi =set()

file = open("Flagged_Users_Tweets.txt","w")
tris = open("Triangle_Users_Tweets.txt",'w')
multi = open("Triangle_Multiple_User_Tweets.txt",'w')
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
			if int(j["user"]["id_str"]) not in found_users:
				found_users.add(int(j["user"]["id_str"]))
		if int(j["user"]["id_str"]) in triangle_users:
			tris.write(str(j["id"]))
			tris.write(";")
			tris.write(str(j["user"]["id_str"]))
			tris.write(";")
			tris.write(str(j["created_at"])[5:25])
			tris.write(";")
			tris.write(str(j["text"].encode('unicode-escape')))
			tris.write("\n")
			if int(j["user"]["id_str"]) not in found_tris:
				found_tris.add(int(j["user"]["id_str"]))
		if int(j["user"]["id_str"]) in multi_users:
			multi.write(str(j["id"]))
			multi.write(";")
			multi.write(str(j["user"]["id_str"]))
			multi.write(";")
			multi.write(str(j["created_at"])[5:25])
			multi.write(";")
			multi.write(str(j["text"].encode('unicode-escape')))
			multi.write("\n")
			if int(j["user"]["id_str"]) not in found_multi:
				found_multi.add(int(j["user"]["id_str"]))				
	except ValueError:
		pass
		file.write("\n")
		tris.write("\n")
		multi.write("\n")
	line = tweets_file.readline()	
tweets_file.close()
file.close()
tris.close()
multi.close()

print "Number of Oxy User's Twitterings Sought:"
print len(flagged_users)
print "Number of Oxy User's Twitterings Found:"
print len(found_users)
print "Number of Triangle User's Twitterings Sought:"
print len(triangle_users)
print "Number of Triangle User's Twitterings Found:"
print len(found_tris)
print "Number of Multi-Triangle User's Twitterings Sought"
print len(multi_users)
print "Number of Multi-Triangle User's Twitterings Found:"
print len(found_multi)