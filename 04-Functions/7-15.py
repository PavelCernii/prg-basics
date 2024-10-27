def f(detector):
    people = 0 
    people_max = 0

    for char in detector:
        if char == '+':
            people += 1
        elif char == '-':
            people -= 1
    
        people_max = max(people_max, people)

    if people_max >= 3:
        return True
    else:
        return False
        

print(f("+-++-++-+---"))