import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
import threading
import time
host = "127.0.0.1"
port = 4444
s.connect(('127.0.0.1',4444))
p=0


def f():
    global p
    n=input("Signup/Login(1/0):")
    
    if(n=="1"):
        s.send('1'.encode('ascii'))
   
        while(True):
            name=input("Set Username:")
            s.send(name.encode('ascii'))
            p=name
            ms=s.recv(1024).decode('ascii')
            
            if('already' == ms):
                print("Username already Exist. Try other username")
            else:
                break
        
        password=input("set Password:")
        s.send(password.encode('ascii'))
    else:
        s.send('0'.encode('ascii'))
        while(True):
            name=input("Type Username:")
            p=name
            s.send(name.encode('ascii'))
            ms=s.recv(1024).decode('ascii')
            if('not' in ms):
                print("Username doesn't Exist")

            else:
                break
        while(True):
            nn=input("Type password/Forget passwords (0/1):")
            
            if(nn=='0'):
                s.send('0'.encode('ascii'))
                password=input("Fill Password:")
                s.send(password.encode('ascii'))
                ms=s.recv(1024).decode('ascii')
                if('incorrect!!' in ms):
                    print(ms)
                else:
                    print(ms)
                    print("Successfully Logged in.")
                    break
            else:
                s.send('1'.encode('ascii'))
                email=input("Type recovery email:")
                s.send(email.encode('ascii'))
                nn=input("verify OTP:")
                s.send(nn.encode('ascii'))
                ms=s.recv(1024).decode('ascii')
                if(ms=='ok'):
                    while(True):
                        r1=input("Set new password:")
                        r2=input("Type confirmed password:")
                        if(r1==r2):
                            s.send(r1.encode('ascii'))
                            print("Password successfuly updated. You're logged in.")
                            break

                        else:
                            print("Wrong Password . Type Password.")
                            continue
                    break
                else:
                    print("Wrong OTP")
    n=input("Type recipient Username:")
    s.send(n.encode('ascii'))
    ms=s.recv(1024).decode('ascii')
    while(ms=='no'):
        print("user don't exist!!")
        n=input("Type recipient Username:")
        s.send(n.encode('ascii'))
        ms=s.recv(1024).decode('ascii')

    
    if(':' not in ms):
        print(ms)

                
    return n

     
n=f()    
ra=n
r=False
def receives():
    global ra
    while(True):
        try:
            mesg=s.recv(1024).decode('ascii')
            if(mesg=='no'):
                print("User don't Exist")
           
            
            else:
                if("Last seen" in mesg):
                    print(mesg)
                elif('Offline' in mesg):
                    sf=mesg.split(" ")[0]
                    if(sf==ra):
                        print(mesg)
                elif(':' in mesg):
                    sf=mesg.split(':')[0]
                    if(sf==ra):
                        print(mesg)
                else:
                    print(mesg)         
                
             
                
        except:
            s.close()
            break

def sends():
    y=n
    global ra
    
    while(True):
        r=False
        mesg=input("")
        if(mesg=='exit'):
            s.send('exit'.encode('ascii'))
            exit()
        if(mesg=='back'):
            ra=""
            z=input("Type recipient Username:")
            y=z
            
        r=True
        if(mesg!='back'):
            print(f'{p}:{mesg}')
            x=y+':'+mesg
        else:
            x=y
        ra=y
        s.send(x.encode('ascii'))
    
th2=threading.Thread(target=receives)
th2.start()
th1=threading.Thread(target=sends)
th1.start()
