def login(req):
    d={'gokul':'9865','mani':'8760','kumar':'1234'}
    a1=input("enter user name:")
    b=input("enter password:")
    
    a=a1.lower()
    b1=b.strip()
    if d[a1]==b1:
        print("user found")
    else:
        print("user not found")
        
login(0)

