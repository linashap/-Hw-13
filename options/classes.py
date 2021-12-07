from abc import abstractmethod


class Math:
    @abstractmethod
    def ad(x,y):
        pass
    @abstractmethod    
    def sub(x,y):
       pass
    @abstractmethod   
    def mul(x,y):
        pass

    @abstractmethod    
    def floordiv(x,y):
        pass

    @abstractmethod    
    def truediv(x,y):
        pass
class m(Math):

    def ad(x,y):
        rez=float(x)+float(y)
        return(print(f"Sum is {rez}" ))

    def sub(x,y):
        rez=float(x)+(-(float(y)))
        return(print(f"Subtraction is {rez}" ))

    def mul(x,y):
        rez=float(x)*float(y)
        return(print(f"Multiplication is {rez}" ))


    def floordiv(x,y):
        rez=float(x)//float(y)
        return(print(f"celocis delenie is {rez}" ))


    def truediv(x,y):
        rez=float(x)/float(y)
        return(print(f"delenie is {rez}" ))
