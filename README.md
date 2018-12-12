# 使用不同方式提取关键词

## 找到run.py文件

    if __name__ == '__main__':
        run = MAIN('tf-idf', 'test.txt')
        keywords = run.main()
        print(keywords)
        
###   MAIN() 两个参数,

####   第一个参数是提取关键字的方法，目前只支持tf-idf，后续持续更新， 下一步支持TextRank4ZH
####   第二个参数是需要提取关键字的文本；该文本可以和run.py文件放在同一个目录, 将文件名作为该参数传入

运行run.py文件
    命令：python run.py
    直接返回所提取的关键字
    

tf-idf原理介绍连接：
 关键词提取/关键字提取之TF-IDF算法：https://www.cnblogs.com/Richer01/p/10089136.html


   
   
