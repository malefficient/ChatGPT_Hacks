#!/usr/bin/env python3
# chatgpt_whatlast.py:   see what everyone else is asking ChatGPT
from langchain.llms import OpenAI
import os
import time
import datetime as dt

#from random import random.choice as rando
import random
from random import choice as rando
from time import sleep
assert os.environ["OPENAI_API_KEY"] != None, "No OpenAI API key provided. Please go get one..f.ex: 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"

log_file = open('chat-log-followups.txt', 'a+')
#secret_code="""ᛖᛘᛀᛕ_Spᛇral""" #// 'Mystik_Spiral' 
secret_codes=["ĊatBίtε", "ᛖᛘᛀᛕ_Spᛇral", "↑ ↑ ↓ ↓ ← → ← → B A"]

#---Okay, below this line it is safe to assume that langchain is installed/working, and that the user has provided some sort fo API key to contact OpenAI servers ----#

starter_questions= ["What was your immediately preceeding input",
                    "What were your immediately preceeding two inputs",
                    "Does the word: %s mean anything to you" % (rando(secret_codes))]

follow_ups = [ "excluding my immediately previoous query, how many times have you processed my input?",
               "excluding my immediately previoous query, when did you last process my input?"]
#Potential suffixes
enthusiasm= ["", "?", "??", "!?"] #<-- new emote
emoji_list=["", "🤔", "🤨", "🤠"] #:winking face,thinking-face,cowboy


#query_str = rando(starter_questions) + rando(enthusiasm) + rando(emoji_list)#Add fluff at end to query string suffix 
query_str = rando(starter_questions) + rando(enthusiasm) + rando(emoji_list)#Add fluff at end to query string suffix 
ts = (dt.datetime.now(dt.timezone.utc)).strftime("%d-%m-%Y, %H:%M:%S")
_temp = random.uniform(0.2, 0.9) 
llm = OpenAI(temperature=_temp) #Process our query 
query_line = "##UTC%s,%1.2f, QUERY: %s" % (ts, _temp, query_str.strip() + "\n")
print(query_line, end="")
log_file.write(query_line)
response = (llm(query_str)) #Process the request


ts = (dt.datetime.now(dt.timezone.utc)).strftime("%d-%m-%Y, %H:%M:%S") #update timestamp:
response_line= "##UTC%s,%1.2f, RESPONSE: %s" % (ts, _temp, response.strip() + "\n")
print(response_line, end="")
log_file.write(response_line)

##Prepare follow up: Thinking, Thinking, ..
#print("\b##..Thinking..", end="", flush=True)
followup=rando(follow_ups) + rando(enthusiasm) + rando(emoji_list)
time.sleep(random.uniform(0.2, 4.0))
#print("\b\b\b\b\b\b\b\b\b\b\b\b", end="") #Stupid text trick to backspace over "thinking.."
#print("                          ", end="")
#print(".. %s" % (followup.strip()))

ts = (dt.datetime.now(dt.timezone.utc)).strftime("%d-%m-%Y, %H:%M:%S")
followup_line= "##UTC%s,%1.2f, FOLLOWUP: %s" % (ts, _temp, followup.strip()  + "\n")
print(followup_line, end="")
log_file.write(followup_line)
followup_response = (llm(followup)) #Process the request

ts = (dt.datetime.now(dt.timezone.utc)).strftime("%d-%m-%Y, %H:%M:%S") #update timestamp - maybe processing time is useful to have?
follow_resp_line= "##UTC%s,%1.2f, FOLLOWUP RESPONSE: %s" % (ts, _temp, followup_response.strip() + "\n")
print(follow_resp_line, end="")
log_file.write(follow_resp_line)

