# datescrape
Datescrape is a python library, the purpose of which is to take in a generic string describing a date and time, and return a date object of the "best guess"

Some examples include:

"jan 1 at 2pm"  => 2020-01-01 14:00:00        
"June 5th 1920" => 1920-06-05 23:59:00    
"4 2 2020"      => 2020-02-04 23:59:00

The general format is "date @ time" or "date at time".
Time and date can be specified on their own using "date" or "@time".

If time is not specified, it will be set to 23:59:00 by default.
If date is not specified, it will be set to either the current day, or tomorrow if the current time is after the specified time.


