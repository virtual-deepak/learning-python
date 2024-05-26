class Greeter:
    def say_hello(self):
        print('Hello world')
    
    def say_hello(self):
        print('Hello pythonista!')

    #def say_hello(self, name): # Cannot have this. Python does not support overloading!
    #    print('Hello {a}')

    def __str__(self):
        return "This is from __str__"
    
    def __repr__(self): # ==> Should return a format description of creating an object  
        return "Greeter()"

g = Greeter()
g.say_hello() # Output => Hello pythonista! The last function of the same name in the sequence wins.
print(g) # Output => This always calls __str__
print(eval(repr(g)).say_hello()) 