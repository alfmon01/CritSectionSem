

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array, Lock, BoundedSemaphore

N=8

def non_critic_section(common, tid):
    for i in range(3):
        print(f'{tid}−{i}: Non−critical Section')
        print(f'{tid}−{i}: End of non−critical Section')
        
def critic_section(common, tid):
    for i in range(3):
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        common.value = v
        print(f'{tid}−{i}: End of critical section')

def task(common, tid, l):
    non_critic_section(common, tid)
    l.acquire()
    critic_section(common, tid)
    l.release()



 
def main():
    lp=[]
    common=Value('i', 0)
    l = BoundedSemaphore(1)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, l)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
        
    print (f"Valor final del contador {common.value}")
    print ("fin")
if __name__ == "__main__":    main()