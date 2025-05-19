import requests
from datetime import datetime
time = datetime.now()
formatted = time.strftime("%Y%m%d")
user = "garen"
token ="iamvenomeminem"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{user}/graphs"
pixeladd = f"{graph_endpoint}/graph1"
user_params={
    "token":token

    ,"username":user
    ,"agreeTermsOfService":"yes"
    ,"notMinor":"yes"

}
# response =requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_params={
    "id":"graph1",
    "name":"Green",
    "unit":"min",
    "type":"int",
    "color":"sora"
}
addpixel ={
    "date":formatted
   , "quantity":"6"
}
header ={
    "X-USER-TOKEN":token
}
# response = requests.post(url=graph_endpoint,json=graph_params,headers=header)
pixel = requests.post(url=pixeladd,json=addpixel,headers=header)
print(pixel.text)
