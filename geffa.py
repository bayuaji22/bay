# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile,pytz

cl = LINETCR.LINE()
cl.login(token="ErjxAqRcaD9BQaQvAvq7.RNPnQdVDEHss6kJitzRcPW.dDx46mXFJT6X1glqdTNN9uJyAbrBgGPyY9DEWRTj4mI=")
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔═══[ Help Media ]
╠ Music
╠ /lirik
╠ /ig
╠ Image
╠ Youtubelink:
╠ Searchid:
╠ Kalender
╠ Tr-en
╠ Tr-id
╠ En@id
╠ Id@en
╠ /kapan
╠ /berapa
╠ /berapakah
╠ /hari
╠ /apakah
╠ Playstore
╠ Say-id
╠ Say-en
╠ Say welcome
╠ Gift
╠═══[ Help Setting ]
╠ Autoadd on/off
╠ Join on/off
╠ Leave on/off
╠ Sambutan on/off
╠ Alwaysread on/off
╠ Contact on/off
╠ Sider: on/off
╠ Respon1/2/3 on/off
╠═══[ Help Group ]
╠ Ginfo
╠ Tag
╠ Lurking on/off
╠ Lurking reset
╠ Lurking
╠ Bye
╠═══[ Help Self ]
╠ Set
╠ Key/Help
╠ Speed
╠ Runtime
╠ Bot restart
╠ Mycopy
╠ Mybackup
╚═══[ Help Finish ]
"""
KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
admin=["uae7a4da83bdd7a1492e8a8c84d9ac2a7"]

contact = cl.getProfile()
backup1 = cl.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

wait = {
    "contact":False,
    "autoJoin":True,
    "autoCancel":{"on":True,"members":1},
    "autoAdd":False,
    "copy":{},
    "steal":{},
    "detectMention":False,
    "detectMention2":True,
    "detectMention3":False,
    "lang":"JP",
    "Sambutan":False,
    "alwaysRead":False,    
    "Sider":{},
    "LeaveRoom":True
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

setTime = {}
setTime = read['readTime']
mulai = time.time() 
#==============================================================================#
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

def cms(string, commands): 
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

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMention(op.param1, op.param1, "Halo", ", terimakasih telah menambahkan saya sebagai teman")
#==============================================================================#
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#==============================================================================#
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "oy " + "[ " + Name + " ]" + "\nJangan Ngintip Aja\nSini ikutan Chat😁   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "ahay " + "[ " + Name + " ]" + "\nKetauan Ngintip \nSini ikutan Chat😁   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "Haii " + "[ " + Name + " ]" + "\nJangan Ngintip Aja\nSini ikutan Chat😁   ")
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
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)
#==============================================================================#
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#==============================================================================#
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDemoga Betah ^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)  
            cl.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }                
            cl.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
#==============================================================================#
        if op.type == 26:
            msg = op.message                                          
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Oit!",cName + " Nggak Usah Tag-Tag! Penting Langsung Pm Aja"," Lagi Off", cName + " lagi kerja"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "165",
                                                       "STKPKGID": "2",
                                                       "STKVER": "100" }
                                  cl.sendMessage(msg)                     
                                  break   
#==============================================================================#    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Saduk i we " + cName + " ngtag2 ae ","Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Tag Mulu Lo asem!","Dia Lagi Off", cName + " Kenapa Tag? Kangen?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                                               
                                  break
#==============================================================================#                 
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Nah ☆☞ " + cName + " ☜☆"]
                    balas1 = "Ini Foto Si Jones Yang Suka Ngetag⬇️⬇️⬇️"
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,balas1)
                                  cl.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "163",
                                                       "STKPKGID": "2",
                                                       "STKVER": "100" }
                                  cl.sendMessage(msg)                                
                                  break 
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
#==============================================================================#
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
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
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")                       
#==============================================================================#
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Buat Grup Ini")
#==============================================================================#
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
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
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass
#==============================================================================#                                 
            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.CloneContactProfile(target)
                                cl.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break
#==============================================================================#
            elif wait["contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#==============================================================================#
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
#==============================================================================#
            elif msg.text in ["Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#==============================================================================#         
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Berhasil Mengaktifkan Respon1")
		else:
		    cl.sendText(msg.to,"khusus admin")
#==============================================================================#
            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Berhasil Menonaktifkan Respon1")
		else:
		    cl.sendText(msg.to,"khusus admin")	
#==============================================================================#
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Berhasil Mengaktifkan Respon2")
		else:
		    cl.sendText(msg.to,"khusus admin")
#==============================================================================#
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    cl.sendText(msg.to,"Berhasil Menonaktifkan Respon2")
		else:
		    cl.sendText(msg.to,"khusus admin")	    
#==============================================================================#
            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Berhasil Mengaktifkan Respon3")
		else:
		    cl.sendText(msg.to,"khusus admin")
#==============================================================================#
            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    cl.sendText(msg.to,"Berhasil Menonaktifkan Respon3")
		else:
		    cl.sendText(msg.to,"khusus admin")	
#==============================================================================#
            elif msg.text in ["Contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
#==============================================================================#
            elif msg.text in ["Contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
#==============================================================================#
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"Berhasil Mengaktifkan Alwaysread")
#==============================================================================#
            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"Berhasil Menonaktifkan Alwaysread")                
#==============================================================================#
            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Sambutan")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"On")
#==============================================================================#
            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Sambutan")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")                       
#==============================================================================#           
            elif "Sider ok" in msg.text:
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
                cl.sendText(msg.to,"øκ.ακ†ιŦ")
#==============================================================================#
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Berhasil Menonaktifkan Cek Sider")
                else:
                    cl.sendText(msg.to, "Cek Sider Belum Aktif")                         
#==============================================================================#
            elif msg.text in ["Join on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
#==============================================================================#
            elif msg.text in ["Join off"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
#==============================================================================#
            elif msg.text in ["Leave on"]:
              if msg.from_ in admin:
                if wait["LeaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
                else:
                    wait["LeaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
#==============================================================================#
            elif msg.text in ["Leave off"]:
              if msg.from_ in admin:
                if wait["LeaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
                else:
                    wait["LeaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
#==============================================================================#
            elif msg.text in ["Set"]:
              if msg.from_ in admin:
                md = ""
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["detectMention"] == True: md+=" Auto Respon1 : on\n"
                else: md+=" Auto Respon1 : off\n"
                if wait["detectMention2"] == True: md+=" Auto Respon2 : on\n"
                else: md+=" Auto Respon2 : off\n"
                if wait["detectMention3"] == True: md+=" Auto Respon3 : on\n"
                else: md+=" Auto Respon3 : off\n"
                if wait["Sambutan"] == True: md+=" Sambutan : on\n"
                else: md+=" Sambutan : off\n"
                if wait["alwaysRead"] == True: md+=" Auto Read : on\n"
                else: md+=" Auto Read : off\n"
                if wait["Sider"] == True: md+=" Cek Sider : on\n"
                else: md+=" Cek Sider : off\n"
                if wait["LeaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                cl.sendText(msg.to,md)
#==============================================================================#
            elif msg.text in ["Autoadd on"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
                    else:
                        cl.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
#==============================================================================#
            elif msg.text in ["Autoadd off"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
                    else:
                        cl.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
#==============================================================================#
            elif msg.text in ["Tag"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                  summon(msg.to, nama)
                if jml > 100 and jml < 200:
                  for i in range(0, 99):
                    nm1 += [nama[i]]
                  summon(msg.to, nm1)
                  for j in range(100, len(nama)-1):
                    nm2 += [nama[j]]
                  summon(msg.to, nm2)
                if jml > 200  and jml < 500:
                  for i in range(0, 99):
                    nm1 += [nama[i]]
                  summon(msg.to, nm1)
                  for j in range(100, 199):
                    nm2 += [nama[j]]
                  summon(msg.to, nm2)
                  for k in range(200, 299):
                    nm3 += [nama[k]]
                  summon(msg.to, nm3)
                  for l in range(300, 399):
                    nm4 += [nama[l]]
                  summon(msg.to, nm4)
                  for m in range(400, len(nama)-1):
                    nm5 += [nama[m]]
                  summon(msg.to, nm5)
                if jml > 500:
                  print "Terlalu Banyak Men 500+"
                cnt = Message()
                cnt.text = "ʝʊʍʟǟɦ:\n" + str(jml) +  " мємвєяѕ"
                cnt.to = msg.to
                cl.sendMessage(cnt)
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
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
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
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#==============================================================================#
            elif 'Y ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Y ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
#==============================================================================#
            elif 'Yv ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Yv ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        cl.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        cl.sendText(msg.to, "Could not find it")                    


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
#==============================================================================#
            elif msg.text in ["@zhu"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#==============================================================================#
            elif msg.text in ["Bot restart"]:
              if msg.from_ in admin:
    	          cl.sendText(msg.to, "Kami Siap Restart\nWaktu Restart Sekitar 10 Detik ")
                  restart_program()
              else:
                cl.sendText(msg.to,"This Command Only For Owner")
#==============================================================================#
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Berhasil Copy Profile")
                            except Exception as e:
                                print e
#==============================================================================#
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(backup1.pictureStatus)
                    cl.updateProfile(backup1)
                    cl.sendText(msg.to, "Berhasil Backup Profile")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
#==============================================================================#
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#==============================================================================#
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#==============================================================================#
            elif "Sayi " in msg.text:
                say = msg.text.replace("Sayi ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
            elif "Saye " in msg.text:
                say = msg.text.replace("Saye ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
            elif "Sayko " in msg.text:
                say = msg.text.replace("Sayko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")    
                
            elif "Sayjpn " in msg.text:
                say = msg.text.replace("Sayjpn ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")    
#==============================================================================#
            elif msg.text.lower() in ["ge"]:
                beb = "Hadirr 😘 " ,cName + " 􀸂􀆇starry heart􏿿"
                cl.sendText(msg.to,beb)

            elif "Say welcome" in msg.text:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
                
#==============================================================================#
            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                cl.sendText(msg.to,"Link Aplikasi Sudah Terkirim")
#==============================================================================#
            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "warna " in msg.text:
                apk = msg.text.replace("warna ","")
                rnd = ["Pink","Biru","Putih","Merah","Coklat","Belang"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")    
#==============================================================================#
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")   
#==============================================================================#
            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#      
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                
#==============================================================================#
            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
 #==============================================================================#
            elif "Gambar " in msg.text:
                search = msg.text.replace("Gambar ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
#==============================================================================#
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
#==============================================================================#
            elif "Jawa " in msg.text:
                isi = msg.text.replace("Jawa ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='jw')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Sunda " in msg.text:
                isi = msg.text.replace("Sunda ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='su')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)        

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
                
            elif "Trjp " in msg.text:
                isi = msg.text.replace("Trjp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A) 
            
            elif "Trjer " in msg.text:
                isi = msg.text.replace("Trjer ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='de')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)         
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
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)
                
            elif "Id@su" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'su'
                kata = msg.text.replace("Id@su ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke sunda----\n" + "" + result) 
                
            elif "Jw@su" in msg.text:
                bahasa_awal = 'jw'
                bahasa_tujuan = 'su'
                kata = msg.text.replace("Jw@su ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari jawa----\n" + "" + kata + "\n\n----Ke sunda----\n" + "" + result)  
            elif "Su@jw" in msg.text:
                bahasa_awal = 'su'
                bahasa_tujuan = 'jw'
                kata = msg.text.replace("Su@jw ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----sunda----\n" + "" + kata + "\n\n----jawa----\n" + "" + result)       
                
#==============================================================================#
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
                cl.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
#==============================================================================#
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)                
#==============================================================================#      
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)     
#==============================================================================#
            elif msg.text == "cctv ok":
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
                            cl.sendText(msg.to," on")
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
                        cl.sendText(msg.to, "Set reading point:\n" + readTime)
#==============================================================================#
            elif msg.text == "cctv off":
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
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + readTime)
#==============================================================================#
            elif msg.text == "cctv reset":
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
                    cl.sendText(msg.to, "Reset reading point:\n" + readTime)
                else:
                    cl.sendText(msg.to, "Lurking belum diaktifkan ngapain di reset?")
#==============================================================================#          
            elif msg.text == "cctv":
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
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][msg.to].items():
                                chiya.append(rom[1])
                                   
                            cmem = cl.getContacts(chiya)
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
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
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
#------------------------
#------------------------
        if op.type == 26:
            msg = op.message
            if msg.text in ["geff","Angel","angel"]:
                cl.sendText(msg.to,"Hadir")

#------------------------
        if op.type == 59:
            print op
            
    except Exception as error:
        print error
        
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
#------------------------
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
