#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
import subprocess

data = cgi.FieldStorage()
myx = data.getvalue("x")


if ("date" in myx):
     x=subprocess.getoutput("sudo date")
     print(x)
     subprocess.getoutput("sudo espeak-ng `date`")
elif ("cal" in myx):
      x=subprocess.getoutput("sudo cal")
      print(x)
      subprocess.getoutput("sudo espeak-ng `cal`")
elif (("ls" in myx)):
      x=subprocess.getoutput("sudo ls")
      print(x)
      subprocess.getoutput("sudo espeak-ng `ls`")
elif (("pwd" in myx)):
      x=subprocess.getoutput("sudo pwd")
      print(x)
      subprocess.getoutput("sudo espeak-ng `pwd`")
elif (("hadoop" in myx))and (("version" in myx)):
      x=subprocess.getoutput("sudo hadoop version")
      print(x)
      subprocess.getoutput("sudo espeak-ng `version`")
else:
    subprocess.getoutput("sudo espeak-ng 'Command not found'")
    print("No command found...!!!")
#x=sb.getoutput(cmd)
