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
echo "Installing MongoDB"
$ins install mongodb
echo "***********************************************************************"
echo "***********************************************************************"
echo "Installing pymongo"
pip3 install pymongo
echo "***********************************************************************"
echo "***********************************************************************"
echo "Creating Database"
mongo database.js
echo "***********************************************************************"
echo "***********************************************************************"
echo "Done"
