#ip to location 
#http://ip-api.com/json/


import os
import time

os.system("clear")
time.sleep(0.5)


print("""


8888888b.        d8888 8888888b.  888    d8P         .d8888b.   .d8888b.  
888  "Y88b      d88888 888   Y88b 888   d8P         d88P  Y88b d88P  Y88b 
888    888     d88P888 888    888 888  d8P          888        888    888 
888    888    d88P 888 888   d88P 888d88K           888d888b.  Y88b. d888 
888    888   d88P  888 8888888P"  8888888b          888P "Y88b  "Y888P888 
888    888  d88P   888 888 T88b   888  Y88b  888888 888    888        888 
888  .d88P d8888888888 888  T88b  888   Y88b        Y88b  d88P Y88b  d88P 
8888888P" d88P     888 888   T88b 888    Y88b        "Y8888P"   "Y8888P"  
                                                                          
                                                                          
                                                                          

                                                           


\033[1;35m===============================================================
Tools Owner  : Abdullah 
Team            :Muslim fighter 
GitHub          :$$$$$$$$$$
Email             :mdabdullah@gmail.com
mobile           :0176876767667
Use Only for legal work Not Use For Ileg work

\033[1;35m===============================================================
                                                                      
                                                                      
                                                                      

""")






import requests 

ip=input("Enter Your Target Ip :")


req=requests.get("http://ip-api.com/json/" +ip)
txt=req.json()

print(f"country: {txt['country']}")
print(f"status:  {txt['status']}")
print(f"countryCode:  {txt['countryCode']}")
print(f"region:  {txt['region']}")
print(f"regionName:  {txt['regionName']}")
print(f"city:  {txt['city']}")
print(f"zip:  {txt['zip']}")
print(f"lat:  {txt['lat']}")
print(f"lon:  {txt['lon']}")
print(f"timezone:  {txt['timezone']}")
print(f"isp:  {txt['isp']}")
print(f"org:  {txt['org']}")
print(f"as:  {txt['as']}")



#{
#  "query": "24.48.0.1",
#  "status": "success",
#  "country": "Canada",
#  "countryCode": "CA",
#  "region": "QC",
#  "regionName": "Quebec",
#  "city": "Montreal",
#  "zip": "H1K",
#  "lat": 45.6085,
#  "lon": -73.5493,
#  "timezone": "America/Toronto",
#  "isp": "Le Groupe Videotron Ltee",
#  "org": "Videotron Ltee",
#  "as": "AS5769 Videotron Ltee"
#}
