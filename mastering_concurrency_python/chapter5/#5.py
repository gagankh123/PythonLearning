import  time
UPDATE_INTERVAL  =  0.01
def  process_requests(threads,  timeout=5):
    def  alive_count():
        alive  =  [1  if  thread.isAlive()  else  0  for  thread  in  threads]
        return  sum(alive)
    while  alive_count()  >  0  and  timeout  >  0:
        timeout  -=  UPDATE_INTERVAL
        time.sleep(UPDATE_INTERVAL)
    for  thread  in  threads:
        print(thread.result)

import  threading
import  requests
class  MyThread(threading.Thread):
    def  __init__(self,  url):
        threading.Thread.__init__(self)
        self.url  =  url
        self.result  =  f'{self.url}:  Custom  timeout'
    def  run(self):
        res  =  requests.get(self.url)
        self.result  =  f'{self.url}:  {res.text}'

urls  =  [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=4000',
    'http://httpstat.us/200?sleep=20000',
    'http://httpstat.us/400'
]
start  =  time.time()
threads  =  [MyThread(url)  for  url  in  urls]
for  thread  in  threads:
    thread.setDaemon(True)
    thread.start()
process_requests(threads)
print(f'Took  {time.time()  -  start}  seconds')
print('Done.')