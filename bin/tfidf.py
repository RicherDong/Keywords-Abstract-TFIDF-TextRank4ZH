# -*- coding: utf-8 -*-
# @Time   : 2018/12/8 15:08
# @Author : Richer
# @File   : tfidf.py
# 此文件是tfidf算法入口
import os,sys
import jieba
import re
from collections import Counter

class TFIDF():
    def __init__(self, file, topK = 20):
        self.base_path = os.getcwd()
        self.file_path = os.path.join(self.base_path, file)    # 需提取关键词的文件, 默认在根目录下
        self.stop_word_file = os.path.join(self.base_path + '/train_data/stop_words.txt')  # 停用词
        self.idf_file = os.path.join(self.base_path + '/data/idf_out/idf.txt')   # idf文件
        self.idf_freq = {}
        self._load_idf()
        self.topK = topK

    def key_abstract(self):
        # 获取处理后数据
        data = self._fitter_data()
        stop_words = self._get_stop_words()
        data = [char for char in data if char not in stop_words]
        total_count = data.__len__()
        list = Counter(data).most_common()
        keywords = {}
        for chars in list:
            char_tmp = {}
            char_tmp[chars[0]] = (chars[1]/total_count) * self.idf_freq.get(chars[0], self.mean_idf)       #TF * IDF(IDF不存在就取平均值)值
            keywords.update(char_tmp)
        tags = sorted(keywords.items(), key= lambda x:x[1], reverse = True)
        if self.topK:
            return  [tag[0] for tag in tags[:self.topK]]
        else:
            return  [tag[0] for tag in tags]



        # words =[char[0]:(char[1]/total_count) for chars in list]
        # print(words[:self.topK])



    def _fitter_data(self):
        string =  open(self.file_path, 'r', encoding= 'utf-8').read()
        content = string.replace("\n", "").replace(" ", "").replace("\u3000","").replace("\u00A0", "")
        content = " ".join(jieba.cut(content, cut_all = False))
        return re.sub('[a-zA-Z0-9.。:：,，)）(（！!??”“\"]', '', content).split()        # 此位置说白了就是只留下中文; 还可以使用遍历的方法判断词是否在  char > u'\u4e00' and char <= u'\u9fa5':


    def _load_idf(self):       # 从文件中载入idf
        cnt = 0
        with open(self.idf_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    word, freq = line.strip().split(' ')
                    cnt += 1
                except Exception as e:
                    pass
                self.idf_freq[word] = float(freq)
        print('Vocabularies loaded: %d' % cnt)
        self.mean_idf = sum(self.idf_freq.values()) / cnt

    def _get_stop_words(self):
        stop_words = []
        with open(self.stop_word_file, 'r') as f:
            words = f.readlines()
            for word in words:
                word = word.replace("\n", "").strip()
                stop_words.append(word)
        return stop_words