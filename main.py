import os,requests,random,time,ctypes,threading

valid,invalid = 0,0
lock = threading.Lock() 
def Banner():
        os.system('cls')
        print('''\u001b[36m
   ▄▄ •  ▄ .▄      .▄▄ · ▄▄▄▄▄▄▄▄▄· ▪   ▐ ▄     ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .▄▄▄  
  ▐█ ▀ ▪██▪▐█▪     ▐█ ▀. •██  ▐█ ▀█▪██ •█▌▐█    ▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·▀▄ █·
  ▄█ ▀█▄██▀▐█ ▄█▀▄ ▄▀▀▀█▄ ▐█.▪▐█▀▀█▄▐█·▐█▐▐▌    ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄▐▀▀▄ 
  ▐█▄▪▐███▌▐▀▐█▌.▐▌▐█▄▪▐█ ▐█▌·██▄▪▐█▐█▌██▐█▌    ██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌▐█•█▌
  ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀▀▀▀  ▀▀▀ ·▀▀▀▀ ▀▀▀▀▀ █▪    ·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀\u001b[37m]
''')

def UpdateTitle():
    while True:
        elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - start)) 
        ctypes.windll.kernel32.SetConsoleTitleW("[Ghostbin Bruter] - Valid: %s | Invalid: %s | Time elapsed: %s" % (valid, invalid,elapsed))
        time.sleep(0.4)

def Bruter():
    global valid, invalid
    code = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(5))
    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0","Referer":"https://ghostbin.com/","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Content-Type":"application/x-www-form-urlencoded"}
    url = f'https://ghostbin.com/paste/{code}'
    r = requests.get(url, headers=headers)

    if (r.status_code == 200):
        lock.acquire()
        print(' [\u001b[32mVALID\u001b[37m] ' +url)
        f = open("hits.txt", "a+").write(url+"\n")
        f.close()
        valid+=1
        lock.release()
    else:
        lock.acquire()
        print(' [\u001b[31mINVALID\u001b[37m] '+url)
        invalid+=1
        lock.release()

if __name__ == "__main__":
    Banner()
    start = time.time()
    threading.Thread(target=UpdateTitle,daemon=True).start() 
    while True:
        for i in range(100):
            threading.Thread(target=Bruter).start()