#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 打开文件
import os
import xlwt
import time
import sys


def git_update_buildroot_base():
	print "***************************************"
	print "Git clone buildroot on branch : N331_SOP2_Candidate......"
	os.system("git clone ssh://yjin10@136.18.227.58:29418/buildroot -b N331_SOP2_Candidate")
#	print "Git clone buildroot on branch : N331"
#	os.system("git clone ssh://yjin10@136.18.227.58:29418/buildroot -b N331")
	print "***************************************"
	
	print "***************************************"
	print "Git clone buildroot on branch : N331_SOP2_Candidate......"
	os.system("git clone ssh://yjin10@136.18.227.58:29418/buildroot base  -b N331_SOP2_Candidate")
	print "***************************************"

CURRENT_PATH=os.getcwd()
GIT_WORK_PATH=os.path.join(CURRENT_PATH,'buildroot')
BASE_GIT_WORK_PATH=os.path.join(CURRENT_PATH,'base')
PACKAGE_BASE_GIT="git clone ssh://yjin10@136.18.227.58:29418/"
package_list = ['n331_amapapi_service:',
		'n331_audio_manager:',
		'n331_carsteward:',
                'n331_entertainment:',
       	        'n331_hmi_centerstack:hmi_sop_0914',
                'n331_hmi_cluster:',
                'n331_hmi_swdl:',
                'n331_ipc:',
                'n331_ipod_service:',
                'n331_meter:pv',
                'n331_mode_manager:',
                'n331_navigation:',
                'n331_ota:',
                'n331_persistency:',
                'n331_phone:',
                'n331_service_manager:',
                'n331_settings:',
                'n331_swdl:',
                'n331_telematics:',
                'n331_usb_manager:',
                'n331_upgrade:',
                'n331_vip:pv',
                'n331_vr_service:',
                'platform_allgo_release:N331',
                'platform_audio_abstract:N331',
                'platform_audio_aec:waf',
                'platform_audio_control:n331',
                'platform_audio_phone:N331',
                'platform_audio_player:waf',
                'platform_bluetooth_LG:',
                'platform_bluetooth_service:N331',
                'platform_media_db_indexer:waf',
                'platform_media_db_sync:N331',
                'platform_media_player:waf',
                'platform_s32k_swdl:',
                'platform_sys_DAR_331:',
                'platform_sys_panda_dbus:waf',
                'platform_sys_usb_manager:pandaplus',
                'platform_sys_video:',
                'platform_tuner_amfm:n331',
		'platform_wifi_service:',
		'online_radio_kaola:',
		'online_music_ultimate:',
		'online_weather_lianyou:',
		'online_media_player:',
		'weston:N331',
		'c_framework:'
		];
def clean_trash():
	for i in range(0,len(package_list)):
		if os.path.exists(package_list[i]):	
			os.remove(package_list[i])
	print "Clean the old package [DONE]"
	

def check_diff_on_base(): 
	for n in range(0,len(package_list)):
		num=n+1
		GIT_CMD=''
		package_name=package_list[n].split(':')[0]
		#组合出需要查找的关键字字符串
		key_str="+" + package_name.upper() + "_VERSION"
		#各个文件的 Git 命令/**TODO if weston **/
		package_branch="master"		
		if(package_list[n].split(':')[1]!=''):	
			package_branch=package_list[n].split(':')[1]	
		if(package_name !='weston'):
			GIT_CMD="git log -p -1 package/visteon/" + package_name + "/" + package_name + ".mk |grep " + key_str + "|awk -F'=' '{print $2}'"
		else:
			GIT_CMD="git log -p -1 package/" + package_name + "/" + package_name + ".mk |grep " + key_str + "|awk -F'=' '{print $2}'"
#		print "[Debug]: " ,GIT_CMD
		
		#进入GIT的工作目录 
		os.chdir(GIT_WORK_PATH)
		#os.system("git pull")
		#获取相关文件的提交信息
		latest_package_version_buildroot=os.popen(GIT_CMD).read().strip()[0:7]

		#进入BASE GIT的工作目录 
		os.chdir(BASE_GIT_WORK_PATH)
		#os.system("git pull")
		
		#获取base相关文件的提交信息
		base_latest_package_version_buildroot=os.popen(GIT_CMD).read().strip()[0:7]
		
#		print "[Debug] latest_package_version: ",latest_package_version_buildroot
		#回到工作目录
		os.chdir(CURRENT_PATH)		
		#git clone package
		PACKAGE_GIT_CMD=PACKAGE_BASE_GIT + package_name + ' -b ' + package_branch
#		print "[Debug] PACKAGE_GIT_CMD : ", PACKAGE_GIT_CMD
		if (os.path.exists(os.path.join(CURRENT_PATH,package_name))):
			#进入package git 目录
			os.chdir(os.path.join(CURRENT_PATH,package_name))
			print "Package name: ", package_name
			os.system("git checkout " + package_branch)
			os.system("git pull")
		else:
			os.system(PACKAGE_GIT_CMD)
			os.chdir(os.path.join(CURRENT_PATH,package_name))
#		print "[Debug] now path is: ", os.getcwd()
		git_str=base_latest_package_version_buildroot+ ".." + latest_package_version_buildroot
		print os.getcwd()
		print git_str
#		www=os.popen("git log "+ git_str + " --pretty=format:'%h : %s' ").read()
		www=os.popen("git log "+ git_str).read()
		print www
		
def Write_excel():
	#open a excel
	file = xlwt.Workbook()

	#Add worksheet with name
	table = file.add_sheet('package_history',cell_overwrite_ok=True)
	package_list_lenth=len(package_list)
	#Add the line in each file 
	for k in range(0,package_list_lenth):
		worked_file=package_list[k]
   		#Add the title for each colume
   		table.write(0,k,worked_file)
    
#        	print "="*8,worked_file,'='*8
   		#Add the line in each file 
   		with open(worked_file) as f:
			for i in range(1,20):
				line=f.readline()[0:7]  #这么做是为了去掉尾部的回车，避免excel处理时的麻烦
#	      			print "line: ", line
               			table.write(i,k,line)
			#Save the excel with name                
	file.save('Statistics.xls')        

	print "Export excel Done!" 

def reset2version(direct,version):
	os.chdir(direct)
	os.system("git pull")
	os.system("git reset --hard " + version)
	os.chdir(CURRENT_PATH)
def usage():
	print "\nUsage:"
	print "./check_diff_on_base.py buildroot_git_version base_git_version\n"

if __name__ =="__main__":
	
	if (len(sys.argv) == 1):
		usage()
	
	if (len(sys.argv) == 3):
		git_update_buildroot_base()	
		reset2version("buildroot",sys.argv[1])
		reset2version("base",sys.argv[2])		

		savedStdout = sys.stdout #保存标准输出流
		with open('diff.log', 'w+') as file:
			os.system('date')	
			sys.stdout.flush()
			sys.stdout = file #标准输出重定向至文件
			check_diff_on_base()
		sys.stdout = savedStdout #恢复标准输出流
