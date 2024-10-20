facebook = input("Do you have an account on Facebook? (yes/no): ") == 'yes'
twitter = input("Do you have an account on Twitter? (yes/no): ") == 'yes'
instagram = input("Do you have an account on Instagram? (yes/no): ") == 'yes'

if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("You are a good influencer!")
else:
    print("You need more social media accounts to be a good influencer.")
  