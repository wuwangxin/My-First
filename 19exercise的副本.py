"""
tup = ("悟空","八戒","唐僧","沙僧","女儿国过往")
"""
# tup = ("悟空","八戒","唐僧","沙僧","女儿国过往")
# iterator = tup.__iter__()
# while True:
#     try:
#         print(iterator.__next__())
#     except:
#         break



"""
dict = {"悟空":2000,"八戒":3000,"唐僧":1000,"沙僧":2800}
不要用for获取字典所有元素，
通过迭代器获取字典所有元素
"""
dict = {"悟空":2000,"八戒":3000,"唐僧":1000,"沙僧":2800}
iterator = dict.__iter__()
while True:
    try:
        key = iterator.__next__()
        value = dict[key]
        print(key, value)
    except StopIteration:
        break

