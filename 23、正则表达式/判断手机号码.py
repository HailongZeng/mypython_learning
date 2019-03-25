'''
给你一串字符串，判断是否是手机号码
'''
import re
def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] !='1':
        return False
    for i in str:
        if i < '0' or i > '9':
            return False
    return True
def checkPhone2(str):
    #13912345678
    pat = r'1(([3578]\d)|(47))\d{8}$'
    res = re.match(pat, str)
    return res

print(checkPhone('13123456789'))
print(checkPhone('13123a456789'))
print(checkPhone('131234567892'))
print(checkPhone('23123456789'))

print(checkPhone2('13123456789'))
print(checkPhone2('14723435523'))
print(checkPhone2('13123a456789'))
print(checkPhone2('131234567892'))
print(checkPhone2('23123456789'))