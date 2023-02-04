from structure import keywords,head_Keys
from pymongo import MongoClient

clientconnnect=MongoClient('mongodb://localhost:27017')
def body_only(bodyLines:str,d:dict):
    Flag=True
    if bodyLines is not None or bodyLines !='':

      if type(d['body'])==list and len(d['body'])!=0:
        
        for j in d['body']:
          if j.lower() in bodyLines.replace(',','').replace('.','').replace('’',"").replace('"',"").lower():
            continue
          else:
            return False
            
      else:
         return False

    else:
         return False
    return Flag

def head_only(headLines:str,d:dict):
  Flag=False
  if headLines is not None and headLines!='':

    for i in d['headline']:

      if type(i)==str:
        if i.lower() in headLines.replace(',','').replace('.','').replace('’',"").replace('"',"").lower():
          Flag=True
        else:
          return False

      elif type(i)==list:
        cur_list=i
        for j in cur_list:
          if j.lower() in headLines.replace(',','').replace('.','').replace('’',"").replace('"',"").lower():
            continue
          else:
            return False
        return True

  else:
    return False
  return Flag

def head_check(headLines:str,d:dict):
    Flag=False
    if headLines is not None or headLines !='':

      if type(d['headline'])==list: 

        for j in d['headline']:
          if j.lower() in headLines.replace(',','').replace('.','').replace('’',"").replace('"',"").lower():
            continue
          else:
            return False
        return True
            
      elif type(d['headline'])==str:

        if d['headline'].lower() in headLines.replace(',','').replace('.','').replace('’',"").replace('"',"").lower():
          Flag=True
        else:
          return False

    else:
        return False
    return Flag

def body_check(bodyLines:str,d:dict):
    Flag=False
    if bodyLines is not None or bodyLines !='':

      if type(d['body'])==list and len(d['body'])!=0:
        
        for j in d['body']:
          if j.lower() in bodyLines.replace(',','').replace('.','').replace('’',"").replace('"',"").lower():
            Flag=True
          else:
            continue
      else:
         return False

    else:
         return False
    return Flag


if __name__=='__main__':
    newsmon=clientconnnect['NEWSMON']
    db=newsmon['EnglishUpdateJan']
    updates=0
    
    for data in db.find({}):

        for i in keywords:

            if((head_check(data['Title'],i) and body_check(data['Text'],i)) and i['condition']=='both'):
                db.update_one( { '_id':data['_id'] }, { '$set': { 'Client': 'NCTC 1' } })
                updates=updates+1
                #print('Title: ',data['Title'],'\n')
                #print('Body: ',data['Text'],'\n')
                #print('-------------------------------------------','\n')
                break

            elif((head_check(data['Title'],i) or body_only(data['Text'],i)) and i['condition']=='anyone'):
                db.update_one( { '_id':data['_id'] }, { '$set': { 'Client': 'NCTC 2' } })
                updates=updates+1
               # print('Title: ',data['Title'],'\n')
                #print('Body: ',data['Text'],'\n')
               # print('-------------------------------------------','\n')
                break

            elif( body_only(data['Text'],i) and i['condition']=='body'):
                db.update_one( { '_id':data['_id'] }, { '$set': { 'Client': 'NCTC 3' } })
                updates=updates+1
                #print('Title: ',data['Title'],'\n')
                #print('Body: ',data['Text'],'\n')
                #print('-------------------------------------------','\n')
                break

            elif((head_only(data['Title'],head_Keys) and i['body']=='' and i['condition']=='')):
                db.update_one( { '_id':data['_id'] }, { '$set': { 'Client': 'NCTC 4' } })
                updates=updates+1
                #print('Title: ',data['Title'],'\n')
                #print('Body: ',data['Text'],'\n')
                #print('-------------------------------------------','\n')
                break

            #elif((head_check(data['Title'],i) or body_check(data['Text'],i)) and i['condition']==''):
               # db.update_one( { '_id':data['_id'] }, { '$set': { 'Client': 'NCTC' } })
               # updates=updates+1
                #print('Title: ',data['Title'],'\n')
                #print('Body: ',data['Text'],'\n')
                #print('-------------------------------------------','\n')
                #break

    print('No.Of. Articles updated',updates)




            


