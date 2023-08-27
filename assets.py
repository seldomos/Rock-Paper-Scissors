def menu():
    print('''
╦═╗┌─┐┌─┐┬┌─           
╠╦╝│ ││  ├┴┐           
╩╚═└─┘└─┘┴ ┴  ┘        
╔═╗┌─┐┌─┐┌─┐┬─┐        
╠═╝├─┤├─┘├┤ ├┬┘        
╩  ┴ ┴┴  └─┘┴└─  ┘     
╔═╗┌─┐┬┌─┐┌─┐┌─┐┬─┐┌─┐┬
╚═╗│  │└─┐└─┐│ │├┬┘└─┐│
╚═╝└─┘┴└─┘└─┘└─┘┴└─└─┘o
                                    dev from seldomos

Enter:
1 - Rock
2 - Paper
3 - Scissors

'S' or 's' = check statistics 
'Q' or 'q' = exit                              
''')


def check(user_in, target):
    if user_in == target:
        return 0
    elif user_in == 1 and target == 3:
        return 1
    elif user_in == 2 and target == 1:
        return 1
    elif user_in == 3 and target == 2:
        return 1
    else:
        return 2
