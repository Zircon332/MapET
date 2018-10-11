import base64
print("icon='''\\\n" + base64.encodestring(open("img.gif", "rb").read(  )) + "'''")
