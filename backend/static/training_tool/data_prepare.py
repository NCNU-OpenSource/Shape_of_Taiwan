# 訓練資料準備
# 注意: 傳入 dataset, 一篇文章一行，產出 cleaned_training_data.dataset
import re
import sys
import jieba
jieba.set_dictionary("data/dict.txt.big")
jieba.load_userdict('data/userdict.txt')

def main():
    fileName = sys.argv[1]
    
    # 清理不必要符號、數字
    # wf = codecs.open("data/doc_cut_computer_new.dataset", "w","utf-8")
    cleaned_str = ""
    with open(fileName, "r", encoding='utf-8') as f:
        for line in f:
            tmpStr = line.replace(',','').replace('」','').replace('「','').replace('"','').replace('《','').replace('》','').replace('、','').replace('-','').replace('?','').replace('(','').replace(')','').replace('|','').replace('/','').replace('.','').replace('*','').replace('\t','').replace('。','').replace('，','').replace('（','').replace('）','').replace('[','').replace(']','')
            cleaned_str = cleaned_str + re.sub('\d', '', tmpStr)
            # print(re.sub('\d', '', tmpStr))
            # wf.write(re.sub('\d', '', tmpStr))
    # wf.close()

    # 斷詞
    words = jieba.cut(cleaned_str)
    cut_words = " ".join(words)

    # 同義字 dic 建立
    word_net = []
    with open("data/word_net.txt", "r", encoding='utf-8') as f1: # 載入同義字
        for line in f1:
            word_net.append(line)
    word_net = sorted(set(word_net)) # 先短再長的字句，避免誤判
    word_net_dic = {}
    for word in word_net: # 建立同義字 dic {換:被換}
        word_s = word.split()
        word_net_dic[word_s[0]] = word_s[1]

    # 同義字替換
    wf = open("cleaned_training_data.dataset", "w", encoding='utf-8')
    for word in cut_words.split(' '):
        if( word in word_net_dic):
            wf.write(word_net_dic[word] + " ")
        else:
            wf.write(word + " ")
    wf.close()

if __name__ == "__main__":
    main()