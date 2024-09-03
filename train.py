from datetime import datetime
import re
u={'gokul':1235,'gokul':54321}
a={'gokul':9865,'mani':8760}
class loginclass():
    def __init__(self):
        self.status=False
        self.username=""  
    def login(self,k):
        if k=="a":
            input1=input("ENTER USER NAME :")
            if input1 in a:
                print(a[input1])
                password=int(input("ENTER PASSWORD:"))
                if a[input1]==password:
                    print(f"WELCOME {input1} HERE YOU GO---->")
                    self.status=True
                    self.username=input1
                else:
                    print("wrong password")
                    self.status=False
            else:
                print("user not found")
                self.status=False
        elif k=="u":
            pass
        else:
            print("CHOOSE CORRECT OPTION")
            self.status=False
        return self.status
class trainstation(loginclass):
    def booking(self):
        traindic={'5':'12653 - Rock Fort Sf Express','5:15':'12637 - Pandian Sf Express'
                  ,'5:30':"16179 - Mannai Express",'6:15':'12637 - Pandian Sf Express'}
        if self.status:
            print("done")
            print(traindic)   
        for i,k in traindic.items():
            print(k.rjust(1),"---->",i.rjust(2))
        book=input("ENTER TRAIN TIMING:")
        bok={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
        if book in traindic:
            print(traindic[book])
            print(f"TOTAL NO OF TICKETS AVILABLE:{len(bok)}")
            bo1=input(F"DO YOU WANT TO BOOK {traindic[book]} Y/N:")
            bo=bo1.lower()
            if bo=="y":
                count=int(input("NO OF TICKETS:"))
                for i in range(count):
                    bok[i+1]=1
                print(bok)
                tc=0
                for i in bok:
                    if bok[i]==1:
                        tc+=1
                print(f"NO OF TICKETS BOOKED {tc} REMAINING {10-tc} TICKETS AVILABLE")
                bookingtime= datetime.now()
                t=bookingtime.strftime("%Y-%m-%d %H:%M:%S")
                print("TRAIN BOOKED AT: ", t)
                train_ids = re.findall(r'\b\d+\b',traindic[book])
                print (f"id:{train_ids}")
            elif bo=="n":
                print("THATS GRATE HAVE A NICE DAY")
            else:
                print("PLEASE ENTER CORRECT OPTION")
        else:
            print("TRAIN TICKET NOT AVILABLE!")
login=loginclass()
k1=input("ENTER A FOR ADMIN LOGIN ,U FOR USER LOGIN:")
k=k1.lower()
login.login(k)
# trainstation.new(1)
instance=trainstation()
instance.status = login.status
# instance.new()
instance.booking()