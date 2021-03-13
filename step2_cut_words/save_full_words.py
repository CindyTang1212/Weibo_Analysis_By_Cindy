import pymysql
import jieba

jieba.load_userdict("SogouLabDic.txt")
jieba.load_userdict("dict_baidu_utf8.txt")
jieba.load_userdict("dict_pangu.txt")
jieba.load_userdict("dict_sougou_utf8.txt")
jieba.load_userdict("dict_tencent_utf8.txt")
jieba.load_userdict("my_dict.txt")

stopwords = {}.fromkeys([line.rstrip() for line in open('Stopword.txt')])


def save_full_words(weibo_name):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678',
                           db='weibo_comments',
                           unix_socket='/tmp/mysql.sock', use_unicode=True, charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql = 'select 评论内容 from %s' % weibo_name
    cur.execute(sql)
    result = cur.fetchall()
    mytext = []
    for text in result:
        token = jieba.cut(text['评论内容'])
        for word in list(token):
            if word not in stopwords:
                mytext.append(word)
    output_path = '../output/word_data/%s_data_full.dat' % weibo_name
    fo = open(output_path, "a+")
    for word in mytext:
        fo.write(word)
        fo.write(' ')
    fo.close()
