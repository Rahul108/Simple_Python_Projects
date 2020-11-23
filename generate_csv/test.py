import requests
import json
import csv

url = "[__api_endpoint__]"


type_of_files = ["one","two","three"]
# Mension File types with files in list format
# like .... 
# one[] = ['file1.jpg','file2.txt']

i=0



with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["File", "Output(Address)"])
    
    def get_result_inside_csv(image_file,type_of_bill):
        payload = {'type': type_of_bill}
        file_name='test_data/%s'%image_file
        files = [
            ('image', open(file_name,'rb'))
        ]
        headers= {}

        response = requests.request("POST", url, headers=headers, data = payload, files = files)

        #  fetch particular response from json
        get_json = response.json()
        # like...
        # print(get_json["address"])
        
        writer.writerow([image_file, get_json["address"]])
    
    def perform_test(files,type_of_bill):
        for i in range(len(files)):
            get_result_inside_csv(files[i],type_of_bill)

    perform_test(one,type_of_files[0])
    perform_test(two,type_of_files[1])
    perform_test(three,type_of_files[2])