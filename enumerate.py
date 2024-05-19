# x = ("Masala","Lemon","ginger")
# y = enumerate(x)
# print(list (x))
# print(list (y))  


list = [{'name':'chai', 'time':'2min'},{'name':'code', 'time':'3min'}]

# for i in enumerate(list,start=1):
#     print(i)

for i,video in enumerate(list,start=1):
    print(f"{i}, {video['name']}")