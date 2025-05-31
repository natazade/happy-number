number = 45
def is_happy(number: int) -> bool:
    seen_numbers = set()
    while (number!=1) and (number not in seen_numbers):
        seen_numbers.add(number)
        number = sum([int(i)**2 for i in str(number)])

    return number == 1 

if __name__ == "__main__":
    assert is_happy(7) , 'test case 1 is failed'
    assert is_happy(45) , 'test case 2 is failed'
    assert is_happy(72), 'test case 3 is failed'
    assert is_happy(82), 'test case 4 is failed'   
