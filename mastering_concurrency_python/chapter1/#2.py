from  timeit  import  default_timer  as  timer
import concurrent.futures

def  f(x):
    return  x  *  x  -  x  +  1

start  =  timer()
result  =  3
for  i  in  range(20):
    result  =  f(result)
print('Result  is  very  large.  Only  printing  the  last  5  digits:',  result  %  100000)
print('Sequential  took:  %.2f  seconds.'  %  (timer()  -  start))

def  concurrent_f(x):
    global  result
    result  =  f(result)

result  =  3
with  concurrent.futures.ThreadPoolExecutor(max_workers=20)  as  exector:
    futures  =  [exector.submit(concurrent_f,  i)  for  i  in  range(20)]
    _  =  concurrent.futures.as_completed(futures)
print('Result  is  very  large.  Only  printing  the  last  5  digits:',  result  %  100000)
print('Concurrent  took:  %.2f  seconds.'  %  (timer()  -  start))