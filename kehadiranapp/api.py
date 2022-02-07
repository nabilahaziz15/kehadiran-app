import requests

def tempat():
    #api_url = "https://portal-apac.central.arubanetworks.com/platform/frontend/"
    #api_url = " https://portal-apac.central.arubanetworks.com/platform/frontend/#!/APIGATEWAY"
    # api_url = "https://api.kawalcorona.com/indonesia/"
    #api_url = "https://portal-apac.central.arubanetworks.com/platform/signup/aepsetiawan@apps.ipb.ac.id/6JC4jbyBLlAGwHIr9X4WJAxGBlQyuNvO/76da9947adf7454fa3856f3331d29449?language=en_US"
    #access_token = "cbaRBIL0IwFFy2i5R684886TRTRvOFpn"
    rslt=requests.get(api_url).json()
    print(rslt)

# refresh=schedule.every(2).seconds.do(tempat) #adar web refresh otomatis

data_tempat=tempat()
print(tempat)