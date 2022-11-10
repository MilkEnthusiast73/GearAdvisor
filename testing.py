class Tests:
    import random
    #This class hosts all the individual tests for each function in the working code 
    def test_obdDataFetcher(self): #Each test has to be custom written for the function that it is testing
        grrr, sped = obdDataFetcher()
        if isinstance(grrr, int) and grrr >=-1 and grrr <= 6:
            if isinstance(sped, float) and sped >=-5 and sped <= 120:
                return True #If the function works as expected the function returns true
            else:
                return False #Otherwise it will return False
        else:
            return False #Otherwise it will return False

    #add the next test here


class fullTest(Tests):
    #This class can be used to run all the tests in one go.
    def run_all_tests(self):
        for result in dir(Tests):
            if not result:
                return False #If a single test fails, the function will return False
        return True #If all tests pass, the function returns True