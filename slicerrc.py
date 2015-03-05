# number of characters for ID
N = 4
SCENE_FOLDER = '/home/jonathan/scenes'

user_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
print "id: ", user_id

def load_all_scenes():
    import os
    import shutil
    import fnmatch

    # change to model view
    slicer.util.mainWindow().moduleSelector().selectModule('Models')


    global SCENE_FOLDER

    MODELS_LOADED_DIRECTORY = '/home/jonathan/models/loaded/'

    SCENE_OR_MODEL = 'scene'
#SCENE_OR_MODEL = 'model'

    if SCENE_OR_MODEL == 'scene':
        file_extension = '*.mrb'
    else:
        file_extension = '*.vtk'

    models = []
    for root, dirnames, filenames in os.walk(SCENE_FOLDER):
        for filename in fnmatch.filter(filenames, file_extension):
            models.append(os.path.join(root, filename))

    print models

    for model in models:
        if SCENE_OR_MODEL == 'scene':
            if slicer.util.loadScene(model) == True:
                print 'loaded successfully; time to move'
                try:
                    shutil.move(model, MODELS_LOADED_DIRECTORY)
                except:
                    os.remove(model)
                    pass

        else:
            if slicer.util.loadModel(model) == True:
                print 'loaded successfully; time to move'
                shutil.move(model, MODELS_LOADED_DIRECTORY)

# generate random key
# create folder of key
def setup_environment():
    import random
    import string
    import os

    global user_id
    global SCENE_FOLDER

    print "setup environment id: ", user_id

    temp_dir = os.path.join(SCENE_FOLDER, user_id)
    os.mkdir(temp_dir)

def load_data():
    # Download MRHead from sample data
    import SampleData
    sampleDataLogic = SampleData.SampleDataLogic()
    print("Getting MR Head Volume")
    mrHeadVolume = sampleDataLogic.downloadMRHead()

def save_scene():
    global user_id
    global SCENE_FOLDER
    print "save id: ", user_id

    temp_dir = os.path.join(SCENE_FOLDER, user_id)
    filename = os.path.join(temp_dir, user_id + '.mrb')
    slicer.util.saveScene(filename)

# TODO:
# - periodidcally load all scenes in a folder
# - automatically create AND volume and do volume render of the output
# 

def setupMacros():
  """Set up hot keys for various development scenarios"""
  
  import qt
  global load_all_scenes
  global setup_environment
  global save_scene
  global load_data
  
  macros = (
    ("Shift+Ctrl+2", load_all_scenes),
    ("Shift+Ctrl+3", save_scene),
    )
      
  for keys,f in macros:
    k = qt.QKeySequence(keys)
    s = qt.QShortcut(k,mainWindow())
    s.connect('activated()', f)
    s.connect('activatedAmbiguously()', f)
    print "SlicerRC - '%s' -> '%s'" % (keys, f.__name__)

  setup_environment()
  load_data()
  slicer.util.mainWindow().moduleSelector().selectModule('Editor')

# Install macros
if mainWindow(verbose=False): setupMacros()


