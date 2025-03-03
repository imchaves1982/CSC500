#Purchased Meal Check Calculation

#Input Variable
cost_of_meal = float(input('Enter Cost of Meal Total (in dollars and cents:'))


#Calculations
sales_tax = cost_of_meal * .07
tip = (cost_of_meal + sales_tax) * .18
total_check = cost_of_meal + tip + sales_tax

#Output
print('Meal Cost: $', '{:.2f}'.format(cost_of_meal))
print('Sales Tax (7%): $','{:.2f}'.format(sales_tax))
print('Tip (18%): $','{:.2f}'.format(tip))
print('Total Price: $','{:.2f}'.format(total_check))