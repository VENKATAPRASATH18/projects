import osmnx.geocoder as gd

def latitude(addrs: str): 
    try:
        gd.geocode(addrs)[0]
    except Exception as e:
        pass
    return str(gd.geocode(addrs)[0])

def longitude(addrs: str): 
    try:
        gd.geocode(addrs)[1]
    except Exception as e:
        pass
    return str(gd.geocode(addrs)[1])

def stateid(val: list):
    result=[]
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

    for id in val:
        #if id in state_id.keys():
        if state_id.get(id)!=None:
            result.append(state_id.get(id))
        else:
            continue

    return result


def latlongid(val: list):
    result=[]
    
    for i in val:
        if i is None:
            # result.append(None)
            continue
        else:
            try:
                result.append([latitude(i),longitude(i)])
            except:
                pass
    return result   