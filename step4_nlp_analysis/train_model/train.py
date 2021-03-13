#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jane 21 2021
@author: Cindy Tang
"""
from snownlp import sentiment

sentiment.train('negative_dict.txt', 'positive_dict.txt')
sentiment.save('sentiment.marshal')

