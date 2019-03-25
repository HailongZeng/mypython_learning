#排列：从n个不同元素中取出m(m<=n)个元素，按照一定的顺序排成一列，叫做从n个元素中取出m个元素
#的一个排列（Arrangement)。特别地，当m=n时，这个排列被称作全排列（Permutation）


##组合：从n个不同元素中取出m(m<=n)个元素作为一组进行组合
import itertools
mylist1 = list(itertools.permutations([1,2,3,4,5], 3))  #从[1,2,3,4]取出三个数进行排列
mylist2 = list(itertools.combinations([1,2,3,4,5], 3))  #从[1,2,3,4]取出三个数进行组合
mylist3 = list(itertools.product('0123456789', repeat=4))
print(mylist1)
print(len(mylist1))
print(mylist2)
print(len(mylist2))
#print(mylist3)
print(len(mylist3))
