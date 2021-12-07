from options.classes import *



def expchekfloor(x,y):
    try:
            float(x)//float(y)
    except ZeroDivisionError as err:
            print(f"Делить на ноль это грех,{err}")
    else:
        return(m.floordiv(x,y))


def expchektruediv(x,y):
    try:
            float(x)/float(y)
    except ZeroDivisionError as err:
            print(f"Делить на ноль это грех,{err}")
    else:
        return(m.truediv(x,y))

class NEtotsimvil(Exception):
        def __init__(self, mess="Этот символ не обрабатывается нашим калькулятором") -> None:
                super().__init__(mess)
            
class Nottipe(Exception):
        def __init__(self, mess="Вы вввели не число") -> None:
            super().__init__(mess)