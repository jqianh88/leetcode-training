'''
Binary Strings: Have to review and work on this

A binary string is a string that only has
two characters, usually the numbers 0 and 1,
and it represents a series of binary digits.


In computer programming, binary string variables are
used to store binary data, which is data that is represented
in a binary (base-2) format, rather than a text (base-10) format. 
The three most common types of binary string variables used in 
databases are “BINARY”, “VARBINARY”, and “BLOB”. Here’s a brief 
overview of each:

BINARY: The BINARY data type is used to store fixed-length binary data.
The data that is put in the column must always be the same size and the 
size of the column must be defined when the table is formed.
A BINARY column, for instance, can only hold binary strings that are 
exactly 10 bytes long if its definition is BINARY(10).

VARBINARY: The VARBINARY data type is similar to BINARY but allows 
for variable-length binary data. As a result, the data that is kept 
in the column can be of any size, and the column size does not need to 
be defined. A VARBINARY column, for instance, can store binary strings 
that are any size between 0 and 65, 535 bytes.

BLOB: The BLOB (Binary Large Object) data type is used to store large 
binary data objects, such as images, audio files, or video files. 
When the size of the data being saved surpasses the largest size permitted 
by the BINARY or VARBINARY data types, BLOB columns are commonly employed. 
BLOB columns are frequently used to store files that are too big to fit 
directly in a table since they can hold binary data of any size.



Binary	 	 
 	    0	 	Start at 0
•	    1	 	Then 1
••	    10	 	Start back at 0 again, but add 1 on the left
•••	    11	 	 
••••	100	 	start back at 0 again, and add one to the number on the left...
                ... but that number is already at 1 so it also goes back to 0 ...
                ... and 1 is added to the next position on the left
•••••	101	 	 
••••••	110	 	 
•••••••	111	 	 
•••••••• 1000	 	Start back at 0 again (for all 3 digits),
                    add 1 on the left
••••••••• 1001	 	And so on!
'''