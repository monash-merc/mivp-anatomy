import os
import shutil
import random
import string

# number of characters for ID
N = 4

# folder to save scenes
SCENE_FOLDER = '/home/jonathankhoo/Monash063_scratch/mivp-anatomy/saved-scenes/'

# folder to move loaded scenes to
MODELS_LOADED_DIRECTORY = '/home/jonathankhoo/Monash063_scratch/mivp-anatomy/loaded-scenes'

user_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
print "id: ", user_id

def load_all_scenes():
    import fnmatch

    global SCENE_FOLDER
    global MODELS_LOADED_DIRECTORY

    # change to model view
    slicer.util.mainWindow().moduleSelector().selectModule('Models')

    models = []
    for root, dirnames, filenames in os.walk(SCENE_FOLDER):
        for filename in fnmatch.filter(filenames, '*.mrb'):
            models.append(os.path.join(root, filename))

    print models

    for model in models:
        if slicer.util.loadScene(model) == True:
            print 'loaded successfully; time to move'
            try:
                shutil.move(model, MODELS_LOADED_DIRECTORY)
            except:
                os.remove(model)
                pass

# create folder of key
def setup_environment():
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

def select_andsfilter():
    print "selecting ANDS filter"
    slicer.util.mainWindow().moduleSelector().selectModule('SimpleFilters')


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
  global select_andsfilter
  
  macros = (
    ("Shift+Ctrl+2", save_scene),
    ("Shift+Ctrl+3", load_all_scenes),
    ("Shift+Ctrl+4", select_andsfilter)
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


