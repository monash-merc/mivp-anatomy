#!/usr/bin/env bash

umask 002 # XXX: terrible... but has to be done

# MASSIVE - project monash027
PROJECT_FOLDER=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
SLICERRC_FILENAME=slicerrc.py

slicerrc_file=${PROJECT_FOLDER}/${SLICERRC_FILENAME}

if [ ! -e "$slicerrc_file" ]; then
  echo "Could not find slicerrc.py file at $slicerrc_file. Exiting"
  exit
fi 

# This must point to the slicerrc.py file
export SLICERRC=${slicerrc_file}

module load 3dslicer
module load virtualgl

vglrun Slicer
