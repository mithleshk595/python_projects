names = ["Mithlesh", "Anil", "Akash"]
ages = [25, 23, 27]
salaries = [34555.50, 40000.00, 45000.00]

#creates iterators of tuple

it = zip(names, ages, salaries )

# built list by iteratings the itertor object

lst = list(it)
print(lst)


# build the list into tuples 

n, a, s = zip(*lst)
print(n)
print(a)
print(s)
