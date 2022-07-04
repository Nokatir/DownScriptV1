from time import *

timen = time()
n=0
while time()-timen<2:
    n+=1


try :
    raise Exception("Erreure normale")
except:
    raise Exception("Erreure normale")
