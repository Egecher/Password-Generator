import time
import numpy as np

def create_password(count):
    dizi = np.random.randint(0,100000,size=(1,10))
    print(dizi)
    parola = ''.join(map(str, dizi[0]))
    print(f"{count}- Password Created : {parola}")

count = 1
while True:
    create_password(count)
    count+=1
    time.sleep(3)