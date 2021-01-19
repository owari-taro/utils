import os


class MyObject:
    def __init___(self):
        self.data=os.urandom(100)

def get_data():
    values=[]
    for _ in range(100):
        obj=MyObject()
        values.append(obj)
    return values

def run():
    deep_values=[]
    for _ in range(100):
        deep_values.append(get_data())
    return deep_values

if __name__=="__main__":
    import gc
    found_objects=gc.get_objects()
    print("before:",len(found_objects))

    #import waste_memory

    hold_reference=run()
    found_objects=gc.get_objects()
    print("after:",len(found_objects))
    for obj in found_objects[:3]:
        print(repr(obj)[:100])