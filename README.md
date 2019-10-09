# datescrape
Python library that scrapes a date object from a descriptive string using regex.

Datescrape is a python library, the purpose of which is to take in a generic string describing a date and time, and return a date object of the "best guess"

Some examples include:
"jan 1 at 2pm"  => 2020-01-01 14:00:00        
"June 5th 1920" => 1920-06-05 23:59:00    
"4 2 2020"      => 2020-02-04 23:59:00

