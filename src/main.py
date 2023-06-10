from utils.get_list_url import *
from utils.request import *
from utils.download_image import *
from utils.get_list_category import *
import yaml
import sys
sys.path.append('../../')
import config
import re
import logging

logging.basicConfig(filename="../log/logging.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# yaml_file = open("../config/config.yaml")
yaml_file = open("../config/config.yaml", encoding='utf8')
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
API_GetList = cfg['API']['API_GetList']
API_ClothesHer = cfg['API']['API_ClothesHer']
API_ClothesHim = cfg['API']['API_ClothesHim']
API_AccesHer = cfg['API']['API_AccesHer']
API_AccesHim = cfg['API']['API_AccesHim']
path_rs = cfg['data']['result']


def main():
    try:
        # Get list category
        lst_idSubsection_she,lst_familia_she,lst_IdAccesorio_she,lst_FamiliaAccesorio_she,lst_idSubsection_he,lst_familia_he,lst_IdAccesorio_he,lst_FamiliaAccesorio_he = get_list_cate(API_GetList)
        logger.info(f'Get list category sucessful -------------------------')
        #For Clothes Her
        lst_img_url_ForHer,lst_img_name_ForHer = get_img_url (API_ClothesHer,lst_familia_she,lst_idSubsection_she)
        logger.info(f'Get list {len(lst_img_url_ForHer)} image for her clothes sucessful -------------------------')
        download_image(lst_img_url_ForHer,lst_img_name_ForHer,path_rs)
        logger.info(f'Download {len(lst_img_url_ForHer)} for her clothes sucessful -------------------------')
        #For Accesorio her
        lst_img_url_Accesorio_ForHer,lst_img_name_Accesorio_ForHer = get_img_url (API_AccesHer,lst_FamiliaAccesorio_she,lst_IdAccesorio_she)
        logger.info(f'Get list {len(lst_img_url_Accesorio_ForHer)} image for her accesorio sucessful -------------------------')
        download_image(lst_img_url_Accesorio_ForHer,lst_img_name_Accesorio_ForHer,path_rs)
        logger.info(f'Download {len(lst_img_url_Accesorio_ForHer)} for her accesorio sucessful -------------------------')
        #For Clothes Him
        lst_img_url_ForHim,lst_img_name_ForHim = get_img_url (API_ClothesHim,lst_familia_he,lst_idSubsection_he)
        logger.info(f'Get list {len(lst_img_url_ForHim)} image for him clothes sucessful -------------------------')
        download_image(lst_img_url_ForHim,lst_img_name_ForHim,path_rs)
        logger.info(f'Download {len(lst_img_url_ForHim)} for him clothes sucessful -------------------------')
        #For Accesorio him
        lst_img_url_Accesorio_ForHim,lst_img_name_Accesorio_ForHim = get_img_url (API_AccesHim,lst_FamiliaAccesorio_he,lst_IdAccesorio_he)
        logger.info(f'Get list {len(lst_img_url_Accesorio_ForHim)} image for her accesorio sucessful -------------------------')
        download_image(lst_img_url_Accesorio_ForHim,lst_img_name_Accesorio_ForHim,path_rs)
        logger.info(f'Download {len(lst_img_url_Accesorio_ForHim)} for him accesorio sucessful -------------------------')    
    except Exception as e:
        logger.error(f'Fail with error {e}')
        pass
if __name__ == "__main__":
    main()