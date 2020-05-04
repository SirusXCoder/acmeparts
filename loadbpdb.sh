#! /bin/sh
# BPDB Load Script
#
echo
echo "  ---> clearing PRODUCTS tables  \n "
python manage.py migrate products zero

echo  
echo "  --->  Initialize Product TABLES\n "
python manage.py migrate
echo "  ---> Done initializing tables \n\n"
#
echo "  ---> Loading BPDB data ... \n"
#
echo "  ---> Loading PACKAGES data ... "
python manage.py loaddata packages.json
echo
echo "  ---> Loading CERTIFICATION data ... "
python manage.py loaddata certifications.json
echo
echo "  ---> Loading FORM FACTOR data ... "
python manage.py loaddata formfactors.json
echo
echo "  ---> Loading VENDOR data ... "
python manage.py loaddata mfglocs.json
echo
echo "  ---> Loading CONFIGURATION data ... "
python manage.py loaddata configurations.json
echo "\n\n"
echo "#######################################"
echo "  *** PROCESS MAIN PRODUCT TABLES ***  "
echo "#######################################"
echo
echo "  ---> Loading CHIP data ... "
python manage.py loaddata chips.json
echo
echo "  ---> Loading BOARD data ... "
python manage.py loaddata boards.json
echo
echo "  ---> Loading SYSTEM data ... "
python manage.py loaddata systems.json
echo "\n\n"
echo "#######################################"
echo "  *** DATA LOADS COMPLETED ***  "
echo "#######################################"
echo "\n\n"


