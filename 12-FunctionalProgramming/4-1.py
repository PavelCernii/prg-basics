employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
            "JACKSON Peter","JOHNSON Rick",
            "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e: e[0]=="J", employees))
print(emp_J)