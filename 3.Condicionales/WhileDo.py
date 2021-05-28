#%%
# Create a program that with a int number with 3 digits show us its
# square root, its cube root and its fifth power.
while True:
    try:
        number = int(input('Please input a int number with three digits: '))
        while len(str(number)) == 3:
            square = round(number**(1/2), 2)
            print('the square root of the number is: ', square)
            cube = round(number**(1/3), 2)
            print('The cube root of the number is: ', cube)
            fifth = number**5
            print('The fifht power of the number is: ', fifth)
            break
        else:
            print('the number has not 3 digits')
            continue
        break
    except:
        print('the input is not a number')
    finally:
        print('')

#%%
#Create a list of objets to be chosen 
while True:
    list=input('choise a mean of transport: /n A-Car /n B-Train /n C-Bus')
    if list=='A':
        print('you have chosen Car')
        break
    elif list=='B':
        print('you have chosen Train')
        break
    elif list=='C':
        print('you have chosen Bus')
        break
    else:
        print('you must chose a mean of transport')
print('Enjoy your trip')

# %%
