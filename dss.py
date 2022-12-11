nums=[]
def sumofnum():
    num=[]
    for i in range(5):
        a=int(input('Enter a positive number: '))
        if a>=0:
            num.append(a)
        else:
            print('U entered a non positive number')
            c=int(input('Enter a positive number: '))
            num.append(c)
    nums.append(num)
    return('The sum of the numbers is', sum(num))
print(sumofnum())
print(nums)