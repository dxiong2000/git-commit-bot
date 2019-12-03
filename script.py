import os
import sys
from subprocess import call

# n is number of commits
n = int(sys.argv[1])

os.chdir("D:\\Projects\\gitbot")
print(os.path.dirname(os.path.realpath(__file__)))

for i in range(n):
	#call(["echo", "\"temp\"", ">", "temp.txt"])
	open("temp.txt", 'w').close()
	call(["git", "add", "temp.txt"])
	call(["git", "commit", "-m", "\"created file {}".format(i)])
	call(["git", "push", "origin", "master"])
	os.system("del temp.txt")
	call(["git", "add", "temp.txt"])
	call(["git", "commit", "-m", "\"deleted file {}".format(i)])
	call(["git", "push", "origin", "master"])