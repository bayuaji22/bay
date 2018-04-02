# -*- coding: utf-8 -*-
#DoniSatriaBot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,string,ast,os,subprocess,six,ast,pytz,requests,tempfile

ka = LINETCR.LINE()
ka.login(token='EpNXG7DPqALvQM4PLzR9.mcgNJZM/LzspJccBd9bWwq.9qcmIHjObYsRCTlhiLZ0QdJNwBcvEFkhVYLxXIUm0f0=')
ka.loginResult()

kb = LINETCR.LINE()
kb.login(token='EprNj8HVoWJZDt5acOM5.x9stiL3M304dZxfq5Qx1Lq.+43hG87BfneOG33gLiIN+Z+XfkHfvZ5Xgc7lFuNxDtI=')
kb.loginResult()

kc = LINETCR.LINE()
kc.login(token='EprF74V3PgDJNJuVkhv4.AfXiUEwlH/LPi+AY4rWena.pmHKyD7f5V1qyznVTpnF2rjYgdCKe8kjBUsNzG3AggA=')
kc.loginResult()

kd = LINETCR.LINE()
kd.login(token='EpZzKxrE4ZCfEe88Ukkf.1ZkEufVlAC998ZnedS4sxW.shHF+i7h9VdZ8WNjQDPGl0FELwRZAW8aCY4TwQMAxw0=')
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token='EpLR4ghTyaBqXbr7A9k1.0LG/m4b5Hl9w/in/aRu5Kq.ip2Y4vihlops2KMgEI8zl1UPvqLOrxPTSjLW2GHTa6Y=')
ke.loginResult()

backup = LINETCR.LINE()
backup.login(token='EqMFLx8hYDXv2qA6ZVGf.1CoDT6S0YL/Xx5N+7ZeeFW.rZ3aOkFHr1kvYAcu+Czg5zfqTaUglIqpV1UyKd/l2HU=')
backup.loginResult()

print "Sukses All Login"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔════════
╠    M E N U
╠════════
╠ Help Publik
╠ Help Creator
╠ Help Setting
╠ Help Media
╠════════
╚════════
"""

creatorMessage ="""
╔════════
╠   A D M I N
╠════════
╠steal
╠/invitemeto:
╠Leave all group
╠Clear
╠Ourl/Curl
╠Status
╠Tagall
╠Lurking
╠Gurl
╠Masuk/Keluar
╠Banlist
╠Clear ban
╠Bot restart
╠Glist
╠Glistmid
╠Removechat
╠════════
╚════════
"""

setMessage ="""
╔════════
╠  S E T I N G
╠════════
╠Purge on/off
╠Cancel on/off
╠Qr on/off
╠Contact on/off
╠Join on/off
╠Leave on/off
╠Share on/off
╠Simisimi on/off
╠Sider on/off
╠Lurking on/off
╠Lurking reset
╠Admin add @
╠Admin remove @
╠Sambutan on/off
╠Cancelinvite on/off
╠════════
╚════════
"""
publikMessage ="""
╔════════
╠  P U B L I K
╠════════
╠Me
╠Creator
╠Ginfo
╠Adminlist
╠List group
╠Absen
╠Respon
╠Sp/Speed
╠════════
╚════════
"""
mediaMessage ="""
╔════════
╠   M E D I A
╠════════
╠/musik
╠/lirik
╠Ig:
╠Youtubelink:
╠Say-id
╠Say-en
╠Say welcome
╠Playstore
╠/apakah
╠/hari
╠/berapa
╠/berapakah
╠/kapan
╠Image
╠Tr-en
╠Tr-id
╠En@id
╠Id@en
╠SearchID:
╠Runtime
╠════════
╚════════
"""
KAC=[ka,kb,kc,kd,ke]
mid = ka.getProfile().mid
Amid = kb.getProfile().mid
Bmid = kc.getProfile().mid
Cmid = kd.getProfile().mid
Dmid = ke.getProfile().mid
Emid = backup.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid]
owner=["ud5c39db7ab34ca5fb15f99ffef31047f"]
admin=["ud5c39db7ab34ca5fb15f99ffef31047f"]

contact = ka.getProfile()
backup1 = ka.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

contact = kb.getProfile()
backup2 = kb.getProfile()
backup2.displayName = contact.displayName
backup2.statusMessage = contact.statusMessage                        
backup2.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup3 = kc.getProfile()
backup3.displayName = contact.displayName
backup3.statusMessage = contact.statusMessage                        
backup3.pictureStatus = contact.pictureStatus

contact = kd.getProfile()
backup4 = kd.getProfile()
backup4.displayName = contact.displayName
backup4.statusMessage = contact.statusMessage                        
backup4.pictureStatus = contact.pictureStatus

contact = ke.getProfile()
backup5 = ke.getProfile()
backup5.displayName = contact.displayName
backup5.statusMessage = contact.statusMessage                        
backup5.pictureStatus = contact.pictureStatus
#==============================================================================#
responsename = ka.getProfile().displayName
responsename2 = kb.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kd.getProfile().displayName
responsename5 = ke.getProfile().displayName

wait = {
    "contact":False,
    "Bot":{},
    "autoJoin":True,
    "autoCancel":{"on":False,"members":1},
    "leaveRoom":True,
    "timeline":True,
    "Timeline":True,
    "autoAdd":True,
    "lang":"JP",
    "comment1":"😴Auto Like By zhu",
    "comment2":"😴Auto Like By zhu",
    "comment3":"😴Auto Like By zhu",
    "comment4":"😴Auto Like By zhu",
    "comment5":"😴Auto Like By zhu",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":True,
    "Protectcancl":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True,
    "blacklist":{},
    "steal":{},
    "message":"Thx For Add Me ",    
    "Sambutan":True,
    "Sider":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{}
}

settings = {
    "simiSimi":{}
}

setTime = {}
setTime = read['readTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
           if wait["autoAdd"] == True:
              ka.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                ka.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ka.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        ka.sendText(op.param1, "Hai " + "[ " + Name + " ]" + "\ndo not take a peek here to chat😁   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        ka.sendText(op.param1, "Hai " + "[ " + Name + " ]" + "\ndo not take a peek here to chat😁   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    ka.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\ndo not take a peek here to chat😁   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass 
#==============================================================================#
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
#==============================================================================#
        if op.type == 13:
          if mid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                ka.acceptGroupInvitation(op.param1)
                G = ka.getGroup(op.param1)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
              else:
                ka.rejectGroupInvitation(op.param1)
                
          if Amid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                kb.acceptGroupInvitation(op.param1)
              else:
                kb.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
                
          if Bmid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                kc.acceptGroupInvitation(op.param1)
              else:
                kc.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
                
          if Cmid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                kd.acceptGroupInvitation(op.param1)
              else:
                kd.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
                
          if Dmid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                ke.acceptGroupInvitation(op.param1)
              else:
                ke.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
#==============================================================================#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = ka.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots or admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
                try:
                  ka.cancelGroupInvitation(op.param1, gMembMids)
                  ka.sendText(op.param1,ka.getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==============================================================================#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if wait["blacklist"][op.param3] == True:
              ka.sendText(op.param1,ka.getContact(op.param3).displayName + " On Blacklist Boss\nWe Will Cancel Invitation")
              random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
#==============================================================================#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if ka.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).preventJoinByTicket = True
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#==============================================================================#
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in owner:
                return
            ginfo = ka.getGroup(op.param1)
            contact = ka.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            ka.sendText(op.param1,"Hallo " + ka.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ka.sendMessage(c)  
            ka.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }                
            ka.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
#==============================================================================#
        if op.type == 17: #Protect Join
          if wait["Protectjoin"] == True:
            if wait["blacklist"][op.param2] == True:
              ka.sendText(op.param1,ka.getContact(op.param2).displayName + " On Blacklist Boss\nWe Will Kick")
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==============================================================================#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
#==============================================================================#
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or owner:
                  G = ke.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  ke.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(op.param1)
                  backup.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  backup.kickoutFromGroup(op.param1,[op.param2])
                  H = backup.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  backup.updateGroup(H)
                  Ticket = backup.reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ke.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  backup.leaveGroup(op.param1)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#==============================================================================#
            elif op.param3 in Amid:
              if op.param2 not in Bots or owner:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kc.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Bmid:
              if op.param2 not in Bots or owner:
                  G = kd.getGroup(op.param1)
                  kd.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kd.updateGroup(G)
                  Ticket = kd.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kd.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kd.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Cmid:
              if op.param2 not in Bots or owner:
                  G = ke.getGroup(op.param1)
                  ke.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ke.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(op.param1)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ke.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Dmid:
              if op.param2 not in Bots or owner:
                  G = ka.getGroup(op.param1)
                  ka.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ka.updateGroup(G)
                  Ticket = ka.reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ka.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ka.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
        if op.type == 19: #admin
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
            try:
              if op.param3 in admin:
                if op.param2 not in Bots or owner:
                  if op.param2 in Bots:
                    pass
                  elif op.param2 in owner:
                    pass
                  else:
                    try:
                      ka.kickoutFromGroup(op.param1,[op.param2])
                      kb.kickoutFromGroup(op.param1,[op.param2])
                      kc.kickoutFromGroup(op.param1,[op.param2])
                      kd.kickoutFromGroup(op.param1,[op.param2])
                      ke.kickoutFromGroup(op.param1,[op.param2])
                      ka.inviteIntoGroup(op.param1,[op.param3])
                      kb.inviteIntoGroup(op.param1,[op.param3])
                      kc.inviteIntoGroup(op.param1,[op.param3])
                      kd.inviteIntoGroup(op.param1,[op.param3])
                      ke.inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).getGroup(op.param1)
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
#==============================================================================#
              elif op.param3 in owner:
                if op.param2 not in Bots or owner:
                  try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    #ka.inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).getGroup(op.param1)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    #random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
            except:
              try:
                ka.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
#==============================================================================#
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
#==============================================================================#
        if op.type == 26:
            msg = op.message
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            ka.sendMessage(msg)
            ka.sendText(op.param1,ka.getContact(op.param2).displayName + " Kickers")
#==============================================================================#
        if op.type == 11:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            ka.sendMessage(msg)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ka.sendText(msg.to, "[One Piece Chat] " + "\n" + data['result']['response'].encode('utf-8'))
#==============================================================================#
        if op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param2 not in admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              else:
                random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True
#==============================================================================#
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ka.leaveRoom(msg.to)
#==============================================================================#
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ka.like(url[25:58], url[66:], likeType=1001)
#==============================================================================#
        if op.type == 26:
            msg = op.message
        if op.type == 26:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                ka.sendText(msg.to,"Bot Sudah on Kembali.")  

        if op.type == 26:
          if wait["Bot"] == True:    
            msg = op.message
            
        if op.type == 26:
            msg = op.message
#==============================================================================#
            if msg.contentType == 13:
              if msg.from_ in owner:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ka.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ka.findAndAddContactsByMid(target)
                                contact = ka.getContact(target)
                                cu = ka.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                ka.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                ka.sendText(msg.to,"Profile Picture " + contact.displayName)
                                ka.sendImageWithURL(msg.to,image)
                                ka.sendText(msg.to,"Cover " + contact.displayName)
                                ka.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass
#==============================================================================#
              elif wait["wblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  ka.sendText(msg.to,"already")
                  wait["wblack"] = False
                else:
                  wait["commentBlack"][msg.contentMetadata["mid"]] = True
                  wait["wblack"] = False
                  ka.sendText(msg.to,"decided not to comment")
#==============================================================================#
              elif wait["dblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  del wait["commentBlack"][msg.contentMetadata["mid"]]
                  ka.sendText(msg.to,"deleted")
                  wait["dblack"] = False
                else:
                  wait["dblack"] = False
                  ka.sendText(msg.to,"It is not in the black list")
#==============================================================================#
              elif wait["wblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  ka.sendText(msg.to,"already")
                  wait["wblacklist"] = False
                else:
                  wait["blacklist"][msg.contentMetadata["mid"]] = True
                  wait["wblacklist"] = False
                  ka.sendText(msg.to,"aded")
#==============================================================================#
              elif wait["dblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  del wait["blacklist"][msg.contentMetadata["mid"]]
                  ka.sendText(msg.to,"deleted")
                  wait["dblacklist"] = False
                else:
                  wait["dblacklist"] = False
                  ka.sendText(msg.to,"It is not in the black list")
#==============================================================================#
              elif wait["contact"] == True:
                msg.contentType = 0
                ka.sendText(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                  contact = ka.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = ka.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    ka.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                else:
                  contact = ka.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = ka.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    ka.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    ka.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#==============================================================================#
            elif msg.text in ["Key","help","Help"]:
                ka.sendText(msg.to,helpMessage)

            elif msg.text in ["Key creator","help creator","Help Creator"]:
                ka.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key self","help self","Help Publik"]:
                ka.sendText(msg.to,publikMessage)

            elif msg.text in ["Key set","help set","Help Setting"]:
                ka.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help Media"]:
                ka.sendText(msg.to,mediaMessage)
#==============================================================================#
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ka.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ka.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ka.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
            elif msg.text is None:
                return
#==============================================================================#
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ud5c39db7ab34ca5fb15f99ffef31047f'}
                ka.sendMessage(msg)
#==============================================================================#
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            ka.findAndAddContactsByMid(target)
                            kb.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            kd.findAndAddContactsByMid(target)
                            ke.findAndAddContactsByMid(target)
                            admin.append(target)
                            ka.sendText(msg.to,"Admin Already Added Boss")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Owner add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner add executing"
                _name = msg.text.replace("Owner add @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            ka.findAndAddContactsByMid(target)
                            kb.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            kd.findAndAddContactsByMid(target)
                            ke.findAndAddContactsByMid(target)
                            owner.append(target)
                            ka.sendText(msg.to,"Owner Already Added Boss")
                        except:
                            pass
                print "[Command]Owner add executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ka.sendText(msg.to,"Admin Deleted")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Owner remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner remove executing"
                _name = msg.text.replace("Owner remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.remove(target)
                            ka.sendText(msg.to,"Owner Deleted")
                        except:
                            pass
                print "[Command]Owner remove executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  ka.sendText(msg.to,"The stafflist is empty")
              else:
                  ka.sendText(msg.to,"Tunggu...")
                  mc = "👑 Admin One Piece Bot 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in admin:
                      mc += "[★]" + ka.getContact(mi_d).displayName + "\n"
                  ka.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
#==============================================================================#
            elif msg.text in ["Ownerlist","ownerlist"]:
              if owner == []:
                  ka.sendText(msg.to,"The Owner is empty")
              else:
                  ka.sendText(msg.to,"Tunggu...")
                  mc = "👑 Owner One Piece Bot 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in owner:
                      mc += "[★]" + ka.getContact(mi_d).displayName + "\n"
                  ka.sendText(msg.to,mc)
                  print "[Command]Ownerlist executed"
#==============================================================================#
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)
#==============================================================================#
            elif msg.text in ["List group"]:
                    gid = ka.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = ka.getGroup(i).name
                        h += "╠ [ %s ]\n" % (gn)
		        jml += 1
                    ka.sendText(msg.to,"╔══[ List Group ]\n"+ h +"╚══[ Total Group ] "+str(jml))
#==============================================================================#
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  ka.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ka.findAndAddContactsByMid(msg.from_)
                    ka.inviteIntoGroup(gid,[msg.from_])
                  except:
                    try:
                      kb.findAndAddContactsByMid(msg.from_)
                      kb.inviteIntoGroup(gid,[msg.from_])
                    except:
                      try:
                        kc.findAndAddContactsByMid(msg.from_)
                        kc.inviteIntoGroup(gid,[msg.from_])
                      except:
                        try:
                          kd.findAndAddContactsByMid(msg.from_)
                          kd.inviteIntoGroup(gid,[msg.from_])
                        except:
                          try:
                            ke.findAndAddContactsByMid(msg.from_)
                            ke.inviteIntoGroup(gid,[msg.from_])
                          except:
                            ka.sendText(msg.to,"Mungkin kami tidak di dalaam grup itu")
#==============================================================================#
            elif msg.text in ["Bot out","Leave all group"]:
              if msg.from_ in owner:
                gid = ka.getGroupIdsJoined()
                gid = kb.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = kd.getGroupIdsJoined()
                gid = ke.getGroupIdsJoined()
                for i in gid:
                  ke.leaveGroup(i)
                  kd.leaveGroup(i)
                  kc.leaveGroup(i)
                  kb.leaveGroup(i)
                  ka.leaveGroup(i)
                if wait["lang"] == "JP":
                  ka.sendText(msg.to,"Sayonara")
                else:
                  ka.sendText(msg.to,"He declined all invitations")
#==============================================================================#
            elif msg.text in ["Clear"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = ka.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                          random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                    ka.sendText(msg.to,"I pretended to cancel and canceled.")
#==============================================================================#
            elif msg.text in ["Ourl","Url on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    ka.sendText(msg.to,"Url Sudah Aktif")
                else:
                    ka.sendText(msg.to,"Can not be used outside the group")
#==============================================================================#
            elif msg.text in ["Curl","Url off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    ka.sendText(msg.to,"Url Sudah Di Nonaktifkan")
                else:
                    ka.sendText(msg.to,"Can not be used outside the group")
#==============================================================================#
            elif msg.text in ["Cancelinvite on","cancelinvite on"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == True:
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Berhasil mengaktifkan Cancel Invite")
                  else:
                    ka.sendText(msg.to,"Berhasil mengaktifkan Cancel Invite")
            elif msg.text in ["Cancelinvite off","cancelinvite off"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == False:
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Berhasil menonaktifkan Cancel Invite")
                  else:
                    ka.sendText(msg.to,"Berhasil menonaktifkan Cancel Invite")
#==============================================================================#
            elif msg.text in ["Purge on","purge on","Purge: on","purge: on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan High Protect")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan High Protect")
            elif msg.text in ["Purge off","purge off","Purge: off","purge: off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan High Protect")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan High Protect")
#==============================================================================#
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan Cancel")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Cancel")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan Cancel")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Cancel")
#==============================================================================#     
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan Protect QR")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Protect QR")       
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan Protect QR")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Protect QR")
#==============================================================================#                           
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in owner:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Info Contact")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in owner:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Info Contact")
#==============================================================================#
            elif msg.text in ["Join on","Auto join on"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan Auto Join")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Auto Join")
            elif msg.text in ["Join off","Auto join off"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan Auto Join")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Auto Join")
#==============================================================================#
            elif msg.text in ["Leave on","Autoleave on"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan Auto Leave")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Auto Leave")
            elif msg.text in ["Leave off","Auto leave:off"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan Auto Leave")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Auto Leave")
#==============================================================================#
            elif msg.text in ["Share on","Share on"]:
              if msg.from_ in owner:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan Mode Share")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Mode Share")
            elif msg.text in ["Share off","Share off"]:
              if msg.from_ in owner:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan Mode Share")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Mode Share")
#==============================================================================#
            elif msg.text in ["Sambutan on"]:
              if msg.from_ in owner:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan Sambutan")
            elif msg.text in ["Sambutan off"]:
              if msg.from_ in owner:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan Sambutan")
#==============================================================================#            
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                ka.sendText(msg.to," Berhasil mengaktifkan Simisimi")
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                ka.sendText(msg.to,"Berhasil menonaktifkan Simisimi")
#==============================================================================#
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                ka.sendText(msg.to,"Berhasil mengaktifkan Sider point")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    ka.sendText(msg.to, "Berhasil menonaktifkan Sider point")
                else:
                    ka.sendText(msg.to, "Setting Masih Mode Off\nMohon Maaf")                         
#==============================================================================#
            elif msg.text in ["Status","Set"]:
              if msg.from_ in admin:
                md = "╔═══════════════\n║⭐Protection Status⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                if wait["Protectgr"] == True: md+="║[•]Protect QR Enable\n"
                else: md+="║[•]Protect QR Disable\n"
                if wait["Protectcancl"] == True: md+="║[•]Protect Invite Enable\n"
                else: md+="║[•]Protect Invite Disable\n"
                if wait["Protectcancel"] == True: md+="║[•]Protect Cancel Enable\n"
                else: md+="║[•]Protect Cancel Disable\n"
                if wait["Protectjoin"] == True: md+="║[•]High protect Enable\n"
                else: md+="║[•]High protect Disable\n"
                if wait["contact"] == True: md+="║[•]Contact ✔\n"
                else: md+="║[•]Contact ✖\n"
                if wait["autoJoin"] == True: md+="║[•]Auto Join ✔\n"
                else: md +="║[•]Auto Join ✖\n"
                if wait["leaveRoom"] == True: md+="║[•]Auto Leave ✔\n"
                else: md+="║[•]Auto Leave ✖\n"
                if wait["timeline"] == True: md+="║[•]Share ✔\n"
                else: md+="║[•]Share ✖\n"
                if wait["Sambutan"] == True: md+="║[•]Sambutan ✔\n"
                else: md+="║[•]Sambutan ✖\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║One Piece Protect\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                ka.sendText(msg.to,md)
              else:
                ka.sendText(msg.to,"This Command Only For Admin & Owner")
#==============================================================================#
            elif msg.text in ["Tagall","Tag all"]:
              if msg.from_ in owner:
                  group = ka.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ka.sendMessage(msg)
                  except Exception as error:
                      print error
#==============================================================================#
            elif msg.text == "Lurking on":
              if msg.from_ in owner:
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if msg.to in read['readPoint']:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            ka.sendText(msg.to,"Lurking already on")
                else:
                    try:
                        del read['readPoint'][msg.to]
                        del read['readMember'][msg.to]
                        del read['readTime'][msg.to]
                    except:
                        pass
                    read['readPoint'][msg.to] = msg.id
                    read['readMember'][msg.to] = ""
                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    read['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                        ka.sendText(msg.to, "Set reading point:\n" + readTime)
                            
            elif msg.text == "Lurking off":
              if msg.from_ in owner:
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if msg.to not in read['readPoint']:
                    ka.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                    except:
                          pass
                    ka.sendText(msg.to, "Delete reading point:\n" + readTime)
    
            elif msg.text == "Lurking reset":
              if msg.from_ in owner:
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if msg.to in read["readPoint"]:
                    try:
                        read["readPoint"][msg.to] = True
                        read["readMember"][msg.to] = {}
                        read["readTime"][msg.to] = readTime
                        read["ROM"][msg.to] = {}
                    except:
                        pass
                    ka.sendText(msg.to, "Reset reading point:\n" + readTime)
                else:
                    ka.sendText(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
            elif msg.text == "Lurking":
              if msg.from_ in owner:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                        if read["ROM"][msg.to].items() == []:
                             ka.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][msg.to].items():
                                chiya.append(rom[1])
                                   
                            cmem = ka.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
                        msg.text = xpesan+ zxc + "\nLurking time: \n" + readTime
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        msg.contentMetadata = lol
                        try:
                          ka.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
                    else:
                        ka.sendText(msg.to, "Lurking has not been set.")
#==============================================================================#     
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = ka.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ka.updateGroup(x)
                    gurl = ka.reissueGroupTicket(msg.to)
                    ka.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can't be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
              else:
                ka.sendText(msg.to,"This Command Only For Admin & Owner")
#==============================================================================#
            elif msg.text in ["Masuk","Bot in"]:
              if msg.from_ in owner:
                G = ka.getGroup(msg.to)
                ginfo = ka.getGroup(msg.to)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                invsend = 0
                Ticket = ka.reissueGroupTicket(msg.to)
                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                G = ka.getGroup(msg.to)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
                print "Semua Sudah Lengkap"
#==============================================================================#
            elif msg.text in ["timeline"]:
		try:
                    url = ka.activity(limit=10)
		    ka.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
#==============================================================================#
            elif msg.text in ["Keluar","Get out","Out"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = ka.getGroup(msg.to)
                    try:
                        ke.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                    except:
                        pass
#==============================================================================#
            elif msg.text in ["Absen"]:
              if msg.from_ in admin:
                ka.sendText(msg.to,"ルフィ😭")
                kb.sendText(msg.to,"ゾーラー😭")
                kc.sendText(msg.to,"サンジ😭")
                kd.sendText(msg.to,"ウソップ😭")
                ke.sendText(msg.to,"チョッパー😭")
#==============================================================================#
            elif msg.text.lower() in ["respon"]:
                ka.sendText(msg.to,responsename)
                kb.sendText(msg.to,responsename2)
                kc.sendText(msg.to,responsename3)
                kd.sendText(msg.to,responsename4)
                ke.sendText(msg.to,responsename5)
#==============================================================================#
            elif msg.text.lower() in ["Sp","Speed","sp","speed"]:
                fake=["0.002253985673451seconds"]
                fspeed=random.choice(fake)
                ka.sendText(msg.to," Progress.....")
                ka.sendText(msg.to,(fspeed)) 
#==============================================================================#
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    ka.sendText(msg.to,"Nothing Banned User")
                else:
                    ka.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "→" +ka.getContact(mi_d).displayName + "\n"
                    ka.sendText(msg.to,mc)
#==============================================================================#
            elif msg.text in ["Clear ban"]:
              if msg.from_ in owner:
                wait["blacklist"] = {}
                ka.sendText(msg.to,"Succes Clear Blacklist Boss")
#==============================================================================#
            elif "zhueexp" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("zhueexp","")
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    ka.sendText(msg.to,"Sampai jumpaa~")
                    kb.sendText(msg.to,"Dadaaah ~~ ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ka.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots or owner:
                            if target in owner:
                              pass
                            elif target in admin:
                              pass
                            elif target in Bots:
                              pass
                            else:
                              try:
                                klist=[ka,kb,kc,kd,ke]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                              except:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
#==============================================================================#
            elif msg.text in ["Bot restart"]:
              if msg.from_ in owner:
    	          ka.sendText(msg.to, "Kami Siap Restart\nWaktu Restart Sekitar 10 Detik ")
                  restart_program()
              else:
                ka.sendText(msg.to,"This Command Only For Owner")
 #==============================================================================#
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						ka.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						ka.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						ka.sendAudioWithURL(msg.to,abc)
						ka.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
#==============================================================================#
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ka.sendText(msg.to, hasil)
                except Exception as wak:
                        ka.sendText(msg.to, str(wak))
#==============================================================================#
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    ka.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    ka.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	ka.sendText(msg.to, str(njer))
#==============================================================================#
            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ka.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    ka.sendText(msg.to,"Could not find it")
#==============================================================================#
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = ka.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#  
            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                ka.sendText(msg.to,"Sedang Mencari...")
                ka.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                ka.sendText(msg.to,"Tuh Linknya Kak (^_^)")
#==============================================================================#
            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ka.sendMessage(msg)
#==============================================================================#
            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")                

            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ka.sendImageWithURL(msg.to,path)
                except:
                    pass
#==============================================================================#
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                ka.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                ka.sendText(msg.to, A)
#==============================================================================#
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ka.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ka.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
#==============================================================================#
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                ka.sendText(msg.to,van)
#==============================================================================#
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = ka.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ka.sendMessage(msg)
#==============================================================================#
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        ka.removeAllMessages(op.param2)
                        kb.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        ke.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        ka.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        ka.sendText(msg.to,"Error")
#==============================================================================#
            elif msg.text in ["Glist"]:
              if msg.from_ in owner:
                ka.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = ka.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠" + "%s\n" % (ka.getGroup(i).name +"▶["+str(len(ka.getGroup(i).members))+"]")
                ka.sendText(msg.to,"╔════[ Glist ]════\n" + h + "╠════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚════[ Glist ]════")

            elif msg.text in ["Glistmid"]:   
              if msg.from_ in owner:
                gruplist = ke.getGroupIdsJoined()
                kontak = ke.getGroups(gruplist)
                num=1
                msgs="════════List GrupMid══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n══════List GrupMid════l═══\n\nTotal Grup : %i" % len(kontak)
                ke.sendText(msg.to, msgs)
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
           
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
#==============================================================================#                                           
        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = ka.fetchOps(ka.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ka.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ka.Poll.rev = max(ka.Poll.rev, Op.revision)
            bot(Op)

