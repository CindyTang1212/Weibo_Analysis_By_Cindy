#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jane 21 2021
@author: Cindy Tang
"""
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread


class Word_cloud:
    def __init__(self):
        self.weibo_name = input('请输入你需要制作词云的微博名：')
        self.keywords = {}

    def get_keywords(self):
        input_path = '/Users/Cindy/PycharmProjects/weibo_analysis_by_Cindy/output/word_data/%s_data_full.dat' % self.weibo_name
        f = open(input_path, 'r')
        lyric = f.read()
        result = jieba.analyse.extract_tags(lyric, topK=500, withWeight=True)
        for i in result:
            self.keywords[i[0]] = i[1]

    def generate_image(self):
        image = Image.open('pic/气泡.png')
        graph = np.array(image)
        wc = WordCloud(font_path='Songti.ttc', background_color='White', colormap='Dark2', max_words=200, mask=graph, width=1000, height=1000)
        wc.generate_from_frequencies(self.keywords)
        plt.imshow(wc)
        plt.axis("off")
        plt.show()
        output_path = '../output/word_cloud/%s_wordcloud.png' % self.weibo_name
        wc.to_file(output_path)


if __name__ == "__main__":
    wc = Word_cloud()
    wc.get_keywords()
    wc.generate_image()
