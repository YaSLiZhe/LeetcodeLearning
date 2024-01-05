def sum_numbers(*nums):
    total = 0
    for x in nums:
        total += x
    print(total)


sum_numbers(1, 1, 2, 3, 4, 5)


def describe_pet(**pet):
    for key, value in pet.items():
        print(f"The {key} is {value}")


describe_pet(age='12', species='dog', name='Buddy')
