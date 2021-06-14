#author Vixtor61
import math

def f1(*args):
    return  args[0]

def f2(*args):
    return  math.e**(args[1] /args[0])

def f3(*args):
    return  2*args[1]*math.sin(args[0]) + (math.cos(args[0]))**2

def f4(*args):
    return args[0]**2 + args[1]**2 + args[2]

def simpson(fun,limits,Ns):
    niter = len(limits)/2
    return simpNested(fun,Ns,0,niter,limits)


def simpNested(fun,Ns,i,nIter,limits,*args):
    #print(type(Ns))
    currentN = Ns[i]
    nhalf = int(currentN/2)
    iterSum = 0 
    limA = limits[2*i](*args) 
    limB = limits[2*i+1](*args) 
    currentH =( (limB  - limA) / currentN)

    if(i == nIter-1):
        firstSum= 0
        for j in range(1,nhalf):
            arg= limA +((2*j))*currentH
            firstSum  +=  fun(*args,arg)

        secondSum=0
        for j in range(1,nhalf+1):
            arg= limA +((2*j -1))*currentH
            secondSum +=  fun(*args,arg)

        iterSum = fun(*args,limA)   + 2 * firstSum  + 4 * secondSum  + fun(*args,limB)
        return (currentH/3)*iterSum

    else:
        i+=1

        firstSum= 0
        for j in range(1,nhalf):
            arg= limA +((2*j))*currentH
            firstSum += 2* simpNested(fun,Ns,i,nIter,limits,*args,arg) 

        secondSum= 0
        for j in range(1,nhalf+1):
            arg= limA +((2*j -1))*currentH
            secondSum += 4 *  simpNested(fun,Ns,i,nIter,limits,*args,arg) 
        
        iterSum = simpNested(fun,Ns,i ,nIter,limits,*args,limA) + firstSum + secondSum + simpNested(fun,Ns,i,nIter,limits,*args,limB)
        return (currentH/3)*iterSum
        

def main():
    limits = [lambda *x: 0 , lambda *x: 4]
    limits2 = [lambda *x: 0.1 , lambda *x: 0.5, lambda *x: x[0] **3 ,lambda *x: x[0]** 2]
    limits3 = [lambda *x: 0 , lambda *x: math.pi/4 , lambda *x: math.sin(x[0]) ,lambda *x: math.cos(x[0])]
    limits4 = [
            lambda *x: 2.0 ,                    lambda *x: 4.0 ,
            lambda *x: x[0] - 1.0 ,             lambda *x: x[0] +6.0 ,
            lambda *x: -2.0,                    lambda *x: 4.0 + x[1]**2.0 
            ]

    narray = [10,10,10]
    #Test Functions
    print("res: " + str(simpson(f1,limits,narray)))
    print("res: " + str(simpson(f2,limits2,narray)))
    print("res: " + str(simpson(f3,limits3,narray)))
    print("res: " + str(simpson(f4,limits4,narray)))
main()

