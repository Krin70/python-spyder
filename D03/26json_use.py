import json

str_ = '{"name":"盗梦空间"}'
print(type(str_))
obj = json.loads(str_)
print(type(obj))

str2 = json.dumps(obj,ensure_ascii=False)
print(type(str2), ":", str2)

json.dump(obj,open("movie.txt",'w',encoding="utf-8"),ensure_ascii=False)

str3 = json.load(open('movie.txt',encoding='utf-8'))
print(str3)