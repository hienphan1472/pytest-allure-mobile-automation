# pytest-allure-mobile-automation

# Run test in parallel with pytest-xdist lib:
    pytest -n=2 --alluredir=./allure/ --driver iOS --env QA

# Run test with allure report:
    pytest tests/ios --alluredir=./allure/ --driver iOS --env QA

# Generate report:
    allure generate "./allure/" -o ./reports/ --clean