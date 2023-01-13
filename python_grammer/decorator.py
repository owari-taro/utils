from collections import defaultdict
from functools import partial,wraps
class EventRegistry:
    def __init__(self):
        self.registry = defaultdict(list)
    
    def on(self,*events):
        def _on(function):
            for event in events:
                self.registry[event].append(function)
            return function
        return _on

    def fire(self,event,*args,**kwargs):
        for function in self.registry[event]:
            function(*args,**kwargs)
        


events=EventRegistry()
@events.on("success","error")
def teardown(value):
    print(f"tearing down got:{value}")

@events.on("success")
def success(value):
    print(f"successfully executed {value}")
    
events.fire("non-existing","nothing to seehere")
events.fire("success","everything is fine")
 

def add(func=None,*,x=1):
    if func is None:
        return partial(add,x=x)
    @wraps(func)
    def wrapped(*args,**kwargs):
        return func(*args,**kwargs)+x

    return wrapped


@add(x=123)
def hoge(x,y):
    return x+y

print(hoge(100,100))