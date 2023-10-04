import meraki
import os
import csv
from dotenv import load_dotenv

load_dotenv()

meraki_base_url = os.getenv("MERAKI_BASE_URL")
meraki_api_key = os.getenv("MERAKI_API_KEY")

dashboard = meraki.DashboardAPI(meraki_api_key, suppress_logging=True)
SQ=['serial']


with open('MX.csv', newline='') as csvfile:
    SQreader = csv.reader(csvfile, delimiter=',')
    line_pendingReboot = 0
    for row in SQreader:
        if line_pendingReboot >=1:
            serial = row[1]
            print("*************************")
            print(serial)
            if serial != "":
                response = dashboard.devices.rebootDevice(
                    serial
                    )
                print(response)
                if response == {'success': False}:
                    SQ.extend([serial])
                print("=========================")
        line_pendingReboot +=1

with open('RebootFailedDevices.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(SQ)    