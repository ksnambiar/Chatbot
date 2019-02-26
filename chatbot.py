# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:59:31 2019

@author: Sidharth
"""

#building chatbot with deep nlp

import numpy as np
import tensorflow as tf
import re
import time

####################DATA PRE-PROCESSING##############################3
lines = open("movie_lines.txt",encoding="utf-8", errors = 'ignore').read().split('\n')
conversations = open("movie_conversations.txt",encoding="utf-8", errors = 'ignore').read().split('\n')

lines