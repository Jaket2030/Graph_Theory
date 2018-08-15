from dict import neighbors
import re 
class Graph(object):

  def __init__(self,name,nodes=[]):
    self.name=name
    #The nodes will be inserted in main 

#prints the description of all the nodes in the graph
  def __str__(self):
    print (self.nodes)
    
#returns the number of nodes in the graph  
  def __len__(self): 
    return len(self.nodes)
  
#returns True in two cases: (1) If key is a string, then if a node called key is in self, and (2) If key is a Node, then if a node with the same name is in self.
  def __contains__(self, key):
    if  type(key) is str:
      for i in range (0 , len (self.nodes)):
       if key in str(self.nodes[i]) :
        return True
    else:    
      if key in self.nodes:  
        return True
      else:
        return False

#returns the Node object whose name is name  
  def __getitem__(self, name):
    if  type(name) is str:
      for i in range (0 , len (self.nodes)):
       if name in str(self.nodes[i]) :
        return self.nodes[i]
    else:
      for i in range (0, len (self.nodes)):
        try:
         if name == self.nodes[i]:
          return self.nodes[i]
        except NameError as error:
          print (error)
  
#returns a new Graph object that includes all the nodes and edges of self and other
  def __add__(self, other):
    for i in range (0, len (other.nodes)):
      if self.__contains__(str(other.nodes[i])) :
        print ("not allowed" ,other.nodes[i])
      else:
    #   if other not in self.nodes:
        self.nodes.append (other.nodes)
         
        
#adds a new node to the graph        
  def __update__(self, other):
    if self.__contains__(other) == True:
      return None #not allowd
    else:
      if other not in self.nodes:
        self.nodes.append({str(other)})

#removes the node name from self.
  def remove_node(self,name):
    for i in range (0, len (self.nodes)):
      if str(name) in str(self.nodes[i]):
        del self.nodes [i]
        print ('removed' ,name)
    else:
      return None

#returns True if to_name is a neighbor of frm_name
  def is_edge(self, frm_name, to_name):
#extracting only Node number from the Node name
    nodenumber= re.findall (r'\d+',to_name.name)
    if frm_name is None :
      frm_node = self.__getitem__(frm_name)
      mylist= list(frm_node.neighbors.keys())
    else:  
      mylist= list(frm_name.neighbors.keys())
    if str (nodenumber[0]) in str(mylist):
      return True
    else:
      return False
   
#adds an edge making to_name a neighbor of frm_name.  
  def add_edge(self, frm_name, to_name, weight):
    if self.is_edge (frm_name,to_name) == True:
      print ("already there")
      return None #not allowd
    else:
      #getting just the number of the node
      frm_nodenumber= re.findall (r'\d+',frm_name.name)
      to_nodenumber= re.findall (r'\d+',to_name.name)
      #formating this to be like in the neighbors list
      tmp='neighbors'+str(frm_nodenumber[0])
      if tmp in neighbors.keys() :
         neighbors[str(tmp)].update ({str(to_nodenumber[0]):weight})
      else:
        return None
  
#removes to_name from being a neighbor of frm_name.
  def remove_edge(self, frm_name, to_name):
    if self.is_edge (frm_name,to_name) is not True:
      print ("not there ,cannot remove")
      return None #not allowd
    else:
      #getting just the number of the node
      frm_nodenumber= re.findall (r'\d+',frm_name.name)
      to_nodenumber= re.findall (r'\d+',to_name.name)
      #formating this to be like in the neighbors list
      tmp='neighbors'+str(frm_nodenumber[0])
      if tmp in neighbors.keys() :
         neighbors[str(tmp)].pop (str(to_nodenumber[0]))
      else:
        return None
      
#returns the weight of the edge between frm_name and to_name.  
  def get_edge_weight(self, frm_name, to_name):
    if self.is_edge (frm_name,to_name) is not True:
      print ("not there ,no weight")
      return None #not allowd
    else:
      #getting just the number of the node
      frm_nodenumber= re.findall (r'\d+',frm_name.name)
      to_nodenumber= re.findall (r'\d+',to_name.name)
      #formating this to be like in the neighbors list
      tmp='neighbors'+str(frm_nodenumber[0])
      #getting the weight
      theweight= neighbors[str(tmp)].get (str(to_nodenumber[0]))
      return (theweight)
    
#returns the total weight of the given path, where path is an
#iterable of nodes’ names.  
  def get_path_weight(self,path):
    self.path=path
    if any (self.path) is not True:
      print ("Path is empty")
      return None
    else:
      list (path)
      #calculating path
      path_weight=0
      for i in range (0 ,len (path)-1):
        #if path[i] is str:
        path[i] = self.__getitem__(path[i])
        path[i+1]= self.__getitem__(path[i+1])
        if self.is_edge (path[i],path[i+1]):
          path_weight +=  self.get_edge_weight (path[i],path[i+1])
      return (path_weight)
  
  #checks if two nodes are bi-directional
  def is_bidirection (self,frm_name,to_name):
    
    to_node = self.__getitem__(to_name)
    frm_node = self.__getitem__(frm_name)
    to_nodenumber= re.findall (r'\d+',to_node.name)
    frm_nodenumber= re.findall (r'\d+',frm_node.name)
    if str(to_nodenumber[0]) in frm_node.neighbors.keys() and\
    str(frm_nodenumber[0]) in to_node.neighbors.keys():
      return True
    else:
      return False
  
  #checks if a Node has no edges
  def no_edges(self,to_name):
    if to_name is str :
      to_name = self.__getitem__(to_name)
    else:
      to_node = self.__getitem__(to_name)
      nodenumber= re.findall (r'\d+',to_name.name)
      mylist= list(neighbors.values())
    if str (nodenumber[0]) not in str(mylist):
      return True
    else:
      return False
 
 #setting a global variable for path 
  global path
  path=[]
    #returns True if to_name is reachable from frm_name.
  def is_reachable(self, frm_name, to_name):
    
    #assigning values to the recursive function
    to_node = self.__getitem__(to_name)
    frm_node = self.__getitem__(frm_name)
    print ("trying to reach from ", frm_node, "to", to_node)
    print (str(to_node.name))
    if (str(to_node.name)).isdigit() is not True:
      to_nodenumber= re.findall (r'\d+',to_node.name)
      print (to_nodenumber)
    frm_nodenumber= re.findall (r'\d+',frm_node.name)
    print ("from number ", frm_nodenumber)
    path.append (frm_nodenumber)
    #print ("from path ", path)
    
    #cheking if the frm node has no neighbors at all
    if '0' in frm_node.neighbors.keys():
      print ("no neighbors ,not possible")
      return False
      #return path
    else:
    #cheking if the to_name has no edges at all
      if self.no_edges (to_name) is True:
        print ("no edges ,not possible")
        return False
      else:
        if str(to_nodenumber[0]) in frm_node.neighbors.keys():
          print (to_name, "is reachable from ",frm_name)
          #adding the path for a later use
          path.append(to_nodenumber[0])
          print ("path" ,path)
          return True, path
        else:
          
          neighbors_list= list (frm_node.neighbors)
          print (neighbors_list[0])
          for i in range (0 ,len (neighbors_list)):
            
            add_node="Node"+ str(neighbors_list[i])
            print (add_node)
             #cheking if its bi-directional ,not to get into inifinite loop
            if self.is_bidirection (add_node,frm_node) is True:
              print ("bi-directional")
              continue 
            # running recursive function
            self.is_reachable (add_node,to_name)
  
#returns the path from frm_name to to_name which has the minimum total weight.
  def find_shortest_path(self, frm_name, to_name):
    
    if self.is_reachable (frm_name,to_name) is not False:
      sliced_list=[]
      add_node_list=[]
      position=[]
      total_path_weight=[]
      shortest_path=[]
      for i in range (0, len (path)):
        add_node = "Node" + path[i][0]
        add_node_list.append(add_node)
      #for j in range (0,1):  
      print (add_node_list)
      new_list=[]
      for i in range (0 ,len (add_node_list)):
  #finding how many paths there are
        if  add_node_list[i] ==  str(to_name.name):
          start=0
          position.append(i)
  #slicing the original list into paths        
      for j in range (0 ,len (position)):
        sliced_list.append ( add_node_list[start:position[j]+1])
        start= position [j]+1
    # adding the frm_node to the other paths which do not contain it
      for j in range (1, len(position)):  
        sliced_list[j].insert (0,add_node_list[0])  
      print (sliced_list)
    #finding the weight for each path
      for i in range (0 ,len (position)):
        total_path_weight.append(self.get_path_weight (sliced_list[i]))
      print (total_path_weight)
      
   #finding the minimum path 
      if len (total_path_weight) is 0:
        print ("No path available")
        return (0)
      else:
        min_path= min (total_path_weight)
        for m in range (0 ,len (total_path_weight)):
          if total_path_weight[m] == min_path:
            for i in range (0, len (sliced_list[m])):
              shortest_path.append(sliced_list[m][i].name)
      print (shortest_path, min_path)
      return (shortest_path,min_path)
    
    #Sort the nodes by the number of their reachable nodes.
  def sort_by_reachable (self):
   
    mycounter=0
    counter=[]
  #counting how many reachable nodes each node has   
    for i in range (0 ,len (neighbors)):
      for j in range (1, len (neighbors)):
        from_node= self.nodes[i]
        to_node= self.nodes[j]
        if self.is_reachable (from_node,to_node) is not False:
          mycounter +=1
      counter.append(mycounter)
    counter.sort()
    print ("Nodes sorted by reachable nodes", counter)
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  