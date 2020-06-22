A script for entering google mail 
(login and password should be specified in .env file, see instructions in example_dotenv_file)

Latest version of selenium and chromedriver are used

run_gmail_tests.py - is used for running tests

tested only with chromedriver (ChromeDriver 83.0.4103.39 ) and only with simplest configuration of selenium grid (following official manual)

There are several parts of code which may appear strange. Especially the use of time.wait is explained by using two-factor authentification
