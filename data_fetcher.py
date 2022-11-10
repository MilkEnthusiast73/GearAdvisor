from testing import fullTest

def obdDataFetcher():
    import random
    gear = random.randint(0,5)
    speed = 0
    if gear == 1:
        speed = random.uniform(0, 15)
    elif gear == 2:
        speed = random.uniform(5,35)
    elif gear == 3:
        speed = random.uniform(22,44)
    elif gear == 4:
        speed = random.uniform(35,50)
    elif gear == 5:
        speed = random.uniform(80,100)

    return gear, speed

test_1=fullTest()
print(test_1.run_all_tests())