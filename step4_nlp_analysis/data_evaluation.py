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
    pos_count = 0
    neg_count = 0
    for line_data in open("/Users/Cindy/PycharmProjects/weibo_analysis_by_Cindy/output/raw_comments/%s_raw_comments.txt" % weibo_name):
        comment = line_data
        s = SnowNLP(comment)
        rates = s.sentiments
        if rates >= 0.5:
            pos_count += 1
        elif rates < 0.5:
            neg_count += 1
        else:
            pass
    return pos_count, neg_count


def get_chart(pos, neg, weibo_name):
    labels = 'Positive Side\n(eg. pray,eulogize and suggestion)', 'Negative Side\n(eg. abuse,sarcasm and indignation)'
    fracs = [pos, neg]
    explode = [0.1, 0]  # 0.1 凸出这部分，
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    # autopilot ，show percet
    plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.savefig("../output/nlp_results/%s_emotions_pie_chart.jpg" % weibo_name, dpi=360)
    plt.show()


if __name__ == "__main__":
    weibo_name = input('请输入需要进行情感分析的微博名：')
    pos, neg = evaluate(weibo_name)
    get_chart(pos, neg, weibo_name)
