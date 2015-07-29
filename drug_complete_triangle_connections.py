import networkx as nx
import json
import pickle

flagged_users_file = file("Complete_Drug_Triangle_Users.txt")
graph_data = file ("13-2015_social_graph.json")

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

nodelings = open("Drug_Complete_Tris_Edges.txt",'w')
nodelings.write(str("Source Target"))
nodelings.write(str("\n"))
connected_users = set()
connected_pairs = set()

while True:
    line = graph_data.readline()
    if line == "":
        break
    try:
        j = json.loads(line)
        if int(j["user_id"]) in flagged_users:
            follower = set(j["follower_ids"]).intersection(flagged_users)
            following = flagged_users.intersection(set(j["friend_ids"]))

            for followers in follower:
                dubs = ' '.join([str(j["user_id"]),str(followers)])
                if dubs not in connected_pairs:
                    connected_pairs.add(dubs)
                    connected_users.add(int(j["user_id"]))
                    connected_users.add(int(followers))
                    nodelings.write(dubs)
                    nodelings.write(str("\n"))

            for friends in following:
                dubs = ' '.join([str(friends),str(j["user_id"])])
                if dubs not in connected_pairs: 
                    connected_pairs.add(dubs)
                    connected_users.add(int(j["user_id"])) 
                    connected_users.add(int(friends))
                    nodelings.write(dubs)
                    nodelings.write(str("\n"))

    except ValueError:
        pass
nodelings.close()
graph_data.close()      

count1 = 0
file = open("Drug_Complete_Tris_Nodes.txt",'w')
file.write("Id Label")
file.write("\n")
for nodes in connected_users:
    if nodes in flagged_users:
        file.write(str(nodes))
        file.write(str(" Drug"))
        file.write(str("\n"))
        count1 = count1 + 1
file.close()

print "Number of Drug Tweeting, Complete Triangle Forming Users Sought:"
print count1
