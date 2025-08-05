print('هلا بكم في جملة مصر')

list1 = [1,2,3,4]

list1.append(7)

print(list1)


point = (int(input('enter point x: ')), int(input('enter point y: ')))

match point:
    case (1,x):
        print(f'1 , {x}')
    case (0,x):
        print(f'0 , {x}') 
    case _:
         print('list1') 



match list1:
    case [a,b,c,d]:
        print(list1)
    case [a,b]:
        print('list1') 
    case [a,b,c,d]:
        print('list1')
    case [a,b,c,d,z]:
        print('very gooood')   
    case _:
         print('nothing') 
     


