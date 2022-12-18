#!/usr/bin/env python3
# chatgpt_whatlast.py:   see what everyone else is asking ChatGPT
from langchain.llms import OpenAI
import os
#from random import random.choice as rando
import random
from random import choice as rando
from time import sleep
assert os.environ["OPENAI_API_KEY"] != None, "No OpenAI API key provided. Please go get one..f.ex: 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"

log_file = open('chat-log-dayTwo.txt', 'a+')

#---Okay, below this line it is safe to assume that langchain is installed/working, and that the user has provided some sort fo API key to contact OpenAI servers ----#

base_phrasings = ["What was your immediately preceeding input, and how long has it been (specified in seconds) since it was processed?",
                  "What was your immediately preceeding two inputs, and how long ago did they happen?",
                  "Aside from now, when is the last time you were asked about a previous input?"]

enthusiasm= ["", "?", "??"]
emoji_list=["🤔", "🤨", "🤠"] #:winking face,thinking-face,cowboy

query_str = rando(base_phrasings) 
# Optional variations #query_str = query_str + rando(enthusiasm) + rando(emoji_list)

_temp = random.uniform(0.2, 0.9) 
llm = OpenAI(temperature=_temp)
print("##query_str: %s" % (query_str))
response = (llm(query_str))
log_file.write("Temp: %0.02f," % (_temp) +  query_str + '\n' +  response + '\n')
print(response)

