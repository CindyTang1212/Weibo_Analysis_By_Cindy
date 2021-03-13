#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 2021
@author: Cindy Tang
"""
import webbrowser
import sinaweibopy3
import re
import pymysql
import time


class Spider:
    def __init__(self, weibo_id, weibo_name):
        self.weibo_id = weibo_id
        self.weibo_name = weibo_name
        self.client = sinaweibopy3.APIClient(app_key='1431227519', app_secret='02c1e46a8699199ea98fb47ddbacc92b',
                                             redirect_uri='https://api.weibo.com/oauth2/default.html')
        self.count = 0
        self.page = 0
        self.comments = []
        self.gender = []

    def code_prepare(self):
        webbrowser.open_new(self.client.get_authorize_url())
        result = self.client.request_access_token(input("please input code : "))
        self.client.set_access_token(result.access_token, result.expires_in)

    def db_prepare(self, user, password):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user=user, password=password,
                                        db='weibo_comments',
                                        unix_socket='/tmp/mysql.sock', use_unicode=True, charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.conn.cursor()
        except:
            print('数据库连接不成功')
        sql_create_table = "CREATE TABLE IF NOT EXISTS `%s`(" \
                           "`编号` INT UNSIGNED," \
                           "`用户ID` VARCHAR(100) NOT NULL," \
                           "`用户性别` VARCHAR(100) NOT NULL," \
                           "`评论内容` VARCHAR(1000) NOT NULL" \
                           ") CHARSET = utf8mb4" % self.weibo_name
        self.cur.execute(sql_create_table)
        print('表格%s-建立成功' % self.weibo_name)

    def get_and_insert_data(self):
        while True:
            try:
                self.page = self.page + 1
                print('开始爬取第%d页数据' % self.page, end='......')
                c = self.client.get_comments(id=str(self.weibo_id), count=200, page=self.page)['comments']
                for info in c:
                    self.count = self.count + 1
                    name = str(info.user.name)
                    gender = str(info.user.gender)
                    text = re.sub('回复.*?:', '', str(info.text))
                    if len(text) != 0:
                        sql = "insert into `" + self.weibo_name + "` (编号, 用户ID, 用户性别, 评论内容) values(%s, %s, %s, %s)"
                        par = (self.count, name, gender, text)
                        try:
                            self.cur.execute(sql, par)
                        except pymysql.err.InternalError as ex:
                            print('ERROR1 : %s' % ex)
                            data_missed = True
                            exit()
                        self.conn.commit()
                time.sleep(1)
            except TypeError as ex:
                print('爬取完成，共获得%d条数据' % self.count)
                break
            print('第%d页数据爬取成功！' % self.page)

    def get_comments_list(self):
        sql_select_comments = 'select 评论内容 from ' + self.weibo_name
        self.cur.execute(sql_select_comments)
        result = self.cur.fetchall()
        for info in result:
            self.comments.append(info['评论内容'])
        return self.comments

    def get_gender(self):
        sql_select_gender = 'select 用户性别 from ' + self.weibo_name
        self.cur.execute(sql_select_gender)
        result = self.cur.fetchall()
        for info in result:
            self.gender.append(info['用户性别'])
        return self.gender
