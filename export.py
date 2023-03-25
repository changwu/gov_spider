import json

fo = open("wjbfb.txt", "r")
for line in fo.readlines(): 
    json_article = json.loads(line.strip())
    with open("exports/{}.txt".format(json_article['pub_time'].strip()), "w") as my_file:
        my_file.write("title: {}\n".format(json_article['title']))
        my_file.write("url: {}\n".format(json_article['url']))
        my_file.write("author: {}\n".format(json_article['author']))
        my_file.write("content: \n{}".format(json_article['content']))
fo.close()