import networkx as nx
import json
import pickle

flagged_users_file = file("Hand_Flagged_Users.txt")
multi_triangles_file = file("Oxycontin_Triangle_User_Multiple.txt")
multi_nonrecip_file = open("Oxycontin_Non-Reciprocal_Tri_Users.txt")
graph_data = file ("13-2015_social_graph.json")

flagged_users = set()
multi_triangle_users = set()
multi_nonrecip_users = set()

line = flagged_users_file.readline()
while line != "":
    try:
        flagged_users.add(int(line))
        line = flagged_users_file.readline()
    except ValueError:
        pass
        line = flagged_users_file.readline()
flagged_users_file.close()

line = multi_triangles_file.readline()
while line != "":
    try:
        multi_triangle_users.add(int(line))
        line = multi_triangles_file.readline()
    except ValueError:
        pass
        line = multi_triangles_file.readline()
multi_triangles_file.close()

line = multi_nonrecip_file.readline()
while line != "":
    try:
        multi_nonrecip_users.add(int(line))
        line = multi_nonrecip_file.readline()
    except ValueError:
        pass
        line = multi_nonrecip_file.readline()
multi_nonrecip_file.close()


oxy_and_mulit_tris = set()
for oxys in flagged_users:
    oxy_and_mulit_tris.add(oxys)
for tris in multi_triangle_users:
    oxy_and_mulit_tris.add(tris)
for nons in multi_nonrecip_users:
    oxy_and_mulit_tris.add(nons)
nodelings = open("Oxy_Tris_User_Edges.txt",'w')
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
        if int(j["user_id"]) in oxy_and_mulit_tris:
            follower = set(j["follower_ids"]).intersection(oxy_and_mulit_tris)
            following = oxy_and_mulit_tris.intersection(set(j["friend_ids"]))

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
count2 = 0
count3 = 0
file = open("Oxy_Tris_User_Nodes.txt",'w')
file.write("Id Label")
file.write("\n")
for nodes in connected_users:
    if nodes in flagged_users:
        file.write(str(nodes))
        file.write(str(" Oxy"))
        file.write(str("\n"))
        count1 = count1 + 1
    elif nodes in multi_triangle_users:
        file.write(str(nodes))
        file.write(str(" Tri"))
        file.write(str("\n"))
        count2 = count2 + 1
    elif nodes in multi_nonrecip_users:
        file.write(str(nodes))
        file.write(str(" Non"))
        file.write(str("\n"))
        count3 = count3 + 1 
file.close()

print "Number of Oxycontin Users in List:"
print len(flagged_users)
print "Number of Oxycontin Users found via Connections:"
print count1
print "Number of Triangle Users in List:"
print len(multi_triangle_users)
print "Number of Triangle Users found via Connections:"
print count2
print "Number of Nonreciprocal Triangle Users in List:"
print len(multi_nonrecip_users)
print "Number of Nonreciprocal Triangle Users found via Connections"
print count3