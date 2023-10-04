# Reboot Devices

This is the source code for Reboot Devices, a simple code to reboot Meraki devices in bluk using Meraki API calls.

## Solution Components
* Meraki Dashboard API

## Installation:
####
```console
git clone https://github.com/YiRenRenYi/RebootDevices.git
```
#### Set up a Python venv
First make sure that you have Python 3 installed on your machine. We will then be using venv to create
an isolated environment with only the necessary packages.

##### Install virtualenv via pip
```
$ pip install virtualenv
```

##### Create a new venv
```
Change to your project folder
$ cd code

Create the venv
$ virtualenv venv

Activate your venv
$ source venv/bin/activate
```

#### Install dependencies
```
$ pip install -r requirements.txt
```

#### Meraki details:
You can deploy this prototype in a lab environment or on your own Meraki dashboard online
[here](https://account.meraki.com/secure/login/dashboard_login).

To generate an API KEY, refer to the documentation [here](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API#Enable_API_access).
You will use this for using this application.

Fill in the details of your Meraki API in the .env file


## How to Use

Use the Meraki dashboard to download device serial number, and put in the MX.csv file. Please remove any quotation marks

Run the code main.py. It will read the serial number from the MX.csv file and reboot the device one-by-one.

The devices failed to be rebooted will be listed into the file RebootFailedDevices.csv with their serial numbers. Please take a copy of the serial numbers before you re-run the code, as the file will be re-writed.

Copy and paste the serial numbers from the RebootFailedDevices.csv into MX.csv, and run the code main.py again to reboot these devices until all devices get rebooted successfully.

### DISCLAIMER:
<b>Please note:</b> This script is meant for prototype purposes only. All tools or scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
