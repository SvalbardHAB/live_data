import requests,time,random,base64
URLROOT = "http://localhost:3000/"
SEC_KEY = "f88ee445-ddbe-47a6-b2a1-9134ea7cb1e2"

i = open('img.jpg','rb')
x = i.read()
i.close()
encoded_image = base64.b64encode(x)

while True:
    requests.post(URLROOT, data = '{"key":\"'+SEC_KEY+'\","image":\"'+encoded_image+'\"}', headers={'content-type':'application/json'})
    time.sleep(1)
    #requests.post(URLROOT, data = {'key':SEC_KEY, 'pressure':str(random.randint(980,1035))})
    time.sleep(1)
    #requests.post(URLROOT, data = {'key':SEC_KEY, 'pressure':str(random.randint(980,1035))})
    time.sleep(1)
