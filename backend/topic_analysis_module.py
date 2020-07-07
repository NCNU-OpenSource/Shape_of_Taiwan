import jieba
jieba.set_dictionary('static/data/dict.txt.big')
jieba.load_userdict('static/data/userdict.txt')
import re
from gensim import corpora, models, similarities

# (def)資料前處理 return str()
def data_preprocess(text_str):
    
    # replace
    replaced_str = text_str.replace('\n',' ').replace(',','').replace('」','').replace('「','').replace('"','').replace('《','').replace('》','').replace('、','').replace('-','').replace('?','').replace('(','').replace(')','').replace('|','').replace('/','').replace('.','').replace('*','').replace('\t','').replace('。','').replace('，','').replace('（','').replace('）','').replace('[','').replace(']','')
    words = jieba.cut(re.sub('\d', '', replaced_str), cut_all=False)# cut
    tmp_str = ' '.join(words)
    words_list = tmp_str.split(' ')
    
    # 同義詞替換
    word_net = []
    with open("static/data/word_net.txt", "r", encoding='utf-8') as f1: # 載入同義字
        for line in f1:
            word_net.append(line)

    word_net = sorted(set(word_net))
    word_net_dic = {}

    for word in word_net:
        word_s = word.split()
        word_net_dic[word_s[0]] = word_s[1]
    
    # 替換
    request_doc_clear = ""
    # 如果 word 在 word_net 中
    for word in words_list:
        if(word in word_net_dic):
            request_doc_clear = request_doc_clear + word_net_dic[word] + ' '
        else:
            request_doc_clear = request_doc_clear + word + ' '
        
    return request_doc_clear

def computer_doc_sims(compare_doc):
    # 載入語料庫
    dictionary = corpora.Dictionary.load("./static/data/doc_computer.dict")
    corpus = corpora.MmCorpus("./static/data/doc_computer.mm") # 將數據流的語料變為內容流的語料
    
    # 載入 lsi 模型
    lsi = models.LsiModel.load('./static/data/doc_computer.lsi')
    
    # lsi 模型去計算 compare_doc 與 corpus 中的相似度 
    vec_bow = dictionary.doc2bow(compare_doc.split()) # 把 compare_doc語料庫轉為一個一個詞包(bow = bag of word 0.0)
    vec_lsi = lsi[vec_bow] # (input: 斷詞後的 bow、output: lsi 建模設定 topic_num)
    
    # 相似度計算
    index = similarities.MatrixSimilarity(lsi[corpus]) # Compute cosine similarity against a corpus of documents by storing the index matrix in memory.
    index.save("./static/data/doc_computer.index")
    sims = index[vec_lsi]
    sims = list(enumerate(sims)) # return [list(文本 id, 相似度)]
    
    return sims[1][1] # 回傳 compare_doc 與 電子計算機文本(1) 的相似度(1)