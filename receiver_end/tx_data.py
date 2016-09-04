import requests,time
URLROOT = "http://localhost:3000/"
SEC_KEY = "f88ee445-ddbe-47a6-b2a1-9134ea7cb1e2"

logfile_names = [nameLogFile("GND_PROCESSED_0_"),nameLogFile("GND_PROCESSED_1_"),nameLogFile("GND_PROCESSED_2")]
last_timestamps = [0,0,0]

EFM_boards = [0]
cloud_boards = [0,1]
hygro_boards = [0]

def nameLogFile(base):#find the first unused file name and use the one before it
  file_counter = 0
  file_name = "data/"+base + str(file_counter) + ".CSV"
  while os.path.isfile(file_name):
    file_counter += 1
    file_name =  "data/"+base + str(file_counter) + ".CSV" ##make sure we don't overwrite anything.
  file_counter -=1
  file_name =  "data/"+base + str(file_counter) + ".CSV"
  return file_name

def transmitRequest(data_line):
    if data_line[0]=='1':
        request_body = '{"key":\"'+SEC_KEY+'\",'
        requests_body += '"RSSI":\"' + data_line[1] + '\",'
        requests_body += '"SNR":\"' + data_line[2] + '\",'
        request_body += '"id":\"' + data_line[3] + '\",'
        requests_body += '"pressure":\"' + data_line[6] + '\",'
        requests_body += '"altitude":\"' + data_line[7] + '\",'
        requests_body += '"temperature":\"' + data_line[8] + '\",'
        requests_body += '"latitude":\"' + data_line[9] + '\",'
        requests_body += '"longitude":\"' + data_line[10] + '\",'
        requests_body += '"photodiode_count":\"' + data_line[11] + '\",'
        requests_body += '"photodiode_level":\"' + data_line[12] + '\",'
        if int(data_line[3],16) in EFM_boards:
            requests_body += '"EFM byte 1":\"' + data_line[13] + '\",'
            requests_body += '"EFM Byte 2":\"' + data_line[14] + '\",'
        if int(data_line[3],16) in cloud_boards:
            requests_body += '"cloud_average":\"' + data_line[15] + '\",'
            


        requests.post(URLROOT, data = request_body, headers={'content-type':'application/json'})
    else:
        print "believe crc failed—check first conditional in transmitRequest"

def checkFile(fileIndex):
  f = open(logfile_names[fileIndex],'r')
  x = f.read();
  f.close();
  x = x.split('\n')
  x.reverse()
  for i in x:
      if i[-1]=='#':
          values = i.split(',')
          if values[19] > last_timestamps[fileIndex]:
              last_timestamps[fileIndex] = values[19]
              transmitRequest(values)
