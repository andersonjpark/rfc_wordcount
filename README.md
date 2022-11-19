# RFC File cleaning project by Andy Park
****

## Purpose:
This program will read every raw RFC 5322 file inside the target directory, normalize every word in the body section, and will print a list of word frequencies per line.

## File Description:
* server.py is the python file that will be run to print a list of word frequencies.

* function.py is the python file that contains all the functions used in fastfreq and it's descriptions.


## Command Line:
````
python fastfreq.py <path> <n>
````
where n will be the number of threads and path will be directory path that would be analyzed.
