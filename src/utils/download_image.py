import requests
import json
import pandas as pd
import yaml
import sys
import re
sys.path.append('../../')
import config
import pandas as pd
from time import sleep
from utils.request import *
  
def download_image(lst_img_url,lst_img_name,dir_dest):
  for i in range(len(lst_img_url)):
    img_url = lst_img_url[i]
    img_name = dir_dest + lst_img_name[i]
    request_image(img_url, img_name)
  return None
