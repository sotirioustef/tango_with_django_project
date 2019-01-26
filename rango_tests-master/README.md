# Rango Tests for WAD2 and ITECH

## Introduction

These tests are only valid for the Rango app of the Tango with Django Book (https://leanpub.com/tangowithdjango19/) up to Chapter 10. Each test runs view and model tests. If you are in Chapter 6, tests from previous chapters might fail as the structure of templates/views changes as you develop Rango.

## Requirements:

* Python 3.7.1
* bcrypt==3.1.5
* certifi==2018.11.29
* cffi==1.11.5
* Django==1.11.17
* olefile==0.46
* Pillow==5.3.0
* pycparser==2.19
* pytz==2018.7
* selenium==3.141.0
* six==1.12.0
* urllib3==1.24.1
* wincertstore==0.2

## How-To

**THESE TESTS ONLY WORK ON WINDOWS! WE WILL NOT SUPPORT macOS and Linux**

For 10% assessment, there are 46 public tests (~68%)and 22 private tests (~32%) (Total: 68)

To run the tests, you need to do the following:

0. Create a new environment, e.g. `conda create -n rangotests python=3.7.1`, and activate the rangotests environment.

1. Clone this repository; **this repository should not be within your rango folder!**

2. Install requirements.txt, e.g. `pip install -r requirements.txt`

3. You are now ready to use the public tests and/or run individual tests for each chapter (including live server tests), so open a terminal/command prompt (Anaconda), navigate to the location where you clone this repository, activate the rango_tests workspace and run:

`python run_tests.py -u Your_GitHub_repository -s student_name -d YYYY-MM-DD`

The above script will take around 5 minutes to complete. This script will clone your repository from YYYY-MM-DD to the date you created your repository. The script will then checkout each commit you did over this period of time and run the tests against the commit. At the beggining you will see that some tests fail but this is the expected behaviour since at the beggining you have not completed the chapter tests. 

**NOTE: If a Windows Security Alert pops up, please choose to allow connections through the firewall. If in doubt, ask your lecturer/demonstrators.**

Alternatively, you can run each test for each chapter by copying the corresponding chapter's test and, "test_utils.py" and "decorators.py" into your "rango" directory and run (in your app directory):

`python manage.py test rango.tests_chapter3`

`python manage.py test rango.tests_chapter4`

`...`

`python manage.py test rango.tests_chapter10`

