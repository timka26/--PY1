# coding=utf-8
salary = 5000  # ежемесячная зарплата
spend = 6000  # расходы
months = 10  # количество месяцев
increase = 1.03  # ежемесячный рост цен
money_capital = 0  # количество денег, чтобы прожить 10 месяцев
total_salary = 0  # всего заработано
total_spend = 0  # всего потрачено
for month in range(0, months):
    total_salary += salary
    total_spend += spend
    spend *= increase
    money_capital = total_spend - total_salary

print(int(round(money_capital)))
