def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n/2.54

def ft_in_to_cm(feet, inches):
    total_inches = (feet * 12) + inches  #Converting feet to inches
    return total_inches * 2.54  # Converting inches to centimeters
    
if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')

