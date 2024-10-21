cs_interest = input('SURVEY: Are you interested in computer science? (y/n): ')
games_interest = input('Do you like playing computer games? (y/n): ')
instagram_account = input('Do you have an Instagram account? (y/n): ')

cs_interest_bool = cs_interest == 'y' 
games_interest_bool = games_interest == 'n'  
instagram_account_bool = instagram_account == 'y' 

print('SURVEY RESULTS')
print(f'Interested in computer science: {"Yes" if cs_interest_bool else "No"}')
print(f'Playing computer games: {"No" if games_interest_bool else "Yes"}')
print(f'Has an Instagram account: {"Yes" if instagram_account_bool else "No"}')
