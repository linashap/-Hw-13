
from options.func import *
from options.exceptions import *

def ui(x,y,znak):
   
#-----------------------------------------------------------------
    if znak=="+":
        return(ad (x,y))
    if znak=="-":
       return( sub (x,y))
    if znak=="*":
        if y==0:
            print("Вы умножаете на ноль и ждете неожиданного результата?")
            return(mul(x,y))
        else:
            return(mul(x,y))
    if znak=="//":
        return(expchekfloor(x,y))
    if znak=="/":
        return(expchektruediv(x,y))
    else:
        raise(NEtotsimvil)

def check(x,y):
    try:
        float(x)
    except ValueError:
        raise Nottipe
    try:
        float(y)
    except ValueError:
        raise Nottipe