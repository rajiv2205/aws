import sys
import os
import string

matchString = sys.argv[1]
#print matchString
searchString = sys.argv[2]
searchString2 = sys.argv[3]
filename = "config.txt"
command = "sed -n '/^"+matchString+"/,/^[0-9a-zA-Z]/p' "+filename+" |  grep "+searchString+" | awk -F : '{print $2}'"

value = os.popen(command)

#exitStatus = "echo "+value+" | wc -c"

#sts = os.popen(exitStatus)

#print sts.read()

new_val = value.read().strip()
exitStatus = "echo "+new_val+" | wc -c"
sts = os.popen(exitStatus)
status = sts.read().strip()
print status
if status == "1":
        command1 = "sed -n '/"+searchString+"/,/^[0-9a-zA-Z]/p' "+filename+" |  grep "+searchString2+" | awk -F : '{print $2}'"
	value1 = os.popen(command1)
	new_val1 = value1.read().strip()
	print new_val1
else:
        
	if searchString == "ip":
		print int(new_val) + 1
	else:
		print new_val

#def getSubnet(self):
#	return 1
