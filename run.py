# -*- coding: utf-8 -*-
# @Time   : 2018/12/5 17:22
# @Author : Richer
# @File   : run.py


import os,sys
from lib.tf_idf.get_idf import IDF
from bin.tfidf import TFIDF

class MAIN():
    def __init__(self, model='tf-idf', file = ''):
        self.model = model
        self.base_path = os.getcwd()
        self.idf_file = self.base_path + '/data/idf_out/idf.txt'
        self.file = file

    def main(self):
        keywords = []
        if self.model == 'tf-idf':
            if not os.path.isfile(self.idf_file):
                idfObj = IDF()
                idfObj.idf()
            else:
                main = TFIDF(self.file)
                keywords = main.key_abstract()
        else:
            # 还有一种方式
            keywords = ''

        return keywords
if __name__ == '__main__':
    run = MAIN('tf-idf', 'test.txt')
    keywords = run.main()
    print(keywords)
