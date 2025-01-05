grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

filtered_grades = list(filter(lambda e: e>2.0, grades))

print(sum(filtered_grades) / len(filtered_grades))