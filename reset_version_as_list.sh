#!/bin/sh

	#package_name:revert__version
list=(
	"n331_hmi_centerstack:a327d941a9d35e790fd2ac1d3777046f63565000"
	"n331_vr_service:d49ddd741ecd9ff774b5e45e4ce2648bd13ab497" 
)

echo  "#list[@] : " ${#list[@]}
echo  "list[@] : " ${list[@]}
 
for((i=0;i<${#list[@]};i++)) 
do
	echo ${list[$i]}	
	package=`echo  ${list[$i]} | cut -d ":" -f 1`
	version=`echo  ${list[$i]} | cut -d ":" -f 2`
	echo "package : $package"
	echo "version : $version"
	cd  $package
	git pull
	git reset --hard $version
	cd .. 
done


echo "+++++++++++++++++++++++++++++++++++++++++++"
echo "+						+"
echo "+		REVERT VERSION DONE		+"
echo "+						+"
echo "+++++++++++++++++++++++++++++++++++++++++++"

