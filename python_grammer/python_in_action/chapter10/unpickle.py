from concurrent.futures import ProcessPoolExecutor, wait


test=lambda :1

def main(test):
    with ProcessPoolExecutor() as e:
        futures = e.submit(test)
        done, not_done = wait([futures])
    print(futures.result())



if __name__=="__main__":
    main()
