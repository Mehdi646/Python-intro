def Addition (x,y):
    z=x+y
    print (z)
    if (z>0):
        print ('Positive')
    if (z<0):
        print ('Negative')

def Addition (x,y):
    
  
    z=float(x)+float(y)
    e=round(z,2)
    print (e)


    z=float(x)-float(y)
    e=round(z,2)
    print (e)


    z=float(x)*float(y)
    e=round(z,2)
    print (e)

    z=float(x)/float(y)
    e=round(z,2)
    print (e)
    x=  'mehdi'
    y=    'bernoussi'
    z= (x+' '+y)
    print (z)

def Soustraction (x,y):
    z=x-y
    print (z)  
    if (z<0):
        print ("Negative")
    if (z>0):
        print ('Positive')
    

def Multiplication (x,y):
    z=x*y
    print(z)
    if (z>0):
        print ('Positive')
    if (z<0):
        print ('Negative')
def Division (x,y):
    z=x/y
    print (z)
    if (z<0):
        print ('Negative')
    else:
        print ('Positive')


if __name__ == '__main__': 

    
    print ('Welcome in my first calculation')
    # print ('1= Addition \n 2= Soustraction \n 3=Multiplication \n 4= Division'  ) 
    choose = input ('Enter a your operation: ' )
    number_one=int(input ('Enter a number:'))
    number_two=int (input('Enter a number: '))
    if (choose)=='+':
        print (number_one+number_two)
    if (choose)=='-':
        print (number_one-number_two)
    if (choose)=='x':
        print (number_one*number_two)
    if (choose)=='/':
        print (number_one/number_two)
