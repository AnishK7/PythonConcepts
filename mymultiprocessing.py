import time
import multiprocessing


# checking my ram limit
def boom1(*args):
    #args[1][0] = 5**10
    #args[2].value = 100.5

    #for i in args[0]:
    #    queue.put(i)
    
    for i in range(100):
        args[4].acquire()
        args[2].value = args[2].value + 1
        args[4].release()
    
def boom2(*args):
    for i in range(100):
        args[2].acquire()
        args[1].value = args[1].value - 1
        args[2].release()
        
def boom3(*args):
    result = 0
    for i in range(100000000):
        for j in range(100):
            result = result + j
    return result

def boom4(*args):
    print(2**10)


    
if __name__=="__main__":
    array = [1,2,3,4,5]
    result = multiprocessing.Array('i', len(array)) # Shared memory
    value = multiprocessing.Value('d', 0.0)
    queue = multiprocessing.Queue()
    lock = multiprocessing.Lock()
    pool = multiprocessing.Pool()

    
    p1 = multiprocessing.Process(target=boom1, args=(array, result, value, queue, lock)) # Cannot pass kwargs
    p2 = multiprocessing.Process(target=boom2, args=(array,value, lock))
    #p3 = multiprocessing.Process(target=boom3, args=(array,))
    #p4 = multiprocessing.Process(target=boom4, args=(array,))
    #print('After initialization', result[:])
    p1.start()
    p2.start()
    #p3.start()
    #p4.start()
    #print('After start', result[:])
    
    p1.join()
    p2.join()
    #p3.join()
    #p4.join()

    
    #print('After join', result[:], value.value)

    #while queue.empty() is False:
    #    print'Queue get',(queue.get())

    #print('Value after done', value.value)

    print(pool.map(boom3, range(10)))
