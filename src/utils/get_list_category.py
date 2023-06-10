import yaml
import sys
sys.path.append('../../')
import config
import requests
import json
from utils.request import *
import re

yaml_file = open("../config/config.yaml", encoding='utf8')
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
Menu_ForHer = cfg['menus']['ForHer']
Menu_ForHim = cfg['menus']['ForHim']
Cate_Clothes = cfg['Category']['Clothes']
Cate_Accesorio = cfg['Category']['Accesorio']

def get_list_cate(API_Getlist):
    familia_check = re.compile(r'familia|accesorio')
    lst_idSubsection_she = []
    lst_familia_she = []
    lst_IdAccesorio_she = []
    lst_FamiliaAccesorio_she = []
    lst_idSubsection_he = []
    lst_familia_he = []
    lst_IdAccesorio_he = []
    lst_FamiliaAccesorio_he = []
    json_load = request_API(API_Getlist)
    for key in json_load['menus'][Menu_ForHer]['menus']: #get item for her
        if key == str(Cate_Clothes):
            lst_cate_she = json_load['menus'][Menu_ForHer]['menus'][key]
            for i in range(len(lst_cate_she)):
                if familia_check.search(json_load['menus'][Menu_ForHer]['menus'][key][i]['retroId']) is not None: 
                    idSubsection = lst_cate_she[i]['id']
                    familia = lst_cate_she[i]['family']
                    lst_idSubsection_she.append(idSubsection)
                    lst_familia_she.append(familia)
        elif key == str(Cate_Accesorio):
            lst_accesorio_she = json_load['menus'][Menu_ForHer]['menus'][key]
            for i in range(1,len(lst_accesorio_she)):
                if familia_check.search(json_load['menus'][Menu_ForHer]['menus'][key][i]['retroId']) is not None: 
                    idSubsection = lst_accesorio_she[i]['id']
                    familia = lst_accesorio_she[i]['family']
                    lst_IdAccesorio_she.append(idSubsection)
                    lst_FamiliaAccesorio_she.append(familia)                
    for key in json_load['menus'][Menu_ForHim]['menus']: #get item for hi
        if key == str(Cate_Clothes):
            lst_cate_he = json_load['menus'][Menu_ForHim]['menus'][key]
            for i in range(len(lst_cate_he)):
                if familia_check.search(json_load['menus'][Menu_ForHim]['menus'][key][i]['retroId']) is not None: 
                    idSubsection = lst_cate_he[i]['id']
                    familia = lst_cate_he[i]['family']
                    lst_idSubsection_he.append(idSubsection)
                    lst_familia_he.append(familia)  
        elif key == str(Cate_Accesorio):
            lst_accesorio_he = json_load['menus'][Menu_ForHim]['menus'][key]
            for i in range(1,len(lst_accesorio_he)):
                if familia_check.search(json_load['menus'][Menu_ForHim]['menus'][key][i]['retroId']) is not None: 
                    idSubsection = lst_accesorio_he[i]['id']
                    familia = lst_accesorio_he[i]['family']
                    lst_IdAccesorio_he.append(idSubsection)
                    lst_FamiliaAccesorio_he.append(familia) 
    return lst_idSubsection_she,lst_familia_she,lst_IdAccesorio_she,lst_FamiliaAccesorio_she,lst_idSubsection_he,lst_familia_he,lst_IdAccesorio_he,lst_FamiliaAccesorio_he