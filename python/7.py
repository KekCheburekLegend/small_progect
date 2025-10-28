import time
a = ''
b = ['🚗','🎉','😒','🙌','🎶','😁','😂','🤣','😃',]
for i in b:
    time.sleep(0.1)
    print(i)
    for c in b:
        print(i + c)
