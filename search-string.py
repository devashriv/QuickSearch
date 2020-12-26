#Import os module
import os

# Ask the user to enter string to search
search_path = input("Enter directory path to search : ")
file_type = input("File Type : ")
search_str = input("Enter the search string : ")

# Create an array to store filenames
data = [['Filenames']] 

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
# If path does not exist, warn the user
if not os.path.exists(search_path):
    print("Invalid path")
    #prevent the window from automatically closing
    input("Press any key and hit enter to exit ")

# Repeat for each file in the directory  
for fname in os.listdir(path=search_path):

    # Apply file type filter   
    if fname.endswith(file_type):

        # Open file for reading
        fo = open(search_path + fname)

        # Read the first line from the file
        line = fo.readline()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find(search_str)
                if ( index != -1) :
                    print(fname, "[", line_no, ",", index, "] ", line, sep="")
                    data.append([fname])
                    
                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()

# Import csv module to store data in csv format
import csv

#data will be stored in output.csv file
with open('output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows(data)
    
#prevent the window from automatically closing
input("Press any key and hit enter to exit ") 