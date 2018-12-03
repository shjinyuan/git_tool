#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 打开文件
import os
import xlwt
print "***************************************"
print "Git clone buildroot on branch : N331......"
os.system("git clone ssh://yjin10@136.18.227.58:29418/buildroot -b N331")
print "***************************************"

CURRENT_PATH=os.getcwd()
GIT_WORK_PATH=os.path.join(CURRENT_PATH,'buildroot')

package_list = ['n331_amapapi_service',
		'n331_audio_manager',
		'n331_carsteward',
                'n331_entertainment',
                'n331_hmi_centerstack',
                'n331_hmi_cluster',
                'n331_hmi_swdl',
                'n331_ipc',
                'n331_ipod_service',
                'n331_meter',
                'n331_mode_manager',
                'n331_navigation',
                'n331_ota',
                'n331_persistency',
                'n331_phone',
                'n331_service_manager',
                'n331_settings',
                'n331_swdl',
                'n331_telematics',
                'n331_usb_manager',
                'n331_upgrade',
                'n331_vip',
                'n331_vr_service',
                'platform_allgo_release',
                'platform_audio_abstract',
                'platform_audio_aec',
                'platform_audio_control',
                'platform_audio_phone',
                'platform_audio_player',
                'platform_bluetooth_LG',
                'platform_bluetooth_service',
                'platform_media_db_indexer',
                'platform_media_db_sync',
                'platform_media_player',
                'platform_s32k_swdl',
                'platform_sys_DAR_331',
                'platform_sys_panda_dbus',
                'platform_sys_usb_manager',
                'platform_sys_video',
                'platform_tuner_amfm',
		'platform_wifi_service',
		'online_radio_kaola',
		'online_music_ultimate',
		'online_weather_lianyou',
		'online_media_player',
		'c_framework'
		];
def clean_trash():
	for i in range(0,len(package_list)):
		if os.path.exists(package_list[i]):	
			os.remove(package_list[i])
	print "Clean the old package [DONE]"
	

def generate_package_history(): 
	for n in range(0,len(package_list)):
		num=n+1
		#组合出需要查找的关键字字符串
		str="+" + package_list[n].upper() + "_VERSION"
		#各个文件的 Git 命令
		GIT_CMD="git log -p -20 package/visteon/" + package_list[n] + "/" + package_list[n] + ".mk > "+CURRENT_PATH+"/"+"git.log"
		print GIT_CMD
		
		#进入GIT的工作目录 
		os.chdir(GIT_WORK_PATH)
		
		#获取相关文件前20条的提交信息
		os.system(GIT_CMD)
		os.chdir(CURRENT_PATH)		
		fo = open("git.log")
		with open(package_list[n],"ab+") as f:
			for line in fo.readlines():                  #readline one by one
				line = line.strip()		     #remove the space at the beginning and end for each lins
				if(line.find(str) != -1):				#在line中查找str,如果有返回值不等于 -1
		#			print line[line.find(str)+ len(str) + 3 : 100]; #调整显示完整的commit id
		#			with open(package_list[n],"ab+") as f:
						short_id = line[line.find(str) + len(str) + 3 : 100].strip()[0:7] #取前7位作为短id
						f.write(short_id+"\n") 
			print "No.", num ,": Read success!"
		f.close()
		fo.close()

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


if __name__ =="__main__":
		
	clean_trash()
	
	generate_package_history()

	Write_excel()	
	
	os.system("cp -rf Statistic.xls /home/N331/tmp")
