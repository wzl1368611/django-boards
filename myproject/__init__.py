import os,sys
base_path = os.path.dirname(os.path.dirname(__file__))
print(base_path)
# path = os.path.join(base_path,'accounts')
# path2 = os.path.join(base_path,'boards')
# print(path)
# print(path2)
lists = ["D:/2022年度/0328/Development/myproject/myproject/accounts",
         "D:/2022年度/0328/Development/myproject/myproject/boards"
         ]
sys.path.append(lists[0])
sys.path.append(lists[1])
print(sys.path)
