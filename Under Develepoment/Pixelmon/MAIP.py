
#MTN

#START
import time
print("Welcome To the Minimalistic Artificial Intelligence programm [M.A.I.P] ")
time.sleep(3)
print("Version Beta 0.1")





def clever_read(com,pin):
    with open("Names.main" , "r") as load:
        for files in load.readlines()[]:
            with open(files,"r") as exe:
                exec(exe.read())
                
    
        

def clever_answer(answer,com):
    print(answer)
        
        
while 1:
    user=input("Just give me some stuff to do! > ")
    analyse = []
    analyse.extend(user)
    clever_read(user,analyse)               
