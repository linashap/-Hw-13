
from options.classes import *
from options.exceptions import *

def ui(x,y,znak):
   
#-----------------------------------------------------------------
    if znak=="+":
        return(m.ad (x,y))
    if znak=="-":
       return( m.sub (x,y))
    if znak=="*":
        if y==0:
            print("Вы умножаете на ноль и ждете неожиданного результата?")
            return(m.mul(x,y))
        else:
            return(m.mul(x,y))
    if znak=="//":
        expchekfloor(x,y)
    if znak=="/":
        expchektruediv(x,y)
    if znak!="/" and znak!="//" and znak!="*" and znak!="-" and znak!="+":
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