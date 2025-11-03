# broi rabotni chasove i tarifata za chas i ichislqvame brutnoto zaplashtane za meseca
name = (input("Name: "))
hours = float(input("Hours: "))
tarif = float(input("Tarif for hour: "))
days_in_month= float(input("Worked days in month: "))
print(f"{name}, who worked {hours} hours with tarif {tarif} for hour\nhave salary bruto:{(hours*tarif*days_in_month):.2f}")