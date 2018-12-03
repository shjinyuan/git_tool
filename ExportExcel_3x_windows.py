import xlwt
from test.test_modulefinder import package_test

#Open a excel
file = xlwt.Workbook()

#Add worksheet with name
table = file.add_sheet('package_history',cell_overwrite_ok=True)

#List the package names which are need be processed
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
                'platform_audio_control',
                'platform_audio_aec',
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
		'c_framework'
                ];
                
                
package_list_lenth=len(package_list)

#Add the line in each file 
for k in range(0,package_list_lenth):
    worked_file=package_list[k]
    
    print("Debug: current worked_file ",worked_file)
    
    #Add the title for each colume
    table.write(0,k,worked_file)
    
    #Add the line in each file 
    with open(worked_file) as f:
            for i in range(1,20):
                line=f.readline()
                print(line)
                table.write(i,k,line)
#Save the excel with name                
file.save('Statistics.xls')        

print("Done!")
