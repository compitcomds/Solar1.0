from BunnyCDN.CDN import CDN
from BunnyCDN.Storage import Storage

storage_api_key='6bef41b0-422d-46a7-97c3d8718db6-8fa4-4284'
storage_zone_name='solarstocks'
storage_zone_region='SG'

obj_storage = Storage(storage_api_key,storage_zone_name,storage_zone_region)
obj_cdn = CDN('3edae41a-4342-4c06-815e-70029b17eba4')