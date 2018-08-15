# This function will be used to accsess the CSV files and parse them

def traveltime():
  from datetime import datetime, timedelta
  import numpy as np
  # first the travelsew file
  with open ('travelsew.csv','r',encoding='utf8') as travelsew :
    mylist=[]
    for lines in travelsew:
      tmp = lines.replace('\n','')
      tmp = tmp.split(',')
      mylist.append(tmp)
      
# Running through the list and getting the time delta and the direction for each row. Ignoring raws with missing data
  overall=[]
  print ("total input lines" ,len (mylist))
  
  #Formating the data into datetime format and also retreiving the direction. Creating a new dict with (direction:duration)
  
  for i in range (1, len (mylist) ):
    try:
      duration=(datetime.strptime(str(mylist[i][3]), '%d/%m/%Y %Hh%Mm')- datetime.strptime(str(mylist[i][1]), '%d/%m/%Y %Hh%Mm'))
      direction= (mylist[i][0] +mylist[i][2])
      overall.append ({direction:duration})
      
  #ignoring faulty lines
    except ValueError :
      pass
    except IndexError:
      pass
  
  # Total lines after removing faulty lines:
  print ("Overall lines" ,len(overall))
  
  #spliting the data into 3 seperate lists ,per direction:
  
  CenterWest=[]
  EastSouth=[]
  CenterNorth=[]
  CenterWest_sum=0
  #print (overall[0].keys())
  for i in range (0, len( overall)):
    if 'CenterWest' in overall[i].keys():
      CenterWest.append(list(overall[i].values()))
    if 'EastSouth' in overall[i].keys():
      EastSouth.append(list (overall[i].values()))
    if 'CenterNorth' in overall[i].keys():
      CenterNorth.append(list (overall[i].values()))
      
  #Calculating the average time per direction
  CenterWest = np.mean (CenterWest)
  EastSouth =  np.mean (EastSouth)
  CenterNorth = np.mean (CenterNorth)
  
  print ('Mean CenterWest', CenterWest)
  print ('Mean EastSouth', EastSouth)
  print ('Mean CenterNorth', CenterNorth)
  #---------------------------------------------------------------#
  
   # Now the travelswe file
  with open ('travelswe.csv','r',encoding='utf8') as travelswe :
    mylist=[]
    for lines in travelswe:
      tmp = lines.replace('\n','')
      tmp = tmp.split(',')
      mylist.append(tmp)
      
# Running through the list and getting the time delta and the direction for each row. Ignoring raws with missing data
  overall=[]
  print ("total input lines" ,len (mylist))
  
  #Formating the data into datetime format and also retreiving the direction. Creating a new dict with (direction:duration). Note the differnt time format from the previous file
  for i in range (1,len (mylist)):
    try:
      duration=(datetime.strptime(str(mylist[i][3]), '%I:%M:%S%p ; %b %d %y')- datetime.strptime(str(mylist[i][1]), '%I:%M:%S%p ; %b %d %y'))
      direction= (mylist[i][0] +mylist[i][2])
      overall.append ({direction:duration})
      
  #ignoring faulty lines
    except ValueError:
      pass
    except IndexError:
      pass
  
  # Total lines after removing faulty lines:
  print ("Overall lines" ,len(overall))
  
  #spliting the data into 6 seperate lists ,per direction:
  CenterEast=[]
  CenterSouth=[]
  NorthCenter=[]
  SouthEast=[]
  WestCenter=[]
  WestNorth=[]
  
  for i in range (0, len( overall)):
    if 'CenterEast' in overall[i].keys():
      CenterEast.append(list(overall[i].values()))
    if 'CenterSouth' in overall[i].keys():
      CenterSouth.append(list (overall[i].values()))
    if 'NorthCenter' in overall[i].keys():
      NorthCenter.append(list (overall[i].values()))
    if 'SouthEast' in overall[i].keys():
      SouthEast.append(list (overall[i].values()))
    if 'WestCenter' in overall[i].keys():
      WestCenter.append(list (overall[i].values())) 
    if 'WestNorth' in overall[i].keys():
      WestNorth.append(list (overall[i].values()))  
      
  #Calculating the average time per direction
  CenterEast= np.mean (CenterEast)
  CenterSouth= np.mean (CenterSouth)
  NorthCenter=np.mean (NorthCenter)
  SouthEast=np.mean (SouthEast)
  WestCenter=np.mean (WestCenter)
  WestNorth=np.mean (WestNorth)
  
  
  print ('Mean CenterEast:', CenterEast)
  print ('Mean CenterSouth:', CenterSouth)
  print ('Mean NorthCenter:',  NorthCenter)
  print ('Mean SouthEast:',  SouthEast)
  print ('Mean WestCenter:', WestCenter)
  print ('Mean WestNorth:',  WestNorth)
 
 #assigning the values to a dictionary
  Center = '1' #'Node1'
  North = '2'  #'Node2'
  South = '3'  #'Node3'
  East = '4'   #'Node4'
  West = '5'   #'Node5'
 
  travel_neighbors ={
  'Node1' : {'5':CenterWest,'2':CenterNorth,'4':CenterEast,'3':CenterSouth},
  'Node2' : {'1':NorthCenter},
  'Node3' : {'4':SouthEast},
  'Node4' : {'3':EastSouth},
  'Node5' : {'1':WestCenter,'2':WestNorth}
  }
 
 
  
  # travel_neighbors ={
  # 'Center' : {'West':CenterWest,'North':CenterNorth,'East':CenterEast,'South':CenterSouth},
  # 'North' : {'Center':NorthCenter},
  # 'South' : {'East':SouthEast},
  # 'East' : {'South':EastSouth},
  # 'West' : {'Center':WestCenter,'North':WestNorth}
  # }
  
  
  
  return(travel_neighbors)
  
  
  
  
  