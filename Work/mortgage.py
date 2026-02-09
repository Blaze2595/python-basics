# mortgage.py
#
# Exercise 1.7
print('Amount and Period if Paid 1000 extra for 12 months')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_pay_start = 61
extra_pay_end = 108
count = 1

while principal > 0:
    principal = round(principal * (1+rate/12) - payment,2)
    if(count >= extra_pay_start and count <= extra_pay_end):
        principal = round(principal - 1000,2)
    total_paid = total_paid + payment
    count = count + 1

print(f'Total amount paid is {total_paid} for period of {count} months')