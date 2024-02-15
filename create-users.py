#!/usr/bin/python2
import os
import re
import sys

def main():
	for line in sys.stdin:

		#use re.match to check for a certain character at the start of a line
		#in this case, we check and skip any lines starting with hashtag #
		match = re.match('^#', line)

		fields = line.strip().split(':') #strip any whitespace and split into an array


		if match or len(fields) != 5: #checking if # is found, or if it doesn't have 5 fields
			continue		#each line is supposed to have 5 fields
						#username, password, last name, first name, and group list
						#if not 5, then probably a messedup line we need to skip
		username = fields[0]
		password = fields[1]

		gecos    = "%s %s,,," % (fields[3],fields[2])

		groups   = fields[4].split(',') #split the group field by comma to get a list of groups

		print "==> Creating account for %s..." % (username)
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
		#print cmd
		os.system(cmd)  #execute the command
		print "==> Setting the password for %s..." % (username)
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
		#print cmd
		os.system(cmd)
		for group in groups: #iterate through each group and add the user to the group
			if group != '-':
				print "==> Assigning %s to the %s group..." % (username,group)
				cmd = "/usr/sbin/adduser %s %s" % (username,group)
				#print cmd
				os.system(cmd)

if __name__ == '__main__':  #remember to use double underlines here
	main()
