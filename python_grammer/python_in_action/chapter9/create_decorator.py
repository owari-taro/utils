def decol(f):
    print("decol colled")

    def wrapper():
        print("before exec")
        v = f()
        print("after exec")
        return v
    return wrapper

@decol
#functional decorator ,decol get func as an argument and //////
def func():
    print("exec")
    return 1


if __name__=="__main__":
    func()