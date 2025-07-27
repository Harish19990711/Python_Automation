import unittest
import HtmlTestRunner
from test.home_page import TestHomePage

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Or to use HTMLTestRunner:
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
