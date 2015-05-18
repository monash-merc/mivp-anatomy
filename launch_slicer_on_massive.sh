#!/usr/bin/env bash

# Copy current version of sliccerc.py to ~/.sliccer.py

# MASSIVE - project monash063
SLICER_PROJECT_FOLDER=/home/projects/Monash063/mivp-anatomy/
SLICERRC_FILENAME=slicerrc.py

slicerrc_file=${SLICER_PROJECT_FOLDER}/${SLICERRC_FILENAME}

if [ ! -e "$slicerrc_file" ]; then
  echo "Could not find slicerrc.py file at $slicerrc_file. Exiting"
  exit
fi 

# This must point to the slicerrc.py file
export SLICERRC=${slicerrc_file}

module load 3dslicer
module load virtualgl

vglrun Slicer
