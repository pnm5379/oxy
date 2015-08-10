import networkx as nx
import json
import pickle


flagged_users_file = file("Hand_Flagged_Users.txt")
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
file = open("Oxycontin_Connections.txt",'w')
recips = open("Reciprocal_Oxy_Users.txt",'w')
pantry = open("Reciprocal_Oxy_Social_Graph.json",'w')
nodelings = open("Oxycontin_User_Edges.txt",'w')
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

file = open("Oxycontin_User_Nodes.txt",'w')
file.write(str("Id Label"))
file.write(str("\n"))
for people in connected_users:
    file.write(str(people))
    file.write(str(" Oxy"))
    file.write(str("\n"))
file.close()

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

print "Number of Reciprocal Oxy User-Pairs:"
print count2

print "Between this many users:"
print len(reciprocal_users)

print "Of whom this many Users are in the Graph File:"
print count3

triangle_users = set()
multi_triangles = set()

recips = open("Reciprocal_Oxy_Users.txt",'r')
pantry = open("Reciprocal_Oxy_Social_Graph.json",'r')
file = open("Oxycontin_User_Social_Triangles.txt",'w')
equalateral = open("Oxycontin_User_Triangle_Thirds.txt",'w')
trinums = open("Oxycontin_User_Triangles_Num_By_Pair.txt",'w')
oxytris = open("Flagged_Oxycontin_Users_Complete_Triangle.txt",'w')
multiples = open("Oxycontin_Triangle_User_Multiple.txt",'w')
nonrecip = open("Oxycontin_Non-Reciprocal_Triangles.txt",'w')
multinonrecip = open("Oxycontin_Non-Reciprocal_Tri_Users.txt",'w')
oxynontris = open("Full_Nonreciprocal_Oxycontin_Users.txt",'w')
num = 0
a = set()
b = set()
count4 = 0
count5 = 0
count6 = 0
count7 = 0
tripplet_thirds = set()
full_triangles = set()
c = set()
d = set()
e = set()
f = set()
g = set()
h = set()
count8 = 0
count9 = 0
count10 = 0 
count11 = 0
full_nonrecips = set()
nonrecip_triangle_users = set()
nonrecip_multi_tris_users = set()
triplicates = set('Start')
#triplicates.add(set('Start')))
temp_triplicates = set()
nonrecip_triplicates = set('Start')
#nonrecip_triplicates.add(set('Start'))
temp_nonrecip_triplicates = set()
#triangles = set()
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
        c = set()
        d = set()
        e = set()
        f = set()
        g = set()
        h = set()
        nontris = set()
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
                        c = set(j["follower_ids"])
                        d = set(j["friend_ids"])
                        for dudes in c:
                            e.add(dudes)
                        for dudes in d:
                            e.add(dudes)
                        #e.add(c)
                        #e.add(d)
                        #print a
                        num = 1
                    else:
                        b = set(j["follower_ids"]).intersection(set(j["friend_ids"]))
                        f = set(j["follower_ids"])
                        g = set(j["friend_ids"])
                        for dudes in f:
                            h.add(dudes)
                        for dudes in g:
                            h.add(dudes)
                        #h.add(f)
                        #h.add(g)
                        #print b
                        num = 0           
            except ValueError:
                pass
        #print a
        #print b
        tris = a.intersection(b)
        nontris = e.intersection(h)
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
        if len(nontris) > 0:
            count8 = count8 + 1
        elif len(nontris) == 0 and len(e) > 0 and len(h) > 0:
            count9 = count9 + 1
        for members in nontris:
            temp_nonrecip_triplicates = set()
            n = 0
            p1 = 0
            p2 = 0
            for originals in pair:
                nonrecip.write(str(originals))
                nonrecip.write(str(" "))
                if members in flagged_users:
                    oxynontris.write(str(originals))
                    oxynontris.write(str(" "))
                    #count10 = count10 + 1
                    full_nonrecips.add(originals)
                    full_nonrecips.add(members) 
                    if n == 0:
                        p1 = int(originals)
                    if n == 1:
                        p2 = int(originals)
                n = 1     
            nonrecip.write(str(members))
            nonrecip.write(str("\n"))
            count11 = count11 + 1
            #triangles.add(int(members))
            #equalateral.write(str(members))
            #equalateral.write(str("\n"))
            if members in flagged_users:
                oxynontris.write(str(members))
                oxynontris.write(str("\n"))
                temp_nonrecip_triplicates.add(' '.join([str(members),str(p1),str(p2)]))   
                temp_nonrecip_triplicates.add(' '.join([str(members),str(p2),str(p1)])) 
                temp_nonrecip_triplicates.add(' '.join([str(p1),str(members),str(p2)]))   
                temp_nonrecip_triplicates.add(' '.join([str(p2),str(members),str(p1)]))  
                temp_nonrecip_triplicates.add(' '.join([str(p1),str(p2),str(members)]))   
                temp_nonrecip_triplicates.add(' '.join([str(p2),str(p1),str(members)]))
                #print temp_nonrecip_triplicates
                #print nonrecip_triplicates
                jib = set()
                jib = temp_nonrecip_triplicates.intersection(nonrecip_triplicates)
                if len(jib) == 0:
                    count10 = count10 + 1
                    for groups in temp_nonrecip_triplicates:
                        nonrecip_triplicates.add(groups)
            if members in nonrecip_triangle_users:
                nonrecip_multi_tris_users.add(members)
                multinonrecip.write(str(members))
                multinonrecip.write(str("\n"))
            else:
                nonrecip_triangle_users.add(members)       
    except ValueError:
        pass

recips.close()
pantry.close()
file.close()
equalateral.close()
trinums.close()
oxytris.close()
multinonrecip.close()
oxynontris.close()

file = open("Complete_Oxy_Triangle_Users.txt",'w')
for people in full_triangles:
    file.write(str(people))
    file.write(str("\n"))
file.close

file = open("Complete_Oxy_Nonrecip_Triangle_Users.txt",'w')
for people in full_nonrecips:
    file.write(str(people))
    file.write(str("\n"))
file.close

print "Of the Oxy-User Pairs, this many have Triangles:"
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

print " "
print "Of the Oxy_User Pairs, this many have Nonreciprocal Triangles:"
print count8
print "Totaling to this many Nonreciprocal Triangles:"
print count11
print "Between this many unique additional users:"
print len(nonrecip_triangle_users)
print "With this many users in more than one nonreciprocal triangle"
print len(nonrecip_multi_tris_users)
print "Number of Pairs (Both in Graph) and with No Nonreciprocal Triangles:"
print count9
print "Number of Nonreciprocal Triangles with 3 Flagged Users:"
print count10
print "Between this Many Different People:"
print len(full_nonrecips)

graph_data.seek(0)

#print len(triangles)

graph_data.close()