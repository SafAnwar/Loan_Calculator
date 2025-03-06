loan_amount = 1000
years = 10
apr = 0.05
for i in range(years):
  loan_amount *= 1 + apr
print(round(loan_amount, 2))