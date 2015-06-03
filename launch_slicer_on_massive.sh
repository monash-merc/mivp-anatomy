#!/usr/bin/env bash

#
# Launcher script to set a number of config values,
# load modules to run on MASSIVE CentOS 6, and then
# run 3D Slicer via VirtualGL.
#

umask 002 # XXX: terrible... but has to be done

# MASSIVE - project monash027
PROJECT_FOLDER=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
SLICERRC_FILENAME=slicerrc.py

slicerrc_file=${PROJECT_FOLDER}/${SLICERRC_FILENAME}

export SCENE_DIR=/scratch/Monash027/mivp-anatomy/saved-scenes/
export LOADED_DIR=/scratch/Monash027/mivp-anatomy/loaded-scenes/

if [ ! -d "$SCENE_DIR" ]; then
  echo "Error: $SCENE_DIR does not exist. Exiting"
  exit
fi

if [ ! -d "$LOADED_DIR" ]; then
  echo "Error: $LOADED_DIR does not exist. Exiting"
  exit
fi

# export DATASET=

# set folder values here. and send them via environment variables

if [ ! -e "$slicerrc_file" ]; then
  echo "Could not find slicerrc.py file at $slicerrc_file. Exiting"
  exit
fi 

# This must point to the slicerrc.py file
export SLICERRC=${slicerrc_file}

module load 3dslicer
module load virtualgl

vglrun Slicer
