# lst = [1, 2, 3]
# my_str = "mlops playlist"
# my_int = 155

# print(type(lst))      # <class 'list'>
# print(type(my_str))   # <class 'str'>
# print(type(my_int))   # <class 'int'>

# lst.clear()
# print(lst)            # This will print []

from oops_proj import chatbook

user1 = chatbook()
print(user1.id)

chatbook.set_id(100)
user2 = chatbook()
print(user2.id)
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)