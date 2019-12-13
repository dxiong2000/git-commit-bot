import os
import sys

# n is number of commits
n = int(sys.argv[1])

os.chdir("D:\\Projects\\gitbot")
print(os.path.dirname(os.path.realpath(__file__)))

for i in range(n):
	open("temp.txt", 'w').close()
	os.system("git add temp.txt")
	os.system("git commit -m \"created file {}\"".format(i))
	os.system("git push origin master")
	os.system("del temp.txt")
	os.system("git add temp.txt")
	os.system("git commit -m \"deleted file {}\"".format(i))
	os.system("git push origin master")

