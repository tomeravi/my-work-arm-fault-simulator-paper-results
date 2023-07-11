
To generate the heat map like exist in this folder "faults_map_aes_case_studies_map.png":
- run the following :
  
  -  ../generate_files.py - generate files/.s for aes.c and with 2 countermeasure

  -  ../test_all.py       - run Armor and generate *rpt file

  -  create the summary report by this line  > grep "Transient Instruction" reports/<required report file>.rpt | awk -F'[:|]' '{printf $1 " : " $3 "\n"}' |sort > summary_report.txt

  -  ./faults_map.py with this summary_report.txt

