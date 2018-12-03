#!/bin/sh
#########################################################
# Usage:						#	
# 							#
# 	./Create_OTA_Delta_ISO.sh  123			#
# 							#
# 	123 means copy #①  #②  #③  as below		#
# 							#
# 							#
# 							#
# 							#
# 升级最小单元						#
# 标号	升级包结构					#
# ①	MCU	N331_Meter_boot_swdl_app.bin		#
# ②		n331_vip_boot_swdl_app.bin		#
# ③	SOC	imx6q-sx5.dtb				#
# ④		ramdisk					#
# ⑤		rootfs.tar				#
# ⑥		u-boot.imx				#
# ⑦		zImage					#
# ⑧	APP	Navi/map.tar				#	
# 		Navi/map_data.tar			#
# 		Userdata				#
# 							#
# 由于 version.txt 会打包在rootfs.tar里			#
# 所以正常情况 rootfs.tar 一直是变化的			#	
# 							#
#########################################################


OLD='/home/N331_R/N331_Release/0810/HIGH/OLD_upgrade-ring'
NEW='/home/N331_R/N331_Release/0810/HIGH/NEW_upgrade-ring'
WORK_FOLDER='/home/N331_R/N331_Release/0810/HIGH/N331_build_MAX'
opt=$1

cd $WORK_FOLDER

echo -e "Step 1. Delete upgrade-ring in $WORK_FOLDER \n"
rm -rf $WORK_FOLDER/upgrade-ring

echo -e "Step 2. COPY $NEW to $WORK_FOLDER \n"
cp -rf $NEW $WORK_FOLDER/upgrade-ring

echo -e "Step 3. COPY the required source from $OLD \n"
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
for (( i = 0; i < ${#opt}; ++i))
	do
	c=${opt:$i:1}
		case $c in 
			0)	echo "		Do Nothing"
			;;
			1)	echo "		copy N331_Meter_*"
				cp  -r $OLD/MCU/N331_Meter_* $WORK_FOLDER/upgrade-ring/MCU
			;;
			2)	echo "		copy n331_*"
				cp  -r $OLD/MCU/n331_vip_boot_swdl_app.* $WORK_FOLDER/upgrade-ring/MCU
			;;
			3)	echo "		copy imx6q-sx5.dtb"
				cp  -r $OLD/SOC/imx6q-sx5.dtb $WORK_FOLDER/upgrade-ring/SOC
			;;
			4)	echo "		copy ramdisk "
				cp  -r $OLD/SOC/ramdisk $WORK_FOLDER/upgrade-ring/SOC
			;;
			5)	echo "		copy rootfs.tar"
				cp  -r $OLD/SOC/rootfs.tar $WORK_FOLDER/upgrade-ring/SOC
			;;
			6)	echo "		copy u-boot.imx"
				cp  -r $OLD/SOC/u-boot.imx $WORK_FOLDER/upgrade-ring/SOC
			;;
			7)	echo "		copy zImage"
				cp  -r $OLD/SOC/zImage $WORK_FOLDER/upgrade-ring/SOC
			;;
			8)	echo "		copy map.tar"
				cp  -r $OLD/APP/NAVI/map.tar $WORK_FOLDER/upgrade-ring/APP/NAVI
			;;
		esac
	done	

echo -e "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

echo -e "Step 4. Make iso\n"
make N331_defconfig O=rootfs
make O=rootfs VEL_TYPE=HIGH

echo -e "Step 5. Do backup\n"
sleep 2
mkdir -p $opt
cp -r upgrade-ring.iso $opt












