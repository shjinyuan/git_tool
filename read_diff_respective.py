#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import xlwt
import sys

p=re.compile(r'(\w+) - (\w+)')
#GIT_PATH="/home/yjin10/01_N331/buildroot_release"
GIT_PATH="/home/yjin10/01_N331/buildroot"
CURRENT_PATH=os.getcwd()
#LOG_PATH="/home/yjin10/my_laboratory/diff.log_bak"
#LOG_PATH="/home/yjin10/my_laboratory/diff.log"
#LOG_PATH_SINGLE="/home/yjin10/git_single.log"


#CMD="git log  --pretty=format:\"%H - %an\" -1 > " + LOG_PATH
#os.chdir("/home/yjin10/01_N331/buildroot")
#os.system(CMD)

commit_list=[]
commit_author=[]
diff_list=[]

def get_commit_list(num,branch):
	CMD = "git log --pretty=format:\"%H - %an\" -" + str(num) + " > " + CURRENT_PATH + "/" + "recent_commit.log"
	print CMD	
	os.chdir(GIT_PATH)
	os.system("git checkout "+ branch)
	os.system(CMD)
	os.chdir(CURRENT_PATH)
	with open("recent_commit.log","ab+") as fo:
		for line in fo.readlines():
			line = line.strip()
			s = p.match(line)
			commit_list.append(s.group(1))
			commit_author.append(s.group(2))
	fo.close()

'''
	for x in commit_list:
		print x
	for x in commit_author:	
		print x
'''

def get_log_each_commit(A1):
	CMD = "git log -p "+ A1 + " -1 > " + CURRENT_PATH + "/" + "diff_test.log"
#	CMD = "git diff "+ A1 + " " + A2 +"  > " + CURRENT_PATH + "/" + "diff_test.log"
	print CMD	
	os.chdir(GIT_PATH)
	os.system(CMD)
	os.chdir(CURRENT_PATH)
	
	
	f = open("diff_test.log")
	diff_content = f.read()
	f.close()
	return diff_content

def find_diff_in_commit(A1):	
	str=get_log_each_commit(A1)
	global IsMerge 
	index_list=[]
	diff_file_number = str.count('diff --git') 
	print "%d found in log." %diff_file_number
	if(diff_file_number > 0):
		IsMerge=0
		del index_list[:]
		del diff_list[:]
		beg = 1 
		for i in range(0,diff_file_number):
#			print "current beg: %d"  %beg
			shift = str.find("diff --git",beg)
#			print "shift is %d" %shift
			beg = beg + shift  
#			print "after add shift  ----------> %d" %beg
			index_list.append(shift-1)	
		index=0	
#		print index_list		
		for x in index_list:
			if (index_list.index(x) < len(index_list)-1):
				diff_list.append(str[index_list[index_list.index(x)]:index_list[index_list.index(x)+1]])
#				print str[index_list[index_list.index(x)]:index_list[index_list.index(x)+1]]
			else:
				diff_list.append(str[index_list[index_list.index(x)]:])
#				print str[index_list[index_list.index(x)]:]
	else:
		IsMerge=1
		del diff_list[:]
		diff_list.append(str)	
	return diff_list 


if __name__ == "__main__":
	
	if (len(sys.argv) !=3 ):
	
		print " Usage: %s argv[1] argc[2]" %sys.argv[0] 
		print "	argv[1]: number of commit"
		print "	argv[2]: local branch name"
			 
	else:
		get_commit_list(sys.argv[1],sys.argv[2])
		
		#Open a excel
		file = xlwt.Workbook()
	
		#Add worksheet with name
		table = file.add_sheet('Recent_commmit',cell_overwrite_ok=True)
		
		for i in range (0,len(commit_list)):
			row=i+1
	#		print commit_list[i]
	#		print commit_author[i]
			find_diff_in_commit(commit_list[i])
			table.write(row,1,commit_list[i])
			table.write(row,2,commit_author[i])
			if (IsMerge == 0): 
				table.write(row,3,len(diff_list))
			else:
				table.write(row,3,0)
			for x in range(0,len(diff_list)):
				table.write(row,4+x,diff_list[x].decode("utf-8", "ignore"))#忽略其中有异常的编码，仅显示有效的编码
			i = i+1
	#	save the excel with name                
		file.save('commit_history.xls')        
		print "*"*16 + " Happy Done！" + "*"*16		
	
