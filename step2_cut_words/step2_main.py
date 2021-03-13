from save_full_words import save_full_words
from extract_keywords import extract_keywords

if __name__ == "__main__":
    weibo_name = input("请输入需要对评论内容进行分词的微博名：")
    save_full_words(weibo_name)
    extract_keywords(weibo_name)
