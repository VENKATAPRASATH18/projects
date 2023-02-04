from functools import cache
@cache
def find(lat:str,long:str):

    try:
        
        reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)
        #locations = [s.strip() for s in str(reverse(lat+','+long)).split(',')]
        locations =reverse(lat+','+long)
        if locations.raw['address'].__contains__('country') and locations.raw['address']['country']=='India':
                
            if locations.raw['address'].__contains__('state') :
                    return state_id.get(locations.raw['address']['state'])
                         
            elif locations.raw['address'].__contains__('city'):
                    return state_id.get(locations.raw['address']['city'] )
                
            elif locations.raw['address'].__contains__('city_district'):
                    return state_id.get(locations.raw['address']['city_district'] )
                
        else:
            return None
            
    except Exception as e:

        f=open('log.txt',"a")
        t=time.localtime()
        s=f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}  {t.tm_mday}/{t.tm_mon}/{t.tm_year}  "
        f.write(f"{s}GEOPY Reversing  lat_long_id ( {lat} {long}) {e} \n")
        f.close()
        

import pymongo
import geopy
from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time


geolocator = Nominatim(user_agent="myapp")


state_id={
      'Andhra Pradesh'     :'AP',  
      'Arunachal Pradesh'  :'AR',
      'Assam'              :'AS',
      'Bihar'              :'BR',  
      'Chhattisgarh'       :'CT',  
      'Goa'                :'GA',
      'Gujarat'            :'GJ', 
      'Haryana'            :'HR', 
      'Himachal Pradesh'   :'HP', 
      'Jharkhand'          :'JH',  
      'Karnataka'          :'KA',  
      'Kerala'             :'KL',  
      'Madhya Pradesh'     :'MP',  
      'Maharashtra'        :'MH',  
      'Manipur'            :'MN',  
      'Meghalaya'          :'ML',  
      'Mizoram'            :'MZ',  
      'Nagaland'           :'NL', 
      'Odisha'             :'OR',  
      'Punjab'             :'PB',  
      'Rajasthan'          :'RJ',  
      'Sikkim'             :'SK',  
      'Tamil Nadu'         :'TN', 
      'Telangana'          :'TG',  
      'Tripura'            :'TR',  
      'Uttarakhand'        :'UT',  
      'Uttar Pradesh'      :'UP',  
      'West Bengal'        :'WB',
      'Andaman and Nicobar Islands'  :'AN',  
      'Chandigarh'                   :'CH' , 
      'Dadra and Nagar Haveli'       :'DN',  
      'Daman and Diu'                :'DD',  
      'Delhi'              :'DL',  
      'Jammu and Kashmir'  :'JK',  
      'Ladakh'             :'LA',  
      'Lakshadweep'        :'LD',  
      'Puducherry'         :'PY' 
    }


f=open('log.txt',"a")
f.write("Time      Date      Type              Details \n")
f.close()

try:
    connect=pymongo.MongoClient('mongodb://localhost:27017/')
except Exception as e:
    f=open('log.txt',"a")
    t=time.localtime()
    s=f"Time {t.tm_hour}:{t.tm_min}:{t.tm_sec}  {t.tm_mday}/{t.tm_mon}/{t.tm_year}  "
    f.write(f"{s}DB Connection     {e} \n")
    f.close()

db=connect.NEWSMON
collection=db['lat_long']





c=0
for i in collection.find({}): 
    c=c+1
    print("Document No: "+str(c)+'\n')
    k=1
    id=set()
    if c>41500: 
     for j in i['lat_long']:
        res=str(find(j[0],j[1]))

        if res!="None":
            id.add(res)
        else:
            continue
        k=k+1
        
     try:
        collection.update_one(
        {"_id" : i['_id']},
        {"$set": {
            "state_id": list(id)
            }
        },
        )
     except Exception as e:
        f=open('log.txt',"a")
        t=time.localtime()
        s=f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}  {t.tm_mday}/{t.tm_mon}/{t.tm_year}  "
        f.write(f"{s}DB Update       {e} \n")
        f.close()
    
    