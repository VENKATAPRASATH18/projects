txt='''Gujarat will soon be home to another Tent City. Nadabet, which is only 4 km from White Rann, will get a Tent City on the lines of the ones in Dhordo, Kutch and the Statue of Unity. Nadabet in Banaskantha is Gujarat’s first Indo-Pak border viewing point.

The state has already identified land for the Tent City in Nadabet and it will be ready within six months. Nadabet, India’s newest border destination, developed on the line of the Wagah Border, was opened to the public in April 2022 and also gets visitors from outside Gujarati.

However, it lacks accommodation and is quite far from major cities. Since the parade function, one of the main attractions, is held in the evening, a day trip is often not possible for visitors.

The proposed Tent City is expected to come up 10 km from Zero Point and will provide accommodation in natural surroundings.

At present, Nadabet gets 2,000 people on average every day and the number is expected to go up once accommodation facilities come up, said Secretary Tourism Hareet Shukla.

The Tent City will have 60 tents and it can go up as per the demand. The per-day rate for each tent will be at par with other Tent Cities, Shukla said.

The Nadabet provides travellers an opportunity to see the workings of an army post on India’s border.

It also offers visitors a view of the Border Security Force’s (BSF) retreat ceremony, has weapons on display, a photo gallery, tanks and other sophisticated devices.

A beating-retreat ceremony like Wagah

​​​​​​​The state government is in talks with the BSF to make the beating retreat ceremony at Nadabet as exciting, appealing and patriotic as the one at Wagah Border. Gujarat has also made representations to the Centre to get Pakistani soldiers on the other side of the border to perform a retreat ceremony to attract a large number of visitors.'''

tit='''Congress says PM Modi's New Year 'gift' cuts rations of 810 mn poor by 50%'''
from structure import keywords
def head(headLines:str,d:dict):
    Flag=False
    if headLines is not None or headLines !='':

      if type(d['headline'])==list: 

        for j in d['headline']:
          if j.lower() in headLines.lower():
            continue
          else:
            return False
            
      elif type(d['headline'])==str:

        if d['headline'].lower() in headLines.lower():
          print(d['headline'])
          Flag=True
        else:
          return False

    else:
        return False
    return Flag

def body(bodyLines:str,d:dict):
    Flag=False
    if bodyLines is not None or bodyLines !='':

      if type(d['body'])==list and len(d['body'])!=0:
        
        for j in d['body']:
          if j.lower() in bodyLines.lower():
            print(j)
            Flag=True
          else:
            continue
      else:
         return False

    else:
         return False
    return Flag

for i in keywords:

            if((head(tit,i) and body(txt,i)) and i['condition']=='both'):
                
                print('Title: ',tit,'\n')
                print('Body: ',txt,'\n')
                print('-------------------------------------------','\n')
                break

            elif((head(tit,i) or body(txt,i)) and i['condition']=='anyone'):
               
                print('Title: ',tit,'\n')
                print('Body: ',txt,'\n')
                print('-------------------------------------------','\n')
                break

            elif( body(txt,i) and i['condition']=='body'):
               
                print('Title: ',tit,'\n')
                print('Body: ',txt,'\n')
                print('-------------------------------------------','\n')
                break

            elif((head(tit,i) or body(txt,i)) and i['condition']==''):
              
                print('Title: ',tit,'\n')
                print('Body: ',txt,'\n')
                print('-------------------------------------------','\n')
                break


