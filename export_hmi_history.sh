#!/bin/sh
NUM=200
GIT_HMI='/home/yjin10/01_N331/other/n331_hmi_centerstack'
cd $GIT_HMI

git pull
git log --pretty=format:"%h:%s" -$NUM > hmi_history.txt
cp hmi_history.txt /home/N331/tmp

echo "=====DONE====="
