#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 17

def test_code():
    assert main.planets("mercury") == 1, 'planets("mercury") == 1 failed'
    assert main.planets("mars") == 4, 'planets("mars") == 4 failed'
    assert main.planets("russia") == "russia is not a planet", 'planets("russia") == "russia is not a planet" failed'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
