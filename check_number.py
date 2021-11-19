def is_number(number):
    numbers = list('+1234567890')
    if number == "":
        return {"status": False}
    for spelling in list(number):
        if spelling not in numbers:
            return {"status": False}
    return {"status": True}


def is_numbers(numbers):
    list = []
    for number in numbers:
        if is_number(number)['status'] is True:
            list.append(number)
    return list
