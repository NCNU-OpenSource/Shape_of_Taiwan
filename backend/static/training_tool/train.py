# 文章主題辨別模型建立
# 輸入訓練檔案名
# 需先準備訓練資料 doc_word_net_computer.dataset 檔案 (可以使用 data_prepare.py)
import sys
from gensim import corpora, models, similarities

def main():
    training_data_fileName = sys.argv[1]

    # # 讀入訓練資料
    # f = open(training_data_fileName, 'r', encoding='utf-8')
    
    # 使用訓練資料建立 Corpus (LSI 需要 tf-idf 與 dictionary 兩個參數)
    # -從 corpus 中移除 stop_word
    with open("data/stop_words.txt", encoding='utf-8') as f: # 載入 stop_word 資料
        stop_word_content = f.readlines()
    # --建立 stop_word_list 作為替換 key
    stop_word_content = [x.strip() for x in stop_word_content] #strip: 移除頭尾空格、中間不會
    stop_word_content = " ".join(stop_word_content)
    stoplist = set(stop_word_content.split())

    # -建立 dictionary (給予文章中 word id)
    # --corpora.Dictionary將文檔裡的詞袋給予編號
    dictionary = corpora.Dictionary(document.split() for document in open(training_data_fileName, encoding='utf-8'))
    # 使用 token2id 找出
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
                if stopword in dictionary.token2id] #dictionary.token2id: 代表什麼字詞對應到什麼id，有幾個id就代表有幾維向量空間
    dictionary.filter_tokens(stop_ids) # 移除 stop_word
    dictionary.compactify() #remove faps in id sequence after worfs that were removed
    dictionary.save("data/doc_computer.dict") 

    # 將 corpus 序列化
    texts = [[word for word in document.split() if word not in stoplist]
         for document in open(training_data_fileName, encoding='utf-8')]
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize("data/doc_computer.mm", corpus) # Corpus in Matrix Market format 
    # -建立 tf-id 將字典中的字詞向量轉換為字詞的重要性的向量 for LSI 
    # (tf-idf 重要性計算方式: 與文章中出現次數成正比，與在其他文章出現次數成反比)
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus] # 轉為向量表示
    
    # 建立 LSI 模型
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=30)
    corpus_lsi = lsi[corpus_tfidf] # LSI潛在語義索引
    lsi.save('data/doc_computer.lsi')
    corpora.MmCorpus.serialize('data/lsi_corpus_computer.mm', corpus_lsi)

    # 檢視建模結果(各篇文章 topic)
    print("# LSI topics:")
    for topic in lsi.print_topics():
        print(topic,end="\n\n")

if __name__ == "__main__":
    main()