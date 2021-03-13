#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 22 2021
@author: Cindy Tang
"""
# from snowplow import sentiment
# import numpy as np
from snownlp import SnowNLP
# from snownlp.sentiment import Sentiment
import matplotlib.pyplot as plt


def evaluate(weibo_name):
    comment = []
    male = 0
    famale = 0
    for line_data in open("/Users/Cindy/PycharmProjects/weibo_analysis_by_Cindy/output/gender/%s_gender.txt" % weibo_name):
        gender = line_data
        if gender == 'm\n':
            male += 1
        elif gender == 'f\n':
            famale += 1
        else:
            pass
    return male, famale


def get_chart(male, famale, weibo_name):
    labels = 'Male', 'Famale'
    fracs = [male, famale]
    explode = [0.1, 0]  # 0.1 凸出这部分，
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    # autopilot ，show percet
    plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.savefig("../output/gender/%s_gender_chart.jpg" % weibo_name, dpi=360)
    plt.show()


if __name__ == "__main__":
    weibo_name = input('请输入需要进行性别分析的微博名：')
    male, famale = evaluate(weibo_name)
    get_chart(male, famale, weibo_name)
