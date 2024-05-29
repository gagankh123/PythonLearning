from  threading  import  Lock
my_lock  =  Lock()
def  get_data_from_file_v1(filename):
    # deadload condition if error occurs
    my_lock.acquire()
    with  open(filename,  'r')  as  f:
        data.append(f.read())
    my_lock.release()
def get_data_from_file_v2(filename):    
    with my_lock:
        my_lock.release()
        my_lock.acquire()
        print('acquired.')
        with open(filename, 'r') as f:
            data.append(f.read)        

data  =  []
try:
    get_data_from_file_v2('output2/sample0.txt')
except  FileNotFoundError:
    print('Encountered  an  exception...')
my_lock.acquire()
print('Lock  can  still  be  acquired.')