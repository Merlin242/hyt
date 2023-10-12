#def distance(**kwargs):
  #res = ((args[0] - x-1) ** 2 + (args[1] - y2) ** 2) ** 0.5
 # return res

#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#print(distance(x1, y1, x2, y2))

#def fib(n):
 #   if n == 0:
  #      return 1
  #  elif n == 1:
  #      return  1
  #  else:
  #      return fib(n - 1) + fib(n - 2)
#print(fib(int(input())))

#def power (a, n):

 #   res = 1
 #   if n > 0:
 #       for i in range(n):
 #           res *= a
#        return  res
 #   elif n < 0:
     #   for i in range (-n):
    #        res /= a
    #    return res
  #  return res
#print(power(int(input())), int(input()))

#def is_year_leap(year):
 #    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  #      return True
    #else:
    #    return False

#year = 2023
#print(is_year_leap(year))

#def season(month):
 #   if month in [12, 1, 2]:
  #      return "зима"
   # elif month in [3, 4, 5]:
        #return "весна"
    #elif month in [6, 7, 8]:
        #return "лето"
    #elif month in [9, 10, 11]:
        #return "осень"
   # else:
    #    return "Неверный номер месяца"


#month_seanson = int(input("Введите номер месяца: "))
#print("Время года:", season(month_seanson))


#def date(day, month, year):
    #if year < 1 or month < 1 or month > 12 or day < 1:
     #   return False
    #days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     #   days_month[2] = 29
   # if day > days_month[month]:
    #    return False
   # return True
#day = int(input("Введите день: "))
#month = int(input("Введите месяц: "))
#year = int(input("Введите год: "))
#print("Существует ли такая дата:", date(day, month, year))


#def prime(num):
 #   if num < 2:
  #      return False
   # for i in range(2, int(num ** 0.5) + 1):
    #    if num % i == 0:
     #       return False
    #return True
#number = int(input("Введите число от 0 до 1000: "))
#print("Является ли число простым:", prime(number))

def final_amount_money(initial_amount, years):

    intereste = 0.10


    final_amount = initial_amount * (1 + intereste) ** years
    return final_amount


initial_amount = float(input("Введите сумму вклада в рублях: "))
years = int(input("Введите срок вклада в годах: "))

final_amount = final_amount_money(initial_amount, years)
print("Сумма на счету после", years, "лет:", final_amount, "рублей")





















