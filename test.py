# import bcrypt

# #x = bcrypt.hashpw("aaa".encode(), bcrypt.gensalt()).decode()
# x="aaa".encode()
# y="$2b$12$.m42DCSqztNVecu8xRkq8O2ZdHNeEPG1cH3pNYd.U1iVDE.G5KYgi".encode()

# print(x)
# print(y)
# print(bcrypt.checkpw(x,y))


# from voluptuous import Schema, MultipleInvalid, Invalid, Exclusive, Required
# from flask import request

# # schema = Schema({'username':str, 'password':int})
# # try:
# #     schema({'usernam':"1"})
# #     print(schema({'passwor':2}))
# #     # raise AssertionError('MultipleInvalid not raised')
# # except MultipleInvalid as e:
# #     print(str(e))

# s = Schema({
#     Required('project'): int,
#     Required('project_name'): str
# })
# try:
#     s({'project':1})
#     print("OK")
# except MultipleInvalid as e:
#     print(str(e))

from contextlib import contextmanager
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1'):
    print('foo')