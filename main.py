import csv

# instantiate empty array
rowArray = [];
# pull out
with open('test.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        rowArray.append(', '.join(row))

#print(rowArray);
# ABOVE RETURNS ['policyID,statecode,county,eq_site_limit,hu_site_limit,fl_site_limit,fr_site_limit,tiv_2011','pug,goldenRetreiver,samoyed,beagle,,,','pug,goldenRetreiver,,,,]


# Start from 1 and end loop at index 3, because our test.csv has three rows
# We start the loop from 1 not 0 because we don't want to include the first row in our csv file
for i in range(1,3): #REPLACE 3 WITH YOUR ROW COUNTS

    # instantiate empty string
    lastString = '';
    # row is an individual string extracted from our rowArray. 'pug,goldenRetreiver,samoyed,beagle,,,'
    row = rowArray[i];
    # Turn string row into an array
    itemArray = row.split(',');   #['pug', 'goldenRetreiver', 'samoyed', 'beagle', '', '', '']

    # Loop through our new array called itemArray
    for index, val in enumerate(itemArray):
        if (val == ''):
            # if empty string found, assign the item before as a string called lastString
            lastString = itemArray[index-1];
            # end loop so we prevent nested looping error
            break;

    # with our last string now assigned, concatenate with a string 'unclassified_'
    outputString = 'unclassified_' + lastString;

    # Loop through itemArray again
    for index, val in enumerate(itemArray):
        if (val == ''):
            # replace every empty string with outputString
            itemArray[index] = outputString;
            f = open('empty.csv','w')
            f.write('hi there\n')
            f.close()

    print(itemArray);
