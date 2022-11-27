# coding=utf-8
salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

total_salary = 0
total_spend = 0
for month in range(0, months):
    total_salary += salary
    total_spend += spend
    spend *= 1.03
money_capital = total_spend - total_salary

print(int(round(money_capital)))
