#!/usr/bin/env bash

# Copy current version of sliccerc.py to ~/.sliccer.py

# MASSIVE - project monash063
SLICER_PROJECT_FOLDER=/home/jonathankhoo/Monash063/mivp-anatomy/
SLICERRC_FILENAME=slicerrc.py

cp -v ${SLICER_PROJECT_FOLDER}/${SLICERRC_FILENAME} ~/.slicerrc.py

module load 3dslicer
module load virtualgl

vglrun Slicer
