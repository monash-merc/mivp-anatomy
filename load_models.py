import os
import shutil
import fnmatch

MODELS_DIRECTORY = '/tmp/'
MODELS_LOADED_DIRECTORY = '/home/jonathan/models/loaded/'

SCENE_OR_MODEL = 'scene'
#SCENE_OR_MODEL = 'model'

if SCENE_OR_MODEL == 'scene':
    file_extension = '*.mrb'
else:
    file_extension = '*.vtk'

models = []
for root, dirnames, filenames in os.walk(MODELS_DIRECTORY):
    for filename in fnmatch.filter(filenames, file_extension):
        models.append(os.path.join(root, filename))

print models

for model in models:
    if SCENE_OR_MODEL == 'scene':
        if slicer.util.loadScene(model) == True:
            print 'loaded successfully; time to move'
            shutil.move(model, MODELS_LOADED_DIRECTORY)
    else:
        if slicer.util.loadModel(model) == True:
            print 'loaded successfully; time to move'
            shutil.move(model, MODELS_LOADED_DIRECTORY)
