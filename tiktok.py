#Importing the tiktok Python SDK

from TikTokApi import TikTokApi as tiktok
#Import JSON for export of data
import json  

#Get cookie data - INCOMPLETE
verifyFp = "verify_lr7n1c0e_hzfMeVrw_iRgb_4Qv0_AQ48_hNqXKPPLMPfo"
#Setup instance
api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoinds= True)