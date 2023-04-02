import pyfiglet

text = pyfiglet.print_figlet(text='com pound interest', 
colors='GREEN', font='isometric3')

print(text)

print('This file will allow you to calculate compound interest of a set contribution to an account with a set interest rate')

begin = input('Would you like to calculate a compound interest financial plan? Y or N : ')

if begin == "Y":
    c = float(input('What do you want to contribute per month?: '))
    y = int(input('How many years will you contibute this amount?: '))
    i = float(input('What will the interest rate be?: '))

    total_balance = 0
    for year in range(1, y+1):
    
        
        year_contribution = c * 12
        total_balance += year_contribution
        year_return = total_balance * (i/100)
        total_balance += year_return 
        y = y - 1
        print('Total balance at the end of year {} is {:.2f}'.format(y, total_balance))
    print('Total balance after {} years is {:.2f}'.format(y, total_balance))

else:
    quit()

        
'''       
while y > 0:        
    c = input('What do you want to contribute per month?: ')
    y = input('How many years will you contibute this amount?: ')
    i = input('What will the interest rate be?')
    year_contribution = c * 12
    year_return = i * year_contribution
    total_balance = year_return + year_contribution
    y = y - 1
        
'''


