from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors


glove_input_file = './glove/vectors.txt'
# word2vec_output_file = './glove/w2v-vectors.txt'
# _ = glove2word2vec(glove_input_file, word2vec_output_file)


# 加载模型
# glove_model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
glove_model = KeyedVectors.load_word2vec_format(glove_input_file, binary=False, no_header=True)
# 如果希望直接获取某个单词的向量表示，直接以下标方式访问即可
cat_vec = glove_model['美国']
print(cat_vec)
# 获得单词frog的最相似向量的词汇
print(glove_model.most_similar('美国'))

similarity = glove_model.similarity('美国', '霸权')

print(similarity)

similarity = glove_model.similarity('美国', '中国')

print(similarity)

distance = glove_model.distance("美国", "霸权")
print(f"{distance:.1f}")

distance = glove_model.distance("美国", "友善")
print(f"{distance:.1f}")