# coding: utf-8
from slackclient import SlackClient
import requests
import json
import re
import datetime
import time
import logging
import keys
# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)
slack_token =keys.slack_token
client = SlackClient(slack_token)
s = requests.Session()
#data=логин и пароль от бота на тестовом джи тесте
data =keys.data
#ссылка на логин в тестовом джитесте
url = keys.url
try:
  s.post(url, data=data)
  client.api_call('chat.postMessage',
                      channel='U017BN1DYHK',
                      text='ji-test is ok')
  logging.info('ji-test is ok')
except:
  client.api_call('chat.postMessage',
                      channel='U017BN1DYHK',
                      text='cannot connect to jira-test')
  logging.info('cannot connect to jira-test')
data2 =keys.data2
url2 = keys.url2
try:
  s.post(url2, data=data2)
  client.api_call('chat.postMessage',
                      channel='U017BN1DYHK',
                      text='ji is ok')
  logging.info('ji is ok')
except:
  client.api_call('chat.postMessage',
                      channel='U017BN1DYHK',
                      text='cannot connect to jira')
  logging.info('cannot connect to jira')
curlic = keys.curlic
if client.rtm_connect():
    client.api_call('chat.postMessage',
                      channel='U017BN1DYHK',
                      text='It s ok, connected')
    logging.info('It s ok, connected')
    while client.server.connected is True:
        for data in client.rtm_read():
            if "type" in data and data["type"] == "message":
              if 'user' in data and '<@'+client.api_call("auth.test")["user_id"]+'>' in data['text']:
                user=data['user']
                yui=requests.get('https://slack.com/api/users.info?token='+slack_token+'&user='+user+'&pretty=1') 
                try:
                  json_answ=json.loads(yui.text)
                except:
                  print(yui.text)
                  break

                try:
                  command= '>'.join(data['text'].split('>')[1:])
                  command=' '.join(command.split())
                  client.api_call('chat.postMessage',
                      channel='U017BN1DYHK',
                      text='got message from:'+json_answ['user']['profile']['email']+'\n'+command)
                  logging.info('got message from:'+json_answ['user']['profile']['email']+'\n'+command+'\nTime=')
                  logging.info(datetime.datetime.now())
                except:
                  break
                channel_id = data['channel']
                thread_ts = data['ts']
                #у этих людей почта с другим доменом, для них меняем домен
                admins={'kolsanovgn','baryshnikovve','severtsevaaa'}
                #в этот список добавте команду, елси эта команда в одно слово(без ключей)
                one_word_commands=['my_email','my_tasks','help','strategy','library','agile','customize','get_api']
                #сюда добавляйте команды с ключами.
                other_commands=['comment [key] [message]','show_comments [key]']
                all_commands=one_word_commands+['comment']
                if command.split(' ')[0]=='test':
                  command=' '.join(command.split(' ')[1:])
                  curlic = "https://ji-test.alfastrah.ru/"
                else:
                  curlic = keys.curlic
                reqji=s.get(curlic+'?os_authType=basic')
                if(reqji.status_code==401):
                  client.api_call('chat.postMessage',
                      channel='U017BN1DYHK',
                      text='back to jira test')
                  try:
                    s.post(keys.url2, data=keys.data2)
                  except:
                    print('cannot connect to jira')
                    break
                reqjitest=s.get('https://ji-test.alfastrah.ru/?os_authType=basic')
                if(reqjitest.status_code==401):
                  try:
                    s.post(keys.url, data=keys.data)
                    client.api_call('chat.postMessage',
                       channel='U017BN1DYHK',
                       text='back to jira')
                  except:
                    print('cannot connect to jira-test')
                #здесь начинаются команды в одно слово
                if command.split(' ')[0] in one_word_commands:
                    #сюда можно добавить команду
                    if command.split(' ')[0]=='strategy':
                      client.api_call('chat.postMessage',
                      channel=channel_id,
                      text='https://wiki.alfastrah.ru/pages/viewpage.action?pageId=38798426',
                      thread_ts=thread_ts,
                      icon_emoji=':+1:',
                      username='this is your strategy__bot'
                      )
                    if command.split(' ')[0]=='library':
                      client.api_call('chat.postMessage',
                      channel=channel_id,
                      text='>You can get books from 2 sources:\n>k:\Library\n>https://wiki.alfastrah.ru/pages/viewpage.action?pageId=63537531',
                      thread_ts=thread_ts,
                      icon_emoji=':+1:',
                      username='this is your library__bot'
                      )
                    if command.split(' ')[0]=='agile':
                      client.api_call('chat.postMessage',
                      channel=channel_id,
                      text='https://wiki.alfastrah.ru/pages/viewpage.action?pageId=53044196',
                      thread_ts=thread_ts,
                      icon_emoji=':+1:',
                      username='this is your agile__bot'
                      )
                    if command.split(' ')[0]=='customize':
                      client.api_call('chat.postMessage',
                      channel=channel_id,
                      text='In progress',
                      thread_ts=thread_ts,
                      icon_emoji=':+1:',
                      username='this is your customize__bot'
                      )
                    if command.split(' ')[0]=='get_api':
                      client.api_call('chat.postMessage',
                      channel=channel_id,
                      text='In progress[1]',
                      thread_ts=thread_ts,
                      icon_emoji=':+1:',
                      username='this is your get_api__bot'
                      )

                    if command.split(' ')[0]=='my_email':
                      yui=requests.get('https://slack.com/api/users.info?token='+slack_token+'&user='+user+'&pretty=1')
                      try:
                        json_answ=json.loads(yui.text)
                      except:
                        print(yui.text)
                        break
                      client.api_call('chat.postMessage',
                      channel=channel_id,
                      text="your email, <@{}>, is ".format(user)+json_answ['user']['profile']['email'],
                      thread_ts=thread_ts,
                      icon_emoji=':+1:',
                      username='this is your email_bot'
                      )
                    if command.split(' ')[0]=='help':
                      client.api_call('chat.postMessage',
                      channel=channel_id,
                      text='My commands are:\n'+'\n'.join(one_word_commands)+'\n'+'\n'.join(other_commands),
                      thread_ts=thread_ts,
                      icon_emoji=':male-doctor:',
                      username='this is your help__bot'
                      )

                    if command.split(' ')[0]=='my_tasks':
                        #some code there
                        try:
                         yui=requests.get('https://slack.com/api/users.info?token='+slack_token+'&user='+user+'&pretty=1')
                        except:
                         client.api_call('chat.postMessage',
                         channel=channel_id,
                         text='something went wrong with your slack',
                         thread_ts=thread_ts,
                         icon_emoji=':x:',
                         username='this is your ERROR__bot'
                         )
                        admins={'kolsanovgn','baryshnikovve','severtsevaaa'}
                        try:
                          json_answ=json.loads(yui.text)
                        except:
                          print(yui.text)
                          break
                        email=json_answ['user']['profile']['email']
                        emai=email.split('@')[0]+'%40'+email.split('@')[1]
                        try:
                           if email.split('@')[0] in admins:
                             emai=email.split('@')[0]+'%40'+'vesta.ru'
                        except:
                           client.api_call('chat.postMessage',
                           channel=channel_id,
                           text='something went wrong with your email',
                           thread_ts=thread_ts,
                           icon_emoji=':x:',
                           username='this is your ERROR__bot'
                           )
                        s.cookies
                        try:
                           req=s.get(curlic+'rest/api/2/user?username='+emai)
                        except:
                           print('beda s dostupom')
                        try:
                          json_answ=json.loads(req.text)
                        except:
                          print(req.text)
                          client.api_call('chat.postMessage',
                          channel=channel_id,
                          text='Something went wrong when try access your tasks. Mb ya not registred in'+curlic,
                          thread_ts=thread_ts
                          )
                          logging.info('problem with encoding jira')
                          break
                        inic=json_answ['displayName'].split(' ')[0]+'%20'+json_answ['displayName'].split(' ')[1]+'%20'+json_answ['displayName'].split(' ')[2]+'"'
                        try:
                          req2=s.get(curlic+'rest/api/2/search?jql=assignee="'+inic)
                          json_answ=json.loads(req2.text)
                        except:
                          print(req2.text)
                          client.api_call('chat.postMessage',
                          channel=channel_id,
                          text='Something went wrong when try access your tasks. Mb ya not registred in'+curlic,
                          thread_ts=thread_ts,
                          icon_emoji=':x:',
                          username='this is your ERROR__bot'
                          )
                          break
                        num_tas=len(json_answ['issues'])
                        k=0
                        vivod=' '
                        for self in range(num_tas):
                          if json_answ['issues'][self]['fields']['status']['name']!=u'Закрыт' and json_answ['issues'][self]['fields']['status']['name']!=u'Сделано':
                           k+=1
                           vivod+='\n>'+json_answ['issues'][self]['key']+'\n>'+json_answ['issues'][self]['fields']['summary']+'.\n Link:   '+curlic+'browse/'+json_answ['issues'][self]['key']+'\n'*3
                        if k==0:
                           vivod='You have '+str(k)+' task(s). You are free now'+'\n'
                        else:
                            vivod='You have '+str(k)+' task(s). '+vivod
                        client.api_call('chat.postMessage',
                        channel=channel_id,
                        text=vivod,
                        thread_ts=thread_ts,
                        icon_emoji=':+1:',
                        username='this is your tasks_bot'
                        )
                else:
                   #здесь идут команды с ключами.  command.split(' ')[0]-первое слово. ключи идут соответственно [1], [2] и тд
                   if command.split(' ')[0]=='comment':
                        if len(command.split(' '))>2:
                           yui=requests.get('https://slack.com/api/users.info?token='+slack_token+'&user='+user+'&pretty=1')
                           try:
                             json_answ=json.loads(yui.text)
                           except:
                             print(yui.text)
                             break
                           if json_answ['user']['profile']['email'].split('@')[0] in admins:
                              emai=json_answ['user']['profile']['email'].split('@')[0]+'@vesta.ru'
                           else:
                              emai=json_answ['user']['profile']['email']
                           headers = {
                           'Content-type': 'text/json',
                           }
                           commen=' '.join(command.split(' ')[2:])
                           if commen[0]==commen[-1]=="'":
                             commen=commen[1:-2]
                           params = (
                           ('comment',''),
                           )
                           data = {"user": emai,
                           "issueKey": command.split(' ')[1],
                           "comment":  commen
                           }
                           try:
                             response = s.post(curlic+'rest/scriptrunner/latest/custom/make',
                             headers=headers,
                             params=params,
                             json=data,
                             verify=False)
                             result=json.loads(response.text)
                           except:
                              client.api_call('chat.postMessage',
                              channel=channel_id,
                              text='its hard access to joe casino',
                              thread_ts=thread_ts,
                              icon_emoji=':x:',
                              username='this is your ERROR_bot')
                              logging.info('cant get access to'+curlic)
                              break
                           try:
                            if result[0]=='Done':
                              #if good
                              client.api_call('chat.postMessage',
                              channel=channel_id,
                              text='Done, its ok. You can check it there:\n'+curlic+'browse/'+ command.split(' ')[1],
                              thread_ts=thread_ts,
                              icon_emoji=':+1:',
                              username='this is your comment_bot'
                              )

                            else:
                             if result[0]=='User has no permission to add comment':
                              client.api_call('chat.postMessage',
                              channel=channel_id,
                              text='access denied',                      
                              thread_ts=thread_ts,
                              icon_emoji=':x:',
                              username='this is your ERROR_bot'

                              )
                             else:
                              #if bad
                              client.api_call('chat.postMessage',
                              channel=channel_id,
                              text='something went wrong',
                              thread_ts=thread_ts,
                              icon_emoji=':X:',
                              username='this is your ERROR_bot')
                              logging.info('something went wrong with commenting')
                           except:
                              client.api_call('chat.postMessage',
                              channel=channel_id,
                              text="Can't find this issue ",
                              thread_ts=thread_ts,
                              icon_emoji=':x:',
                              username='this is your ERROR_bot')
                              logging.info('issue not found')
                        else:
                              client.api_call('chat.postMessage',
                              channel=channel_id,
                              text="Not correct input of this command.\nCorrect example: comment *Issue_id input_text*",
                              thread_ts=thread_ts,
                              icon_emoji=':x:',
                              username='this is your ERROR_bot')
                              logging.info('incorrect input')

                   else:
                    if command.split(' ')[0]=='show_comments':
                      if len(command.split(' '))>1:
                         try:
                           res=s.get(curlic+'rest/api/2/issue/'+ command.split(' ')[1])
                         except:
                           client.api_call('chat.postMessage',
                           channel=channel_id,
                           text='cannot find this issue1',
                           thread_ts=thread_ts,
                           icon_emoji=':x:',
                           username='this is your ERROR_bot'
                           )
                           logging.info('issue wasnt found')
                           break
                         try:
                           json_answ=json.loads(res.text)
                         except:
                           print(res.text)
                           break
                         text=''
                         try:
                          if len(json_answ['fields']['comment']['comments'])==0:
                            text='There is no comments in this issue'
                          else:
                           for i in range(len(json_answ['fields']['comment']['comments'])):
                            text+='*'+json_answ['fields']['comment']['comments'][i]['author']['displayName']+'*:\n'+json_answ['fields']['comment']['comments'][i]['body']+'\n'*2
                         except:
                           client.api_call('chat.postMessage',
                           channel=channel_id,
                           text='cannot find this issue. Maybe something wrong?',
                           thread_ts=thread_ts,
                           icon_emoji=':x:',
                           username='this is your ERROR_bot')
                           logging.info('cant find issue(2)')
                           break
                         client.api_call('chat.postMessage',
                         channel=channel_id,
                         text=text,
                         thread_ts=thread_ts,
                         icon_emoji=':face_with_monocle:',
                         username='this is your show comments_bot')
                      else:
                         client.api_call('chat.postMessage',
                         channel=channel_id,
                         text='Wrong input format',
                         thread_ts=thread_ts,
                         icon_emoji=':x:',
                         username='this is your ERROR_bot')
                         logging.info('input format was wrong')
                    else:
                      #здесь если сообшение боту пустое
                      if command=="":
                        client.api_call('chat.postMessage',
                        channel=channel_id,
                        text='empty command!',
                        thread_ts=thread_ts,
                        icon_emoji=':x:',
                        username='this is your ERROR_bot'
                        )
                        logging.info('empty message')
                      else:
                        #если не удалось найти команду в списке всех команд
                        client.api_call('chat.postMessage',
                        channel=channel_id,
                        text='dont undertand command: *'+command.split(' ')[0]+'*\nTry command *help*',
                        thread_ts=thread_ts,
                        icon_emoji=':x:',
                        username='this is your ERROR_bot'
                        )
                        logging.info('user tried command '+command.split(' ')[0]+' but bot cant find this command')           
else: 
  print ("Connection Failed")
