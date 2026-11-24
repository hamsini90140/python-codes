# Progressive Electricity Billing System
units = 350
fixed_charge = 20.0
bill = 0.0

if units <= 100:
  bill = units * 1.50
elif units <= 300:
  bill = (100 * 1.50) + ((units - 100) * 2.50)
else:
  bill = (100 * 1.50) + (200 * 2.50) + ((units - 300) * 4.00)

bill += fixed_charge
if bill > 200:
  bill *= 1.05  # 5% surcharge

print(f"Consumption: {units} units")
print(f"Total Electricity Bill: ${bill:.2f}")