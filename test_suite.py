import importlib

def run_tests_on(file_path, verbose=0):
    print("")

    module = importlib.import_module(file_path)
    test_case_classes = module.all

    if type(test_case_classes) != list:
        test_case_classes = [test_case_classes]
    
    for test_case_class in test_case_classes:
        t = test_case_class(verbose)
        test_cases = [i for i in dir(t) if i[:5] == 'test_']

        for test_case in test_cases:
            test = getattr(t, test_case)
            test()
        
        print("\n----\n")
    


class TestCase:
    
    def __init__(self, verbose):
        self.verbose = verbose

    def assertEqual(self, a, b):
        try:
          if a==b:
            print(".", end="")
          else:
            print("F", end="")
        except:
            print("E", end="")        

    def assertIn(self, a, b):
        try:
          if a in b:
            print(".", end="")
          else:
            print("F", end="")
        except:
            print("E", end="")      

    def assertGreater(self, a, b):
        try:
          if a > b:
            print(".", end="")
          else:
            print("F", end="")
        except:
            print("E", end="")
