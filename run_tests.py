import unittest
from HtmlTestRunner import HTMLTestRunner

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests", pattern="test_*.py")

    # Define the report file
    report_file = "test_report.html"

    # Run the tests and generate HTML report
    with open(report_file, "w") as report:
        test_runner = HTMLTestRunner(
            stream=report, report_title="Test Report", descriptions=True
        )
        test_runner.run(test_suite)
