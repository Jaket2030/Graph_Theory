from dict import neighbors
from graph import Graph
import re
class NonDirectionalGraph (Graph):
  def __init__(self,name,nodes=[]):
    self.name= name
    
  #adds an edge making to_name a neighbor of frm_name and vice versa.  
  def add_edge_all (self, frm_name, to_name, weight=1):
      #getting just the number of the node
      frm_nodenumber= re.findall (r'\d+',frm_name.name)
      to_nodenumber= re.findall (r'\d+',to_name.name)
      #print ("here in the func", frm_name,to_name)
      #print (frm_name.name,to_name.name)
      ##print ("adding" ,frm_name.name,to_name.name)
      #checking in case this is not in the format of "Node1.."
      
      if not frm_nodenumber and not to_nodenumber :
        for n in range (0, len (self.nodes)):
          if str(frm_name.name) in self.nodes[n].name:
            self.nodes[n].neighbors.update ({str(to_name.name):weight})
            ##print ("friend added",to_name.name)
        for m in range (0, len (self.nodes)):
          if str(to_name.name) in self.nodes[m].name:
            self.nodes[m].neighbors.update ({str(frm_name.name):weight})
            ##print ("and vice versa")
          
        return None
      else:
      #formating this to be like in the neighbors list
        tmp='neighbors'+str(frm_nodenumber[0])
        if tmp in neighbors.keys() :
          neighbors[str(tmp)].update ({str(to_nodenumber[0]):weight})
        #also adding the other direction since this is both directions
          tmp1='neighbors'+str(to_nodenumber[0])
          neighbors[str(tmp1)].update ({str(frm_nodenumber[0]):weight})
      
      return None

        
  #removes to_name from being a neighbor of frm_name.
  def remove_edge_all(self, frm_name, to_name):
      #getting just the number of the node
      frm_nodenumber= re.findall (r'\d+',frm_name.name)
      to_nodenumber= re.findall (r'\d+',to_name.name)
      #print ("removing" ,frm_name.name,to_name.name)
      #checking in case this is not in the format of "Node1.."
      if not frm_nodenumber and not to_nodenumber :
        for i in range (0, len (self.nodes)):
          if str(frm_name.name) in self.nodes[i].name:
            #del self.nodes[i].neighbors [str(to_name.name)]
            self.nodes[i].neighbors.pop (str(to_name.name))
            ##print ("friend removed")
          if str(to_name.name) in self.nodes[i].name:
            self.nodes[i].neighbors.pop (str(frm_name.name))
            ##print ("and vice versa")
      else:      
      #formating this to be like in the neighbors list
        tmp='neighbors'+str(frm_nodenumber[0])
        tmp1='neighbors'+str(to_nodenumber[0])
        if tmp in neighbors.keys() :
          neighbors[str(tmp)].pop (str(to_nodenumber[0]))
          neighbors[str(tmp1)].pop (str(frm_nodenumber[0]))
      
      return None
      
 #this method will suggest a friend list based on common friends 
  def suggest_friend(self, node_name):
    #a list representing all the friends
    shared=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    #finding friends
    for i in range (0 ,len (self.nodes)):
      #removing node_name from the recommend_list ,to aviod recommending itself
      if self.nodes[i] == node_name:
        shared[i] = 0
        continue
      else:
  #checking how many friends corelate
        shared_items=(set(self.nodes[i].neighbors.items()) & set(node_name.neighbors.items()))
        shared[i]= len(shared_items)
        #print (shared[i])
    #the positions of "maxes" in the list 
    max_positions= [i for i, x in enumerate(shared) if x == max(shared)]
    print ("recommended friends" ,max_positions)
    
    for i in range (0,len (self.nodes)):
      for m in range (0,len (max_positions)):
    #checking i'm not recommending a friend who's already on the friends list
        if self.nodes[max_positions[m]].name not in node_name.neighbors:
          print ("recommended: ", self.nodes[max_positions[m]].name)
          return (self.nodes[max_positions[m]].name)
        
      
 
      