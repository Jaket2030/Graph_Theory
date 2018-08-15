from graph import Graph
from travel import traveltime
from social import social
import re
import gc
from nondirgraph import NonDirectionalGraph

class Node(object):
  from dict import neighbors
  
  def __init__(self,name, neighbors ):
    self.name=name
    self.neighbors={}
  ##Node represenation 
  def __str__(self):
   return  f' Node: name={self.name} ,neighbors={self.neighbors}'
  ##return the number of neighbors
  def __len__(self):
    return len(self.neighbors)
    
  ##return whether item is a name of a neighbor of self:  
  def __contains__(self, item):
    if item in self.neighbors:
      return True
    else:
      return False
      
  ##return the weight of the neighbor named key
  def __getitem__(self, key):
    return (self.neighbors)
    
  ##the equality operator ,based on the name attribute
  def __eq__(self, other):
    return self.name == other.name 
    
  ##the not equale operator
  def __ne__(self, other):
    return not self.__eq__(other)
    
  ##return whether item is a name of a neighbor of self
  def is_neighbor(self, name):
   if name in self.neighbors:
      return True
   else:
      return False
      
  ##– add name as a neighbor of self
  def update(self, name, weight): 
      if name == self.name:
        return None #not allowd
      else:
          if name not in self.neighbors:
            self.neighbors.update({str(name):weight})
          else:
            self.weight= max( weight,self.weight)
        ##This method should not allow adding a neighbor with the same name as self.
        
  ## remove name from being a neighbor of self
  def remove_neighbor(self, name):
    if name in self.neighbors:
      self.neighbors.pop(name)
    else:
      return None
      
  ## return True if self has no neighbors
  def is_isolated(self):
    if self.neighbors== {'0':0}:
      return True
    else:
      return False
      
#Initiating Dictionaries
Node1=Node("Node1",{})
Node2=Node("Node2",{})
Node3=Node("Node3",{})
Node4=Node("Node4",{})
Node5=Node("Node5",{})
Node6=Node("Node6",{})
Node7=Node("Node7",{})
Node8=Node("Node8",{})
Node9=Node("Node9",{})
Node10=Node("Node10",{})
##importing nodes
Node1.neighbors=Node.neighbors.get("neighbors1")
Node2.neighbors=Node.neighbors.get("neighbors2")
Node3.neighbors=Node.neighbors.get("neighbors3")
Node4.neighbors=Node.neighbors.get("neighbors4")
Node5.neighbors=Node.neighbors.get("neighbors5")
Node6.neighbors=Node.neighbors.get("neighbors6")
Node7.neighbors=Node.neighbors.get("neighbors7")
Node8.neighbors=Node.neighbors.get("neighbors8")
Node9.neighbors=Node.neighbors.get("neighbors9")
Node10.neighbors=Node.neighbors.get("neighbors10")

## Printing the graph
print (Node.neighbors)
##testing
print (Node1.__str__())
print (Node1.name, Node1.neighbors)
print (len(Node1.neighbors))
print (Node1.__len__())
print (Node1.__getitem__('5'))
print (Node1.__contains__('8'))
print (Node1.is_neighbor('5'))
print ("isolated" ,Node7.is_isolated())
Node1.update("Node1",15)
print (Node1.name, Node1.neighbors)
Node1.remove_neighbor('100')
print (Node1.name, Node1.neighbors)
print (len(Node.neighbors))

#finding how many edges are there
from collections import Counter
edgelist=[]
edgelist=list(Node.neighbors.values())
counter = sum((Counter(d) for d in edgelist[1:]), Counter(edgelist[0]))
print ("This is a list of Nodes with edges: " ,list(counter))
print ("This is a list of the edges with their total weight: \n", counter)
edgessum= sum(counter.values())
print ("This is the sum of all Edges weight: " ,edgessum)
mycounter=0
for i in range (0,len(edgelist)):
  for j in range (1,11):
    if str(j) in edgelist[i]:
      mycounter +=1
print ("Total number of Edges :", mycounter )

# Sorting the Nodes by the number of neighbors
my_sort=[]
for n in range (0,len(edgelist)):
  if '0' in edgelist[n].keys() : #checking if a key is zero ,so it wont count a neighbor
    my_sort.append(('Node'+str(n+1),0))
  else:
    my_sort.append(('Node'+str(n+1),len (edgelist[n].keys())))
print ("Sorting the Nodes by number of neighbors \n",sorted(my_sort,key=lambda node:node[1]))
#--------------------------------------------------------------------------------#

#Working with the Graph class
# Inserting the Node objects into the Graph
mygraph= Graph ('mygraph',[])
mygraph.nodes = [Node1,Node2,Node3,Node4,Node5,Node6,Node7,Node8,Node9,Node10]

#testing
mygraph.__str__()
print (mygraph.__len__())
#print (type (Node1))
#print (type (Graph.nodes[1]))
#nodetest= Graph.nodes[1]
#print (type (nodetest))
print (mygraph.__contains__(Node4))
print (mygraph.__getitem__(Node2))

# adding a new graph to graph
mygraph2 = Graph ('mygraph2',[])
mygraph2.nodes=[Node1]
mygraph3 = Graph ('mygraph3',[])
mygraph3.nodes=[Node1,Node2,Node3,Node4,Node5]
print ('length',mygraph2.__len__())
print ('length',mygraph3.__len__())

#print (mygraph3.__contains__(Node1))
Graph.__add__(mygraph2, mygraph3)
print ('length' ,mygraph2.__len__())



#adding a test node to Graph
print (mygraph.__len__())
Node15= Node("Node15",{})
mygraph.__update__(Node15)
print (mygraph.__len__())

#removing a node from Graph
mygraph.remove_node(Node15)
print (mygraph.__len__())

#checking is_edge
print (mygraph.is_edge(Node1,Node8))

#checkng add_edge
mygraph.add_edge(Node1,Node8, 44)
print (mygraph.__getitem__(Node1))

#checking remove_edge
mygraph.remove_edge(Node1,Node8)
print (mygraph.__getitem__(Node1))

#checking get_edge_weight
mygraph.add_edge(Node1,Node8, 44)
print (mygraph.__getitem__(Node1))
print ("weight" ,mygraph.get_edge_weight(Node1,Node8))
mygraph.remove_edge(Node1, Node8) ## removing the test

#checking get_path_weight
print ("total path weight", mygraph.get_path_weight([Node9,Node8,Node7,Node6]))

#checking is_bidirection
print (mygraph.is_bidirection (Node2,Node1))

#checking no_edges
mygraph.no_edges (Node4)


# # #checking is_reachable
# #print (mygraph.is_reachable(Node9,Node4))
#print ( mygraph.is_reachable(Node9,Node5))

#checking find_shortest_path
mygraph.find_shortest_path (Node1,Node3)

# #Sorting the nodes by the number of their reachable nodes
# mygraph.sort_by_reachable()
#-------------------------------------------------------------#
# paths_list = []
# nodes_list = [Node1, Node2, Node3, Node4, Node5]
# for frm_node in nodes_list:
#   for to_node in nodes_list:
#     if frm_node != to_node:
#       min_path = mygraph.find_shortest_path (Node1,Node3)
#       paths_list.append(min_path)
      

#-------------------------------------------------------------#
#Working with the travel file 

travel_neighbors = traveltime() #calling the travel function from travel.py
Node1 = Node("Node1",{})   #Center
Node2 = Node ("Node2", {}) #North
Node3 = Node ("Node3", {}) #South
Node4 = Node ("Node4" ,{})  #East
Node5 = Node ("Node5", {})  #West

#assigning values to the node's neighbors
Node1.neighbors = travel_neighbors.get("Node1")
Node2.neighbors = travel_neighbors.get("Node2")
Node3.neighbors = travel_neighbors.get("Node3")
Node4.neighbors = travel_neighbors.get("Node4")
Node5.neighbors = travel_neighbors.get("Node5")


#creating the travel graph
travel = Graph('travel', [])
travel.nodes= [Node1,Node2,Node3,Node4,Node5]
#testing the travel graph
print ('Graph Length ' ,travel.__len__())
print (travel.__getitem__('Node1'))
#print (mygraph.__getitem__('Node1'))

travel.is_reachable (Node1,Node5)
#--------------------------------------------------------------------------#
#Working with Non-Dir Graph ,testing with 5 nodes
Node1=Node("Node1",{})
Node2=Node("Node2",{})
Node3=Node("Node3",{})
Node4=Node("Node4",{})
Node5=Node("Node5",{})

##importing nodes
Node1.neighbors=Node.neighbors.get("neighbors1")
Node2.neighbors=Node.neighbors.get("neighbors2")
Node3.neighbors=Node.neighbors.get("neighbors3")
Node4.neighbors=Node.neighbors.get("neighbors4")
Node5.neighbors=Node.neighbors.get("neighbors5")

mynondir_graph = NonDirectionalGraph ('mynondir_graph' )
mynondir_graph.nodes= [Node1,Node2]
print (mynondir_graph.__getitem__(Node2))
print (mynondir_graph.__len__())

#testing adding a "doubled" edge
mynondir_graph.add_edge_all (Node2,Node1)
print (mynondir_graph.__getitem__(Node2))
print (mynondir_graph.__getitem__(Node1))
#testing removing a "doubled edge"
mynondir_graph.remove_edge_all (Node1,Node2)
print (mynondir_graph.__getitem__(Node2))
print (mynondir_graph.__getitem__(Node1))
#-----------------------------------------------------------------------#
#working with the social file
social_graph = NonDirectionalGraph ('social_graph' )
#assigning values to the nodes
Manasseh= Node ("Manasseh",{})
Joseph= Node ("Joseph",{})
Naphtali= Node ("Naphtali",{})
Judah= Node ("Judah",{})
Asher= Node ("Asher",{})
Dan= Node ("Dan",{})
Gad= Node ("Gad",{})
Issachar= Node ("Issachar",{})
Ephraim= Node ("Ephraim",{})
Benjamin= Node ("Benjamin",{})
Zebulun= Node ("Zebulun",{})
Simeon= Node ("Simeon",{})
Levi= Node ("Levi",{})
Reuben= Node ("Reuben",{})


#assigning the nodes to the graph
social_graph.nodes = [Manasseh,Joseph,Naphtali,Judah,Asher,Dan,Gad,Issachar,Ephraim,Benjamin,Zebulun,Simeon,Levi,Reuben]
print (social_graph.__getitem__(Dan))


#imporing from social.py
social_list=[]

social_list= social() #getting the list
#print (social_list)
#splitting the lines into words 

lensum=0 #number of friendships
lenlist=[] 

for m in range (0, len(social_list)):
#for m in range (0 ,11):
  social_list[m] = str.split(str(social_list[m]))
  #print (social_list[m])

#checking if friends were added
  if 'became' in social_list[m]:
    frm_name=[]
    to_name=[]
    frm_friend=0
    to_friend=0
    frm_name = social_list[m][0]
    to_name = social_list[m][2]
    
    for i in range (0,len (social_graph.nodes)):
      if frm_name == social_graph.nodes[i].name:
        frm_friend= social_graph.nodes[i]
      if to_name == social_graph.nodes[i].name:
        to_friend= social_graph.nodes[i]
    #adding friends
    #print ("from friend " , frm_friend, "to_friend", to_friend)
    social_graph.add_edge_all (frm_friend,to_friend,weight=1)
    gc.collect()
    #summing the number of neighbors per node
    lensum += 1
    lenlist.append (lensum)
    #print ("lensum",lensum)
  else:
    
#checking if friends were removed
    if 'cancelled' in social_list[m]:
      frm_name = social_list[m][0]
      to_name = social_list[m][2]
      
      for i in range (0,len (social_graph.nodes)):
        if frm_name == social_graph.nodes[i].name:
          frm_friend= social_graph.nodes[i]
        if to_name == social_graph.nodes[i].name:
          to_friend= social_graph.nodes[i]
      #removing friends
      social_graph.remove_edge_all (frm_friend,to_friend)
      gc.collect()
      # removing from the friendships sum
      lensum -= 1
      lenlist.append (lensum)
      


#printing the latest satus
for i in range (0 ,len (social_graph.nodes)):
  print (social_graph.nodes[i])
#printing the highest number of simultanous friendships
print ("The highest number of simultanous friendships" ,max (lenlist))

#recommending a friend
social_graph.suggest_friend(Manasseh)

#the maximal path
#social_graph.find_shortest_path (Manasseh,Levi)