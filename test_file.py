
import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    retVal = request.param
    print("\nSetup! retVal = {}".format(retVal))
    return retVal

def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True

# @pytest.fixture(scope="session", autouse=True)
# def setupSession():
#     print("\nSetup Session")

# @pytest.fixture(scope="module", autouse=True)
# def setupModule():
#     print("\nSetup Module")

# @pytest.fixture(scope="function", autouse=True)
# def setupFunction():
#     print("\nSetup Function")

# def test1():
#     print("Executing test1!")
#     assert True

# def test2():
#     print("Executing test2!")
#     assert True

# @pytest.fixture()
# def setup1():
#     print("\nSetup 1")
#     yield
#     print("\nTeardown 1")

# @pytest.fixture()
# def setup2(request):
#     print("\nSetup 2")

#     def teardown_a():
#         print("\nTeardown A")
    
#     def teardown_b():
#         print("\nTeardown B")
    
#     request.addfinalizer(teardown_a)
#     request.addfinalizer(teardown_b)

# def test1(setup1):
#     print("Executing test1!")
#     assert True

# def test2(setup2):
#     print("Executing test2!")
#     assert True

# from my_test_file import test_it

# @pytest.fixture()
# @pytest.fixture(autouse=True)
# def setup():
#     print("\nSetup")

# def test1(setup):
# def test1(setup):
#     print("Executing test1!")
#     assert True

# @pytest.mark.usefixtures("setup")
# def test2():
#     print("Executing test2!")
#     assert True

# from my_test_file import test_it


# class TestClass:
#     @classmethod
#     def setup_class(cls):
#         print("Setup TestClass!")
    
#     @classmethod
#     def teardown_class(cls):
#         print("Teardown TestClass!")

#     def setup_method(self, method):
#         if method == self.test1:
#             print("\nSetting up test1!")
#         elif method == self.test2:
#             print("\nSetting up test2!")
#         else:
#             print("\nSetting up unknown test!")
    
#     def teardown_method(self, method):
#         if method == self.test1:
#             print("\nTearing down test1!")
#         elif method == self.test2:
#             print("\nTearing down test2!")
#         else:
#             print("\nTearing down unknown test!")
    
#     def test1(self):
#         print("Executing test1!")
#         assert True

#     def test2(self):
#         print("Executing test2!")
#         assert True

    # def test_me(self):
    #     assert True

    # def test_me2(self):
    #     assert True

# class MyTestClass():
#     def test_it(self):
#         assert True

#     def test_it2(self):
#         assert True

#     def not_a_test():
#         assert True

# def setup_module(module):
#     print("Setup Module")

# def teardown_module(module):
#     print("Teardown Module")

# def setup_function(function):
#     if function == test1:
#         print("\nSetting up test1!")
#     elif function == test2:
#         print("\nSetting up test2!")
#     else:
#         print("\nSetting up unknown test!")

# def teardown_function(function):
#     if function == test1:
#         print("\nTearing down test1!")
#     elif function == test2:
#         print("\nTearing down test2!")
#     else:
#         print("\nTearing down unknown test!")

# def test1():
#     print("Executing test1!")
#     assert True

# def test2():
#     print("Executing test2!")
#     assert True
