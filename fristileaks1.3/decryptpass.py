# simdi ise cryptpass.py dosyasini tek tek inceleyerek onun tam tersiniz yazmaya calisacagiz. kendisi oncelikle kodumuzu base64 ile
# encode ediyor ardindan ise ters cevirip rot13 ile encode ediyor o zaman yapilmasi gerekenler tam tersleri:
# decode rot13 > ters cevir > decode base64

import base64,codecs,sys

def decodeString(str):
    decode13=codecs.decode(str, 'rot13') # decode rot13
    ters=decode13[::-1] # ters cevir
    son=base64.b64decode(ters) # decode base64
    return son
sonuc=decodeString(sys.argv[1])
print(sonuc)

# usage: 
# python decryptpass.py mVGZ3O3omkJLmy2pcuTq
# python decryptpass.py =RFn0AKnlMHMPIzpyuTI0ITG
