from graph import Graph
from nondirgraph import NonDirectionalGraph
# This function will be used to accsess the Social file and parse it
def social():
  
  # first the social file
  with open ('social.txt','r',encoding='utf8') as social :
    mylist=[]
    for lines in social:
      tmp = lines.replace('\n','')
      mylist.append(tmp)
  
  return (mylist)
  