# ARYAINGUZ
# ARYAN 1372
import math
import mpmath


print('! WELCOME TO OUR SCIENTIFIC CALCULATOR ! ')
print('')
print('')
print(f'(note-: please enter accepted input written in parenthisis() below)')


while True: 
    x = input('tell what you want to work on today(trignometic functions, inverse trignometric functions, arithmetic operations, factorial, log, comparison or find greatest no) ').lower()
    
    if x in ['arithmetic operations','arithmetic operation'] :
        a = input('Enter what to find (addition,subtraction,mutliplication,divison,exponential value,square root) ').lower()
        if a in ['addition','add']:       
            xx=int(input('how many numbers you want to add? '))
            add = 0
            for i in range (xx):
                x2=int(input('enter a no '))
                add = x2+add
            print(add) 

        elif a in ['subtraction','subtract']:
            xx=int(input('how many numbers you want to subtract? '))
            sub = int(input('enter a no '))
            for i in range (xx-1):
                x2=int(input('enter a no '))
                sub = sub-x2  
            print(sub)                      
        elif a in ['multiplication','multiply']:
            xx=int(input('how many numbers you want to multiply'))
            mul =1
            for i in range (xx):
                x2=int(input('enter a no '))
                mul = mul * x2
            print(mul)    
        elif a in ['division','divide']: 
            xx=input('how many numbers you want to divide ')
            div=1
            for i in range (xx):
                x2=int(input('enter a no '))
                div = x2//div
            print(div)    
        elif a in ['exponential value','exponential form']:
            xx = int(input('for how many times you want to find exponential form '))
            for i in range (xx):
                x1= int(input('enter the number '))
                x2= int(input('enter exponent or power of the number '))
                exp = x1**x2
                print(exp)  
                print('lets go again ')  

        elif a=='square root':
            xx = int(input('for how many times you want to find square root'))
            for i in range (xx):
                x1 = int(input('enter the number '))
                print(math.sqrt(x1))
                print('lets go again ')  

    elif x in ['trignometric functions', 'trignometric function']:
        pi = math.radians(180) 
        z = input('For what type of value you want to find trignometric functions for(degrees or radians) ').lower()
        a = input('Enter what you want to find(sin,cos,tan,etc):  ').lower()
        if z in ['degrees','degree']:
            z1 = int(input('enter value in terms of degrees '))
            b = math.radians(z1)
        else:
            b =  int(input('enter the value in radians: ')) 

        if a in ['sin','sine']:
            print(math.sin(b))    
        elif a in ['cos','cosine']:
            print(math.cos(b))
        elif a in ['tan','tangent','sin/cos']:
            print(math.tan(b))
        elif a in ['cot','cotan','cotangent','1/tan']:  
            print(mpmath.cot(b))
        elif a in ['sec','secant','1/cos']:
            print(mpmath.sec(b))
        elif a in ['cosec','cosecant','1/sin']:
            print(mpmath.csc(b))      

        

    elif x in ['inverse trignometric functions']:
         pi = math.radians(180) 
         z = input('For what type of value you want to find inverse trignometric functions for(degrees or radians) ').lower()
         a = input('Enter what you want to find(sin inverse, cos inverse, tan inverse,etc):  ').lower()
         if z in ['degrees','degree']:
            z1 = int(input('enter value in terms of degrees '))
            b = math.radians(z1)
         else:
             b =  int(input('enter the value in radians: ')) 

         if a in ['sin inverse','sine inverse']:
                print(math.asin(b))
         elif a in ['cos inverse','cosine inverse']:
                print(math.acos(b))
         elif a in ['tan inverse']:
                print(math.atan(b))
         elif a in ['cot inverse','cotan inverse','cotangent inverse']:  
                print(mpmath.acot(b))
         elif a in ['sec inverse','secant inverse']:
                print(mpmath.asec(b))
         elif a in ['cosec inverse','cosecant inverse']:
                print(mpmath.acsc(b))

    elif x in ['log','logarithm']:
        b = int(input('Enter the number'))
        print(math.log(b))

    elif x in ['factorial']:
        b = int(input('Enter the number'))
        print(math.factorial(b))

    elif x in ['comparison','find greatest number','find greatest number'] :
        xx=int(input('how many numbers you want to compare? '))
        greatest_no = 0
        for i in range(xx):
            x2=int(input('enter a no '))
            if x2>greatest_no:
                greatest_no = x2      
            elif x2<greatest_no:
                greatest_no==greatest_no    
        print('The greatest number here is', greatest_no)
