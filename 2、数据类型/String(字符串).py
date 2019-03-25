'''
什么是字符串？
——字符串是以单引号或双引号括起来的任意文本
'''
#创建字符串
str1="Hailong is a good guy"
str2="Hailong is a nice person"
str3="Hailong is a handsome man"

'''
字符串运算
'''
#字符串连接
str4="Hailong is a "
str5="handsome man"
str6=str4 + str5
print("str6 =", str6)
print("str4 =", str4)    #字符串不可变
print("str5 =", str5)

#输出重复字符串
str7="good "
str8=str7*3
print("str8 =", str8)

#访问字符串中的某一个字符
#通过索引下标查找字符，索引从0开始
#字符串名[下标]
str9="Hailong is a nice person"
print(str9[1])
#str9[1]="u"   会报错，因为字符串不可变

#截取字符串
#字符串名[[start]:end[:step]]
str10=str9[8:17]
print("str10 =", str10)

#格式化输出
#占位符 %d %s %f
'''
转义字符：将一些字符转换成有特殊含义的字符   \
'''
#换行符 \n(表示一个字符)
num=10
str="Hailong works very hard!"
f=10.123456789
print("num = %d,str = %s,f = %.3f" % (num,str,f))
print("num = %d\nstr = %s\nf = %.3f" % (num,str,f))

'''
\\、\'、\"
'''
print("Hailong \\ is a handsome boy")
print("Hailong is a 'good' person")
print("Hailong is a \"good\" person")

#如果字符串内有很多换行，用\n写在一行不好阅读
print("good\nnice\nhandsome")
print('''
good
nice
handsome
''')

'''
\t 制表符
'''
print("Hailong\tZeng")
print("\\\t\\")
#如果字符中有很多字符串需要转义，需要加入很多的\，为了简化，python允许用r表示内部的字符串默认不转义
print(r"\\\t\\")

#eval(str)
#功能：可以将字符串str当成有效的表达式来求值并返回计算结果
num1=eval("123")
print(num1)
print(eval("12+3"))
print(eval("12-3"))

#len(str)
#返回字符串的长度(字符个数，而非字节数）
print(len("Hailong is a pretty guy"))

#str.lower()
#转换字符串中的大写字母为小写字母
str11="HailongZeng is very warm-hearted"
print(str11.lower())   #不改变字符串的值
print(str11)

#str.upper()
#转换字符串中的小写字母为大写字母
str12="HailongZeng is very warm-hearted"
print(str12.upper())

#str.swapcase()
#转换字符串中小写字母为大写字母，大写字母为小写字母
str13="HailongZeng is very warm-hearted"
print(str13.swapcase())

#str.capitalize()
#第一个字母首字母大写，其他小写
str14="HailongZeng is very warm-hearted"
print(str14.capitalize())

#str.title()
#每个单词的首字母大写
str15="HailongZeng is very warm-hearted"
print(str15.title())

#str.center(width,fillchar)
#返回一个指定宽度的居中字符串，可以用给定符号填充，若没有给定符号，则默认空格
str16="HailongZeng is very warm-hearted"
print(str16.center(40,"*"))

#str.ljust(width[,fillchar])
#返回一个指定宽度的左对齐字符串,可以用给定符号填充，若没有给定符号，则默认空格
str17="HailongZeng is very warm-hearted"
print(str17.ljust(40,"*"))

#str.rjust(width[,fillchar])
#返回一个指定宽度的右对齐字符串,可以用给定符号填充，若没有给定符号，则默认空格
str18="HailongZeng is very warm-hearted"
print(str18.rjust(40,"*"))

#str.zfill(width)
#返回一个指定宽带的字符串，原字符串右对齐，左边补0
str19="HailongZeng is very warm-hearted"
print(str19.zfill(40))

#str.count(指定str[,start][,end])
#在原字符串指定范围内寻找指定字符串的个数，并返回
str20="HailongZeng is very warm-hearted"
print(str20.count("very",20,len(str20)))

#str.find(指定str[,start][,end])
#从左向右检测指定字符串是否包含在原字符串中，可以指定范围，默认从头到尾，返回的是指定字符串第一次出现的开始下标。不存在
#指定字符串，返回-1。
str21="HailongZeng is very warm-hearted"
print(str21.find("very"))
print(str21.find("very",14,len(str21)))
print(str21.find("good"))

#str.rfind(指定str[,start][,end])
#从右向左检测指定字符串是否包含在原字符串中，可以指定范围，默认从头到尾，返回的是指定字符串第一次出现的开始下标。不存在
#指定字符串，返回-1。
str22="HailongZeng is very warm-hearted"
print(str22.rfind("very"))
print(str22.rfind("very",14,len(str21)))
print(str22.rfind("good"))

#str.index(指定str[,start][,end])
#跟find()方法一样，只不过当指定str不存在时，会报错。而不是返回-1
str23="HailongZeng is very warm-hearted"
print(str23.index("very"))
print(str23.index("very",14,len(str21)))
#print(str23.index("good"))

#str.rindex(指定str[,start][,end])
#跟rfind()方法一样，只不过当指定str不存在时，会报错。而不是返回-1
str24="HailongZeng is very warm-hearted"
print(str24.rindex("very"))
print(str24.rindex("very",14,len(str21)))
#print(str24.rindex("good"))

#str.lstrip(指定str)
#截掉字符串左侧指定的字符，默认指定字符为空格
str25="  HailongZeng is very warm-hearted"
print(str25)
print(str25.lstrip())

#str.rstrip(指定str)
#截掉字符串右侧指定的字符，默认指定字符为空格
str26="HailongZeng is very warm-hearted********"
print(str26)
print(str26.rstrip("*"))

#str.strip(指定str)
#截掉字符串左右两侧指定字符，默认指定字符为空格
str27="********HailongZeng is very warm-hearted********"
print(str27)
print(str27.strip("*"))

#ord(str)将字符转换为其对应的ASCII码，chr(ASCII码）将ASCII码转换为其对应的字符
str28="a"
print(ord(str28))
str29=chr(65)
print(str29)

#str.split("指定字符串",num)   以指定字符串为分隔符截取字符串,指定num,则仅截取出(num+1)个字符串，即只截取num次
str29="Hailong is pretty good"
print(str29.split(" ",2))

#str.splitlines([keepends])  按照("\r","\r\n","\n")分隔，返回列表。按行切割
#keepends==True   会保留换行符
#keepends==False  不会保留换行符
str30='''
Hailong is very nice!
Hailong is handsome!
Hailong is still a student!
'''
print(str30.splitlines(True))
print(str30.splitlines(False))

#"指定字符串".join(序列)    以指定的字符串分隔符，将序列中的所有元素组合成一个字符串，默认空格连接
list31=["Hailong","is","very","very","handsome"]
str31=" ".join(list31)
str32="*".join(list31)
print(str31)
print(str32)

#max(str)  min(str)   按ASCII码比较
str33="Hailong is very good!"
print(max(str33))
print("*"+min(str33)+"*")

#str.replace("oldstr","newstr",num)
#用newstr替换str中的oldstr，默认是全部替换。如果指定了num，那么只能替换前num个
str34="Hailong works very very very hard!"
str35=str34.replace("very","pretty",1)
print(str35)

#创建一个字符串映射表
#要转换的字符串    目标字符串
#两字符串的长度应该一致
t36=str.maketrans("av","bc")
str36="Hailong works very very very hard!"
str37=str36.translate(t36)
print(str37)

#str.startswith(指定字符串,start=0,end=len(str)) 判断在指定范围内字符串是否以指定字符串开头，若没有指定范围，默认整个字符串
str38="Hailong works very very very hard!"
print(str38.startswith("Hai",5,12))

#str.endswith(指定字符串,start=0,end=len(str)) 判断在指定范围内字符串是否以指定字符串结尾，若没有指定范围，默认整个字符串
str39="Hailong works very very very hard!"
print(str39.endswith("Hai",5,12))

#编码格式  utf-8和gbk(国标）
#str.encode(encoding="utf-8",errors="strict")
str40="Hailong works very very very hard该!"
data40=str40.encode("utf-8","ignore")
print(data40)
#解码 str.decode(encoding="utf-8",errors="strict")
# 注意：要与编码时的编码格式一致，因为不同的编码方式在汉字方面会出现不同的信息，导致解码时出错。
#      可以使用"ignore"忽略编码方式的不同，但是会导致解码的结果与编码时的结果不同
str41=data40.decode("gbk","ignore")
print(str41)

#str.isalpha()  如果字符串的长度不小于一个字符且所有的字符都是字母返回True，否则返回False
str42="Hailong123"
print(str42.isalpha())

#str.isdigit()    如果字符串只包含数字，则返回True，否则返回False
#str.isnumeric()  如果字符串只包含数字字符，则返回True，否则返回False
print("123a".isdigit())
print("1".isdigit())
print("123a".isnumeric())
print("1".isnumeric())

#str.isalnum()  如果字符串的长度不小于一个字符且所有的字符都是字母或者数字返回True，否则返回False
str43="Hailong123"
print(str43.isalnum())


#str.isupper()  如果字符串中至少有一个英文字符且所有的英文字符都是大写字母返回True，否则返回False
str44="HAI1"
print(str44.isupper())

#str.islower()  如果字符串中至少有一个英文字符且所有的英文字符都是小写字母返回True，否则返回False
print("hai".islower())
print("hai1".islower())
print("1".islower())
print("Hai".islower())

#str.istitle()   如果字符串是标题化(每个单词的首字母为大写)的返回True，否则返回False
print("Hai long".istitle())
print("Hai Long".istitle())

#str.isdecimal() 如果字符串中只包含十进制字符，返回True，否则返回False
print("123".isdecimal())
print("123z".isdecimal())

#str.isspace()   如果字符串中只包含空格则返回True，否则返回False
print("***")
print(" ".isspace())
print("    ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())
print("\f".isspace())