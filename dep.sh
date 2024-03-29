#!/bin/sh

if [[ -n "$(command -v yum)" ]]
then
        ins="yum"
else
        ins="apt-get"
fi



echo "***********************************************************************"
echo "***********************************************************************"
echo "Updating System"
$ins update
echo "***********************************************************************"
echo "***********************************************************************"
echo "Installing Required Python Dependencies..."
echo "Installing Python3"
$ins install python3
$ins install python3-pip
echo "***********************************************************************"
echo "***********************************************************************"

echo "Installing numpy"
pip3 install numpy
echo "***********************************************************************"
echo "***********************************************************************"

echo "Installing opencv-python"
pip3 install pip install opencv-python
echo "***********************************************************************"
echo "***********************************************************************"

echo "Installing numpy"
pip3 install numpy
echo "***********************************************************************"
echo "***********************************************************************"
echo "Done"