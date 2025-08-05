import json

with open(r"M:\Study\SELF LEARNING\Ai\Hsoub_Ai_Course\Python\Code\fileOperation\myData.json", 'r') as jfile:
    data_list = json.load(jfile)


# Example of accessing the data_list 

for index , user in enumerate(data_list) :


         print(index+1, ":", data_list[index]["myData"]["name"] , ":")

         try:
             print( "ID => ", data_list[index]["myData"]["ID"] ,)
         except KeyError:
             pass

         print( "age => ", data_list[index]["myData"]["age"] ,)
         print( "email => ", data_list[index]["myData"]["email"] ,)
         print( "address => ", data_list[index]["myData"]["address"]["street"] , ",", data_list[index]["myData"]["address"]["city"] , ",", data_list[index]["myData"]["address"]["state"] , ",", data_list[index]["myData"]["address"]["zip"] , "\n" )


print("=========================================") 
print("\t Total users:", len(data_list))
print("=========================================") 


