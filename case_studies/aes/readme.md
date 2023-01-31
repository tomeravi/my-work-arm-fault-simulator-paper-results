

Scripts :

1. generate_files.py - generate files/.s for aes.c and with 2 countermeaure

2. test_all.py       - run Armor and generate *rpt file

3. summaries_report.py - print summary of all types of faults and generate tmp files for next step

4. count_and_present.py - use tmp files and generate graph 

5. use #3 to use the tmp report of naked file and use it as input for add_ignore_labels_to_s.py

#####
Flow:
- generate_files.py -generate naked .s file and replacement .s file
- run test.all and summaries_report.py
- add_ignore_labels_to_s.py - use the report of naked to created naked with ignore labels
- run from generate_files.py just the replacement script with new .s file 
- run again test.all and summaries_report.py
- examine results with count_and_present.py