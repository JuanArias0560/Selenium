from unittest import  TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtest import SearchTest

assertion_test=TestLoader().loadTestsFromTestCase(AssertionError)
search_test=TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test=TestSuite([assertion_test,search_test])

kwargs={
    "output": 'Smoke report' 
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)