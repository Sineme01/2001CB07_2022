from email import encoders
import socket
from email.mime.base import MIMEBase
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import smtplib
import random as r
host = "127.0.0.1"
port = 4444


def otp():
    return int(r.uniform(1000, 4444))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 4444))
s.listen()
print('server___listening')
clients_all = []
alias = []
kcm = {}
d = {}
u = {}
dc = {}
kct = {}
kcb = {}


def send_email(email, ot):
    try:
        mesg = MIMEMultipart()
        print("[+] Message Object Generated")
    except:
        print("[-] Problem in Generating Message Object")
        return
    fromaddr = 'anand_2001cb07@iitp.ac.in'
    toaddr = email

    mesg['From'] = fromaddr

    mesg['To'] = toaddr

    mesg['Subject'] = 'OTP for Reset Password'

    print(ot)
    body = 'Your verification OTP is:'+str(ot)

    mesg.attach(MIMEText(body, 'plain'))

    try:

        s = smtplib.SMTP('stud.iitp.ac.in', 587)
        print("[+] SMTP Session Formed")
    except:
        print("[-] Error in Forming SMTP session")
        return

    s.starttls()

    try:
        s.login(fromaddr, '#2001CB07_zimbra')
        print("[+] successfully logged in")
    except:

        print("[-] Login Unsuccessful")

    text = mesg.as_string()

    try:
        s.sendmail(fromaddr, toaddr, text)
        print("[+] Mail delivered")
    except:
        print('[-] Mail not delievered')

    s.quit()


def broadcast(name, mesg, clients):

    x = d[clients]+':'+mesg
    if (name not in alias):
        print(name, mesg)

    else:
        time.sleep(0.3)
        u[name].send(x.encode('ascii'))
    kcm[name].append(x)


def handle(clients):

    while (True):
        try:

            mesg = clients.recv(1024).decode('ascii')

            if (mesg == 'exit'):
                index = clients_all.index(clients)
                try:
                    for i in clients_all:
                        if (i != clients):
                            i.send(f'{d[clients]} Offline'.encode('ascii'))
                except:
                    pass
                y, m, dp, h, mini, s, w, yy, stt = time.localtime()
                if (h//10 == 0):
                    h = '0'+str(h)
                else:
                    h = str(h)
                if (mini//10 == 0):
                    mini = '0'+str(mini)
                else:
                    mini = str(mini)
                kcb[d[clients]] = 0
                kct[d[clients]] = h+':'+mini
                del u[d[clients]]
                del d[clients]

                clients_all.remove(clients)
                clients.close()
                ni = alias[index]

                alias.remove(ni)
                break

            elif (':' not in mesg):
                if (mesg not in kcm):
                    clients.send("no".encode('ascii'))
                else:

                    if (kcb[mesg] == 1):

                        clients.send("Online".encode('ascii'))
                    else:
                        clients.send(f"Last seen:{kct[mesg]}".encode('ascii'))
                    if (len(kcm[d[clients]]) != 0):

                        for i in kcm[d[clients]]:
                            time.sleep(.3)
                            clients.send(i.encode('ascii'))

            else:
                name, mesg = mesg.split(':')

                broadcast(name, mesg, clients)


        except:
            index = clients_all.index(clients)
            try:
                for i in clients_all:
                    if (i != clients):
                        i.send(f'{d[clients]} Offline'.encode('ascii'))
            except:
                pass
            y, m, dp, h, mini, s, w, yy, stt = time.localtime()
            if (h//10 == 0):
                h = '0'+str(h)
            else:
                h = str(h)
            if (mini//10 == 0):
                mini = '0'+str(mini)
            else:
                mini = str(mini)
            kcb[d[clients]] = 0
            kct[d[clients]] = h+':'+mini
            del u[d[clients]]
            del d[clients]

            clients_all.remove(clients)
            clients.close()
            ni = alias[index]

            alias.remove(ni)
            break


def ref():
    while (True):
        w = False
        c, add = s.accept()
        q = True

        mesg = c.recv(1024).decode('ascii')
        print(mesg)
        if (mesg == '1'):

            while (True):

                name = c.recv(1024).decode('ascii')
                print(name)
                if (name in dc):
                    c.send('already'.encode('ascii'))
                else:
                    c.send('ok'.encode('ascii'))
                    break
            password = c.recv(1024).decode('ascii')
            dc[name] = password

        else:

            while (True):
                name = c.recv(1024).decode('ascii')
                if (name not in dc):
                    c.send('not'.encode('ascii'))
                else:
                    c.send('ok'.encode('ascii'))
                    break
            while (True):
                ms = c.recv(1024).decode('ascii')
                if (ms == '0'):
                    password = c.recv(1024).decode('ascii')
                    if (dc[name] != password):
                        c.send("Incorrect password!!.".encode('ascii'))
                    else:
                        c.send('ok'.encode('ascii'))
                        break
                else:
                    email = c.recv(1024).decode('ascii')
                    ot = otp()
                    send_email(email, ot)
                    ms = c.recv(1024).decode('ascii')
                    if (ms == str(ot)):
                        c.send('ok'.encode('ascii'))
                        msh = c.recv(1024).decode('ascii')
                        dc[name] = msh
                        break
                    else:
                        c.send('wrong'.encode('ascii'))
            w = True

        if (w):
            pass
        else:
            kcm[name] = []

        if (q):
            clients_all.append(c)
            alias.append(name)
            kcb[name] = 1
            d[c] = name
            u[name] = c

            print(f'aliasname of the clients {name}')

        th1 = threading.Thread(target=handle, args=(c,))

        th1.start()


ref()
