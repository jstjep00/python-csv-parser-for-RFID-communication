
from csv import reader

"""
    Parser that counts different RFID packet types between 
    succesful packet trasnfers
"""

num = 1
# reads csv file as csvfile
with open("com_list_puni.csv", "r") as csvfile:
    readCSV = reader(csvfile)
    #print(readCSV)
    for row in readCSV:
        print(row[0])
        # the communication is between 2 PWR_DWN packets
        if (row[0] == 'PWR_DWN'):
            # all different packet types counts
            QUERY_count = 0
            ACK_count = 0
            REP_count = 0
            ERROR_count = 0
            QADJ_count = 0
            QREP_count = 0
            #print("radin fajl "+str(num))
            output_file = open('output.txt', "a+")
           # num += 1
            dict = ''
            for row in readCSV:

                if (row[0] == 'QUERY'):
                    QUERY_count += 1
                elif (row[0] == 'ACK'):
                    ACK_count += 1
                elif (row[0] == 'QREP'):
                    QREP_count += 1
                elif (row[0] == 'ERROR'):
                    ERROR_count += 1
                elif (row[0] == 'QADJ'):
                    QADJ_count += 1

                dict = {"QUERY":QUERY_count, "ACK":ACK_count, "QREP":QREP_count, "ERROR":ERROR_count, "QADJ":QADJ_count}

                if (row[0] == 'PWR_DWN'):

                    # appends to file the dictionary of packet communication
                    output_file.write(str(num)+":"+str(dict) + '\n')

                    # restarts the counter for next communication segment
                    QUERY_count = 0
                    ACK_count = 0
                    REP_count = 0
                    ERROR_count = 0
                    QADJ_count = 0
                    QREP_count = 0
                    
                    output_file = open('output.txt', "a+")
output_file.close()
