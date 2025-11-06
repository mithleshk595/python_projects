# day = 4
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Today is a Weekday")
#     case 6 | 7:
#         print("I Love Weekends!")


# month = 5
# day = 4 
# match day:
#     case 1 | 2 | 3 | 4 | 5 if month == 4:
#         print("A Weekday in April")
#     case 1 | 2 | 3 | 4 | 5 if day == 5:
#         print("A Weekday in May")
#     case _:
#         print("No match")


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
