import hanlp
import json

tok = hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH)

fo = open("wjbfb.txt", "r")
with open("corpus.txt", "w") as my_file:
    for line in fo.readlines(): 
        json_article = json.loads(line.strip())
        span = " "
        my_file.write(span.join(tok(json_article['content'])))
fo.close()