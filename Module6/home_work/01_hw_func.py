# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    n1 = ticket_number//100000%10
    n2 = ticket_number//10000%10
    n3 = ticket_number//1000%10
    n4 = ticket_number//100%10
    n5 = ticket_number//10%10
    n6 = ticket_number%10
    if n1+n2+n3 == n4+n5+n6:
        print(ticket_number)
# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
