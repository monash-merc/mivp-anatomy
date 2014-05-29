#!/usr/bin/env bash

SLICER_INI=/home/jonathan/.config/NA-MIC/Slicer.ini
SLICER_INI_TEMPLATE=Slicer_template.ini

id=`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 4 | head -n 1`

echo Generated ID: $id
echo "Creating temporary directory: /tmp/$id"
mkdir -v -p /tmp/$id

slicer_id_ini=Slicer_${id}.ini

echo "Generating new Slicer.ini: ${slicer_id_ini}"
sed "s/{{TMP_DIR}}/\/tmp\/$id/g" Slicer_template.ini > ${slicer_id_ini}

rm -v $SLICER_INI
#ln -v -s $slicer_id_ini $SLICER_INI
cp -v $slicer_id_ini $SLICER_INI 

/home/jonathan/Downloads/Slicer-4.3.1-linux-amd64/Slicer


