'''stone paper sessior'''
import random
comp=random.randint(0,2)
user=int(input("enter,0 for stone,1 for paper,2  for sessior="))
print("your choice=",user)
print("comp choice=",comp)
def check(comp,user):
   if user==comp:
       return 0
   elif comp==0 and user==2:
        return -1
   elif comp==1 and user==0:
        return -1
   elif comp==2 and user==1:
        return -1
    
   else: return 1

score=check(comp,user)
if score ==0:
    print ("draw")
elif score==-1:
    print("you loss")
else:
    print ("you won")  

# simple gaame 