for i in range(1,21):
    print(i , ' ' , end='')
else:
    print("LOOOL")        


countries = { 'Iraq' : 'Baghdad' ,'KSA' : 'Reyadh','Egypt' : 'Cairo','Syria' : 'demascus','UAE' : 'Dubai'}

print('\n\n')

for i , y in countries.items():
    print(i , ':' , y)

print('\n\n')  

i=[1,3,5,6,10]

print(len(i))


while len(i) > 0 :
    print(i)
    del i[len(i) - 1]
else:
    print("iiiiiiiiiiiiiiii")
    print(i)