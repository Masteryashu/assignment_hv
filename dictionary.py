x=open('mydata.txt','a')
car={}
for i in range(4):
    brand=input('Enter the car brand: ')
    car[brand]=input('Enter the colur of car: ')
print(car)
print(car,file=x)
x.close()