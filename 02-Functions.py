def printEmployeeDetails(id, name, dob, gender, salary=0, designation="NA", *args, **kwargs):
    print("ID is ", id)
    print("Name is ", name)
    print("DOB is ", dob)
    print("Salary is ", salary)
    print("Gender is ", gender)
    print("Designation is ", designation)
    print("Other details - ", args)
    print("Some other details - ", kwargs)


printEmployeeDetails(1, "Ram", "29-02-2000",
                     gender="M", designation="Dev", salary=15000)
# keyword arguments
# default args should always be at the end of arguments list
# ||ly, keyword arguments should be at the end of parameters list (while calling the fn)
# keyword arguments dont work on position so can bewritten in any order
# but positional arguemnts need to be passed according to the position of the argumen in arguments list
# **kwargs -> keyword arguments


printEmployeeDetails(1, "Ram", "01-01-1999", "M",
                     "20000", "Data Analyst", "HR")

printEmployeeDetails(1, "Ram", "01-01-1999", "M",
                     salary="20000", designation="Data Analyst", department="HR")
