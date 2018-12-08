# -*- coding: utf-8 -*-
# @Time   : 2018/12/5 17:34
# @Author : Richer
# @File   : get_idf.py
# 此文件用于自动计算idf

import jieba
import os,sys
import math

class IDF():

    def __init__(self):
        self.base_path = os.getcwd()
        self.idf_input_path  = os.path.join(self.base_path + '/train_data/tf_idf_input/')  # 存放制作idf文档存放的文件夹
        self.stop_word_file  = os.path.join(self.base_path + '/train_data/stop_words.txt')               # 停用词
        self.idf_output_path = os.path.join(self.base_path + '/data/idf_out/')

    def idf(self):
        all_chars_dict, total = self._get_file()
        with open(self.idf_output_path + 'idf.txt', 'w', encoding='utf-8') as wf:
            for char,value in all_chars_dict.items():
                if char > u'\u4e00' and char <= u'\u9fa5':
                    p = math.log(total / (value + 1))
                    wf.write(char + ' ' + str(p) + '\n')

    def _get_file(self):
        idf_input_list = os.listdir(self.idf_input_path)
        all_dict = {}
        total = 0
        for file_name in idf_input_list:
            file = os.path.join(self.idf_input_path, file_name)
            words = self._read_file(file)                        # 读取每一个文件的信息
            tmp_dict = {char: 1 for char in words}
            total =+1
            for tmp_char in tmp_dict:
                num = all_dict.get(tmp_char, 0)
                all_dict[tmp_char] = num + 1
        return all_dict, total

    def _read_file(self, file):
        stop_words = self._stop_words()
        file = open(file, 'r', encoding='utf-8',errors='ignore') .read()
        content = file.replace("\n","").replace("\u3000","").replace("\u00A0","").replace(" ","")
        content_chars = jieba.cut(content, cut_all= True)
        words = list(set([char for char in content_chars if char not in stop_words]))
        return words

    def _stop_words(self):
        stop_words = []
        with open(self.stop_word_file, 'r') as f:
            words = f.readlines()
            for word in words:
                word = word.replace("\n","").strip()
                stop_words.append(word)
        return stop_words
