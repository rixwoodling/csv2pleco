csv2pleco.py

Converts a CSV vocabulary list into a Pleco-compatible import text file.

Usage:
python3 csv2pleco.py <input.csv>

Example:
python3 csv2pleco.py lesson1.csv

Input Format:
The CSV must contain at least three columns:

Chinese,Pinyin,English
你好,nǐ hǎo,hello
谢谢,xiè xie,thank you

The first row is treated as a header and is skipped.

Output:
The script creates a Pleco-compatible .txt file named after the first Chinese word in the list.

If a sibling "txt" directory exists, the file is written there:
txt/你好.txt

Otherwise, it is created beside the input CSV.

The output format is:
//你好
你好	nǐ hǎo	hello
谢谢	xiè xie	thank you

Notes:

* Skips the CSV header row.
* Ignores rows with fewer than three columns.
* Requires UTF-8 encoded input.
* Exits with an error if the input file does not exist or contains no valid entries.
* Output uses tab-separated fields in a .txt file for direct import into Pleco.
