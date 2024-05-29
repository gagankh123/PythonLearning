def open_file(n):
    files = []
    for i in range(n):
        files.append(open('/mnt/c/gagan_dev/git_repo/PythonLearning/mastering_concurrency_python/chapter4/output1/sample%i.txt' %i, 'w'))
    return files

def open_close_file(n):
    files = []
    for i in range(n):
        f = open('/mnt/c/gagan_dev/git_repo/PythonLearning/mastering_concurrency_python/chapter4/output1/sample%i.txt' %i, 'w')
        files.append(f)
        f.close()
    return files 

def with_statement_file(n):
    files = []
    for i in range(n):
        with open('/mnt/c/gagan_dev/git_repo/PythonLearning/mastering_concurrency_python/chapter4/output1/sample%i.txt' %i, 'w') as f:
            files.append(f)
            
# n=10
n=100000
open_file(n)