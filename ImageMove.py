"This is a test version of the script that is to move the desktop pictures from one folder to other folder if the image is older than 2 day"
'''
import os
f=os.listdir("/Users/rakeshsadu/Desktop/")
print(f)

'''
import os
import time
import datetime
import shutil
import logging
from six.moves import configparser

# create an eventlogger
logger=logging.getLogger('IMAGEMOVELOG')
logger.setLevel(logging.DEBUG)
#set formatter
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

#creating a file handler
fh = logging.FileHandler('/Users/rakeshsadu/Documents/Gitprojects/RajaPersonalProjects/LOGGING/imagemove.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)

#config parser setup
config = configparser.ConfigParser()
#reading the config file from the following location
script_location = os.path.dirname(os.path.realpath(__file__))
config.read(script_location+'/imagemove.ini')

#Atributes that are take from the config file imagemove.ini from DEFAULT stanza
src = config.get('DEFAULT','source')
dest = config.get('DEFAULT','destination')
extn = config.get('DEFAULT','fileextention')

#For Handling multliple file extensions
extensions = extn.split(',')

#Need to handle the space in the delimeter values in the COfig File

def folder_name(extensions, dest):
    file_dict = {}
    for ext in extensions:
        Totalpath = dest+'folder'+(ext[1:])
        if not os.path.exists(Totalpath):
            os.makedirs(Totalpath)
            logger.info("New Folder {} is created".format(Totalpath))
        else:
            logger.info("Folder {} exists".format(Totalpath))
        new_vals = {ext:Totalpath}
        file_dict.update(new_vals)
    return file_dict

try:
    files_list=os.listdir(src)
    extn_location=folder_name(extensions,dest)
    pass
    for i in files_list:
        for key, dest_loc in extn_location.items():
            if i.endswith(key):
                TimephotoAdded = os.path.getctime(src + i)
                CurrentepochTime = float(time.time())
                TimeSinceAdded = abs(TimephotoAdded - CurrentepochTime)
                if i not in os.path.dirname(dest_loc) and TimeSinceAdded > 5.00:
                    shutil.move(src + i, dest_loc)
                    logger.info("successfully Moved the image {} to {}".format(i, dest_loc))
except Exception as e:
    logger.error("An Error occured {} :".format(e))
    raise
finally:
   logger.info("The Script has ended")
