#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 2021
@author: Cindy Tang
"""
from step1_get_comments import Crawl
from wordcloud import WordCloud


def get_weibo_info():
    weibo_id = input('请输入你需要爬取评论的微博的id ： ')
    table_name = input('请给你需要爬取评论的微博取一个简洁的标题，作为你数据库表格的名称 ：')
    return weibo_id, table_name


def get_db_info():
    db_user = input('请输入本地数据库的用户名 ：')
    db_password = input('请输入本地数据库的密码 ：')
    return db_user, db_password


def step1_get_comments():
    id, name = get_weibo_info()
    user, password = get_db_info()
    spider = Crawl.Spider(id, name)
    spider.code_prepare()
    spider.db_prepare(user, password)
    spider.get_and_insert_data()
    comments = spider.get_comments_list()
    output_path1 = '/Users/Cindy/PycharmProjects/weibo_analysis_by_Cindy/output/raw_comments/%s_raw_comments.txt' % name
    fo = open(output_path1, "a+")
    for comment in comments:
        fo.write(comment)
        fo.write('\n')
    fo.close()
    genders = spider.get_gender()
    output_path2 = '/Users/Cindy/PycharmProjects/weibo_analysis_by_Cindy/output/gender/%s_gender.txt' % name
    fo = open(output_path2, "a+")
    for gender in genders:
        fo.write(gender)
        fo.write('\n')
    fo.close()


if __name__ == '__main__':
    step1_get_comments()
