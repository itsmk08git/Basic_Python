def total_exp(exp):
    '''
    This function takes list of number as input and returns sum of the list
    :param exp: input list
    :return: total sum
    '''
    total = 0
    for x in exp:
        total+=x

    return total

mohan_exp=[1000,2000,3000,4000]
mohan_Total=total_exp(mohan_exp)

pandit_exp=[2000,3000,4000]
pandit_total=total_exp(pandit_exp)

print("Total Expenses is "+str(mohan_Total))
print(f"Total Expenses is {pandit_total}")

print(help(total_exp))

#Program to calculate Area Based on Shapes
def cal_area(shape, base, height):
    if shape =="Rectangle" or shape=="rectangle" :
        total_area = base * height
    else:
        total_area = (1/2)*base * height

    return total_area

shape = input("Enter the Shape(Rectangle or Triangle):")
if shape =="Rectangle" or shape=="rectangle" :
    length = input("Enter the length:")
    height = input("Enter the height:")
    length=int(length)
    height=int(height)
    area = cal_area(shape, length, height)
    print(f"The Area of {shape} is {area}.")
elif shape=="Triangle" or shape=="triangel" :
    base = input.int(("Enter the base:"))
    height = input.int(("Enter the height:"))
    area = cal_area(shape, base, height)
    print(f"The Area of {shape} is {area}.")
else:
    print("Shape Out of Recognization:")