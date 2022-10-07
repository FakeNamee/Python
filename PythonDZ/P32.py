lst = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]
lst = [el for el in lst if lst.count(el) == 1]
print(lst)
