import jieba

seg_list = jieba.cut('我来到北京清华大学', cut_all=True)
print('Full Mode: ' + '/'.join(seg_list))

seg_list = jieba.cut('我来到北京清华大学', cut_all=False)
print('Default Mode: ' + '/'.join(seg_list))

seg_list = jieba.cut_for_search("我来到北京清华大学")
print('Search Engine Mode: ' + '/'.join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))