from jieba import analyse

tfidf = analyse.extract_tags


def extract_keywords(weibo_name):
    input_path = '../output/word_data/%s_data_full.dat' % weibo_name
    for line in open(input_path):
        text = line
        keywords = tfidf(topK=100, sentence=text)
        result = []
        for keyword in keywords:
            result.append(keyword)
        output_path = '../output/word_data/%s_data_key_words.dat' % weibo_name
        fo = open(output_path, "a+")
        for j in result:
            fo.write(j)
            fo.write(' ')
        fo.close()

    print("关键词提取成功!")
