import networkx as nx
import json
import pickle


flagged_users_file = file("Flagged_Drug_Users.txt")
graph_data = file ("13-2015_social_graph.json")

flagged_users = set()
reciprocal_users = set()


line = flagged_users_file.readline()
while line != "":
    try:
        flagged_users.add(int(line))
        line = flagged_users_file.readline()
    except ValueError:
        pass
        line = flagged_users_file.readline()
flagged_users_file.close()

print "Number of Flagged Users:"
print len(flagged_users)
 
count1 = 0
count2 = 0
count3 = 0
connected_users = set()
file = open("Drug_Connections.txt",'w')
recips = open("Reciprocal_Drug_Users.txt",'w')
pantry = open("Reciprocal_Drug_Social_Graph.json",'w')
nodelings = open("Drug_User_Edges.txt",'w')
nodelings.write(str("Source Target"))
nodelings.write(str("\n"))
holding = set()
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
                file.write(str(j["user_id"]))
                file.write(" ")
                file.write(str(followers))
                file.write("\n")
                #dubs_list = (str(j["user_id"])," ",str(followers))
                dubs = ' '.join([str(j["user_id"]),str(followers)])
                if dubs not in connected_pairs:
                    connected_pairs.add(dubs)
                    #print dubs
                    connected_users.add(int(j["user_id"]))
                    connected_users.add(int(followers))
                    #nodelings.write(str(j["user_id"]))
                    #nodelings.write(str(" "))
                    #nodelings.write(str(followers))
                    nodelings.write(dubs)
                    nodelings.write(str("\n"))

            for friends in following:
                file.write(str(friends))
                file.write(" ")
                file.write(str(j["user_id"]))
                file.write("\n")
                dubs = ' '.join([str(friends),str(j["user_id"])])
                if dubs not in connected_pairs: 
                    connected_pairs.add(dubs)
                    connected_users.add(int(j["user_id"])) 
                    connected_users.add(int(friends))
                    #nodelings.write(str(friends))
                    #nodelings.write(str(" "))
                    #nodelings.write(str(j["user_id"]))
                    nodelings.write(dubs)
                    nodelings.write(str("\n"))

            count1 = count1 + 1  

            mutual = set(j["follower_ids"]).intersection(set(j["friend_ids"]))
            temp = mutual.intersection(flagged_users)
            for newbs in temp:
                if int(newbs) and int(j["user_id"]) not in reciprocal_users:
                    reciprocal_users.add(int(newbs))
                    reciprocal_users.add(int(j["user_id"]))
                    recips.write(str(j["user_id"]))
                    recips.write(str(" "))
                    recips.write(str(newbs))
                    recips.write("\n")
                    count2 = count2 + 1

            if int(j["user_id"]) in reciprocal_users:         
                if int(j["user_id"]) not in holding:
                    json.dump(j,pantry)
                    holding.add(int(j["user_id"]))
                    pantry.write("\n")
                    count3 = count3 + 1
    except ValueError:
        pass
file.close()
recips.close()
pantry.close()  
nodelings.close()      

#graph_data.close()

print "Number of Flagged Users in the Graph File:"
print count1
print "Of Whom This Many Have Connections Amongst Each Other:"
print len(connected_users)

# file = open("Oxycontin_User_Nodes.txt",'w')
# file.write(str("Users"))
# file.write(str("\n"))
# for people in connected_users:
#     file.write(str(people))
#     file.write(str("\n"))
# file.close()

# graph_data.seek(0)
# count = 0
# file = open("Reciprocal_Oxy_Users.txt",'w')
# while True:
#     line = graph_data.readline()
#     if line == "":
#         break
#     try:
#         j = json.loads(line)
#         if int(j["user_id"]) in flagged_users:
#             mutual = set(j["follower_ids"]).intersection(set(j["friend_ids"]))
#             temp = mutual.intersection(flagged_users)
#             for newbs in temp:
#                 if int(newbs) and int(j["user_id"]) not in reciprocal_users:
#                     reciprocal_users.add(int(newbs))
#                     reciprocal_users.add(int(newbs))
#                     file.write(str(j["user_id"]))
#                     file.write(str(" "))
#                     file.write(str(newbs))
#                     file.write("\n")
#                     count = count + 1
#     except ValueError:
#         pass
# file.close()        

print "Number of Reciprocal Drug User-Pairs:"
print count2

print "Between this many users:"
print len(reciprocal_users)

print "Of whom this many Users are in the Graph File:"
print count3

triangle_users = set()
multi_triangles = set()

recips = open("Reciprocal_Drug_Users.txt",'r')
pantry = open("Reciprocal_Drug_Social_Graph.json",'r')
file = open("Drug_User_Social_Triangles.txt",'w')
equalateral = open("Drug_User_Triangle_Thirds.txt",'w')
trinums = open("Drug_User_Triangles_Num_By_Pair.txt",'w')
oxytris = open("Flagged_Drug_Users_Complete_Triangle.txt",'w')
multiples = open("Drug_Triangle_User_Multiple.txt",'w')
num = 0
a = set()
b = set()
count4 = 0
count5 = 0
count6 = 0
count7 = 0
tripplet_thirds = set()
full_triangles = set()
#triangles = set()
triplicates = set('Start')
temp_triplicates = set()
while True:
    line = recips.readline()
    if line == "":
        break
    try:
        pair = set(line.split())
        pair = [int(x) for x in pair]
        pair = set(pair)
        #print pair
        pantry.seek(0)
        a = set()
        b = set()
        tris = set()
        while True:
            peep = pantry.readline()
            if peep == "":
                break
            try:    
                j = json.loads(peep)
                #print pair

                #temp = set(j["user_id"])
                #temp = [int(x) for x in temp]

                #print set(int(j["user_id"]))
                #overlap = pair.intersection(set(int(j["user_id"])))

                #overlap = pair.intersection(temp)
                #print pair
                #print temp
                #print overlap
                #for people in overlap:
                #print j["user_id"]
                if int(j["user_id"]) in pair:
                    if num == 0:
                        a = set(j["follower_ids"]).intersection(set(j["friend_ids"]))
                        #print a
                        num = 1
                    else:
                        b = set(j["follower_ids"]).intersection(set(j["friend_ids"]))
                        #print b
                        num = 0           
            except ValueError:
                pass
        #print a
        #print b
        tris = a.intersection(b)
        if len(a) > 0 and len(b) > 0:
            trinums.write(str(len(tris)))
            trinums.write(str("\n"))
        #print len(a)
        #print len(b)
        #print len(tris)
        if len(tris) > 0:
            count4 = count4 + 1
        if len(a) > 0 and len(b) > 0 and len(tris) == 0:
            count6 = count6 + 1
        for members in tris:
            temp_triplicates = set()
            n = 0
            p1 = 0
            p2 = 0
            for originals in pair:
                file.write(str(originals))
                file.write(str(" "))
                if members in flagged_users:
                    oxytris.write(str(originals))
                    oxytris.write(str(" "))
                    #count7 = count7 + 1
                    full_triangles.add(originals)
                    full_triangles.add(members)  
                    if n == 0:
                        p1 = int(originals)
                    if n == 1:
                        p2 = int(originals)
                n = 1     
            file.write(str(members))
            file.write(str("\n"))
            count5 = count5 + 1
            #triangles.add(int(members))
            equalateral.write(str(members))
            equalateral.write(str("\n"))
            if members in flagged_users:
                oxytris.write(str(members))
                oxytris.write(str("\n"))
                temp_triplicates.add(' '.join([str(members),str(p1),str(p2)]))   
                temp_triplicates.add(' '.join([str(members),str(p2),str(p1)])) 
                temp_triplicates.add(' '.join([str(p1),str(members),str(p2)]))   
                temp_triplicates.add(' '.join([str(p2),str(members),str(p1)]))  
                temp_triplicates.add(' '.join([str(p1),str(p2),str(members)]))   
                temp_triplicates.add(' '.join([str(p2),str(p1),str(members)]))
                #print temp_triplicates
                #print triplicates
                jib = set()
                jib = temp_triplicates.intersection(triplicates)
                if len(jib) == 0: 
                    count7 = count7 + 1
                    for groups in temp_triplicates:
                        triplicates.add(groups)
            if members in triangle_users:
                multi_triangles.add(members)
                multiples.write(str(members))
                multiples.write(str("\n"))
            else:
                triangle_users.add(members)
    except ValueError:
        pass

recips.close()
pantry.close()
file.close()
equalateral.close()
trinums.close()
oxytris.close()

file = open("Complete_Drug_Triangle_Users.txt",'w')
for people in full_triangles:
    file.write(str(people))
    file.write(str("\n"))
file.close

print "Of the Drug-User Pairs, this many have Triangles:"
print count4
print "Totaling to this many Triangles:"
print count5
print "Between this many unique additional users:"
print len(triangle_users)
print "With this many users in more than one triangle"
print len(multi_triangles)
print "Number of Pairs (Both in Graph) and with No Triangles:"
print count6
print "Number of Triangles with 3 Flagged Users:"
print count7
print "Between this Many Different People:"
print len(full_triangles)

graph_data.seek(0)

#print len(triangles)


graph_data.close()