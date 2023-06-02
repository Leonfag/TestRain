# TestRain

1 - Create o replicate virtual environment
From console terminal

1 - Install pipenv library

Note: Validate if you have pip library install in your computer

pip install pipenv
2 - Clone or download the repository

3 - From root folder project

pipenv install
pipenv shell
This command recreate the virtual environment, be careful when the environment is created, you should see the path where the virtual environment was created

4 - For initiate the virtual environment.

source ./path/virtual/environment/bin/activate

To run tests:

python -m pytest -n auto ./test_rain.py
