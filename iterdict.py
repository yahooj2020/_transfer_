
# 遍历嵌套的字典 ，value是list的情况
key_list = []
value_list = []
def iterdict(d):

    for k,v in d.items():
        if isinstance(v, list) ==False:
            key_list.append(k)
            value_list.append(v)
        else:
            iterdict(v[0])

iterdict(body)
print(key_list)
print(value_list)
