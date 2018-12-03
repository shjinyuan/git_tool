#!/bin/sh

HEAD=`git log HEAD  --pretty=format:"%at" -1`
echo HEAD: $HEAD
CHECKED=`git log $1 --pretty=format:"%at" -1`
#echo $1
echo CHECKED: $CHECKED

if [ $HEAD > $CHECKED ];then

	echo "[PASS] $CHECKED "
else
	
	echo "[FAIL] $CHECKED "
fi
