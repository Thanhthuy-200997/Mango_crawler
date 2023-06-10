import requests
import json
import pandas as pd
import yaml
import sys
sys.path.append('../../')
import config
import yaml
import re
from time import sleep
from utils.request import *


# yaml_file = open("../config/config.yaml")
# cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

# def get_img_url (API_mango_details,lst_familia,lst_idSubsection):
#   lst_img_url = []
#   lst_img_name = []
#   for i in range(len(lst_idSubsection)): # crawl data from page 1 to page 10 for each request 
#     for page in range(1,2):
#       API = API_mango_details + 'pageNum=' + str(page) + '&rowsPerPage=20&columnsPerRow=4&family=' + lst_familia[i] + '&idSubSection=' + lst_idSubsection[i]
#       print(API)
#       respone_API = requests.get(API)
#       if respone_API.status_code == 200:
#         data = respone_API.text
#         # json_load = request_API(API)
#         json_load = json.loads(data)
#         if json_load['groups']:
#           for key in json_load['groups'][0]['garments'].keys():
#             img_url = json_load['groups'][0]['garments'][key]['colors'][0]['images'][0]['img1Src']
#             img_name = json_load['groups'][0]['garments'][key]['id'] + ".jpg"
#             lst_img_url.append(img_url)
#             lst_img_name.append(img_name)
#     sleep(5)      
#   return lst_img_url,lst_img_name


def get_img_url (API_mango_details,lst_familia,lst_idSubsection):
  lst_img_url = []
  lst_img_name = []
  for i in range(len(lst_idSubsection)): # crawl data from page 1 to page 10 for each request 
    for page in range(1,4):
      API = API_mango_details + 'pageNum=' + str(page) + '&rowsPerPage=20&columnsPerRow=4&family=' + lst_familia[i] + '&idSubSection=' + lst_idSubsection[i]
      # print(API)
      # respone_API = requests.get(API)
      # if respone_API.status_code == 200:
      #   data = respone_API.text
      json_load = request_API(API)
        # json_load = json.loads(data)
      if json_load['groups']:
        for key in json_load['groups'][0]['garments'].keys():
          img_url = json_load['groups'][0]['garments'][key]['colors'][0]['images'][0]['img1Src']
          img_name = json_load['groups'][0]['garments'][key]['id'] + ".jpg"
          lst_img_url.append(img_url)
          lst_img_name.append(img_name)
    sleep(5)      
  return lst_img_url,lst_img_name