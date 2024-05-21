import os
BASE_DIR = "/home/rock/Desktop/Hearsight/English/set_face_who/resources"
RAW_IMG_DIR = os.path.join(BASE_DIR, "raw_images")
EMBEDDINGS_DIR = os.path.join(BASE_DIR, "embeddings")
AUDIODIR=os.path.join(BASE_DIR, "audio")
NO_IMG_PER_PERSON = 3

LANG_FILE = "/home/rock/Desktop/Hearsight/lang.txt"

with open(LANG_FILE,'r') as file:
    language = file.read()
                  
MACHINE_VOICE_DIR = f"/home/rock/Desktop/Hearsight/audios/{language}_audio/"


MAPPING_FILE = "mapping.json"
MAPPING_PATH = os.path.join(BASE_DIR, MAPPING_FILE)

RECOGNIZER_FILE = "recognizer.sav"
RECOGNIZER_PATH = os.path.join(BASE_DIR, RECOGNIZER_FILE)

THRESHOLD_BASE = 50

VERBOSE = True