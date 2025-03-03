# Time when alarm will go off after user input how many hours from current time they would like to be alerted

#Variable Definitions

current_time = 13
hours_for_alarm = int(input('Enter number of hours from now when you\'d want your alarm to go off. Ex: 56: '))
hour_per_halfday = 24

#Calculation
alarm = (current_time + hours_for_alarm) % hour_per_halfday

#Output
print('Alarm will go off at: ', alarm,':00 on a 24-hour clock', sep = '', end=" ")

#translate to civilian time
if alarm > 12:
   print('or',alarm - 12 , 'PM')