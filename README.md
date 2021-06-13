## Solutions to programming problems

This repository contains my solutions to different programming problems.

The `run_tests.py` script compiles and runs all the programs, checking
they produce the expected output. Currently it supports the following
programming languages:

* Python (`.py`)
* R (`.R`, `.r`)
* C (`.c`)
* C++ (`.cpp`, `.cc`)
* Java (`.java`)
* Scala (`.scala`)
* SQL (`.sql`)

Each program is contained in a single file, and their expected output
is given in a file named the same as the program but with the `.out`
extension. Also, if a file with the `.in` extension exists, its
content is passed as the standard input when running the program (in
the case of SQL scripts, the `.in` file is used to initialize a SQLite
database).

### Author

Yasser Gonzalez
* Homepage - http://yassergonzalez.com
* Email - contact@yassergonzalez.com
