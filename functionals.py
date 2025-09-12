# import operator
# lst = [("Anil", 21, 80), ("Mithlesh", 20, 90), ("Sunil", 20, 91), ("Shobha", 18, 93), ("Anil", 19, 85), ("Shobha", 20, 92)]
# print(sorted(lst, key= operator.itemgetter(0, 1, 2)))
# print(sorted(lst, key= lambda tpl : (tpl[0], tpl[1], tpl[2])))


d = {"x" : 500, "y" : 5874, "z" : 660}
key_max = max(d.keys(), key = (lambda k: d[k]))
key_min = min(d.keys(), key = (lambda k: d[k]))
print("Maximum value:", d[key_max])
print("Minimum value:", d[key_min])
