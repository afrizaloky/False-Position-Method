#!/usr/bin/env python3
from sympy import var
from sympy import sympify
from math import *
import sys
from prettytable import PrettyTable




#Value from function
def f(value):
        
        res = expr.subs(x, value)
        return res


#False Position Method
def false_position(xu, xl):
        atas = xu*f(xl)-xl*f(xu)
        bawah = f(xl)-f(xu)
        xm = atas/bawah
        return xm

#Input
x = var('x')

try :
        user_input = input("Enter the function (3*x**2+2*x+2) = ")      
        expr = sympify(user_input)
except:
        print("input yang anda masukkan tidak sesuai")
        sys.exit()
        
try:
        xl = float(input("Enter the value of Xl (-10) = "))     
except:
        print("input yang anda masukkan tidak sesuai")
        sys.exit()
        

try:
        xu = float(input("enter the value of xu (15) = "))
except:
        print("input yang anda masukkan tidak sesuai")
        sys.exit()
        

try:
        RAE = float(input("Enter the value of Aproximation Error (0.0001) = "))
except:
        print("input yang anda masukkan tidak sesuai")
        sys.exit()

RAE_now = 100
counter = 0
x_old = 0

#Definition Table
t = PrettyTable()
t.field_names=["i", "xi", "Aproximation Error"]


try:
        #looping
        while RAE<RAE_now:

        
                xm = false_position(xl, xu)
                diff=f(xl)*f(xm)
                if(diff<0):
                        xu=xm
                elif(diff>0):
                        xl=xm
                elif(diff==0):
                        print("True Value = "+str(xm)+".")
                        sys.exit()
                else:
                        print("Program Error")
                        sys.exit()
                if(counter==0):
                        x_new = xm
                        t.add_row([counter, x_new, "-"])
                        counter=counter+1
                        x_old=x_new
                        continue
                x_new = xm
                selisih = abs(x_new-x_old)
                RAE_now = abs(selisih/x_new)
                t.add_row([counter, x_new, RAE_now])
                x_old=x_new
                counter=counter+1
except:
        print("Program Error")
        sys.exit()


print(t)
