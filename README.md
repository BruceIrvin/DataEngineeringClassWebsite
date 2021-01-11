# DataEngineeringWebsite
The website serves one data file in json format each day.

## 
Steps to set up the website:

	1. Spawn up a new VM instance. The minimum machine type required is e2-standard-2 (2 vCPUs, 8 GB memory).
	Allow HTTP and HTTPS traffic.
	2. ssh to your VM
	3. Run: sudo apt-get install git-all
	4. Run: git clone https://github.com/amans330/DataEngineeringWebsite.git
	5. Run: sudo apt-get install python3-pip python-dev
	6. Run: Type python3 -m pip install Django
	7. Change timezone of the VM:
		a. Type "sudo dpkg-reconfigure tzdata" and press enter.
		This will bring up a GUI which will guide you to change your timezone information.
	8. Open up port 8000 in the firewall. Our Django server will listen to requests on this port. To do this:
		a. Go to VPC network -> firewall -> create a firewall rule
		b. Give name as django, targets: all targets in the network, tcp: 8000
		c. Click create
	9. In the VM, go to folder DataEngineeringWebsite/scripts. Run: python3 create_data_files.py. This script
	will create the daily json files starting from day1.json, day2.json and so on.
	10. Run: python3 test_data_files.py to check if the json files contains the correct
	number of records.
	11. Run: cd ../mysite
	12. Run: "nohup python3 manage.py runserver 0.0.0.0:8000 &". This will start the django
	server in the background and would continue to run after you close the window.
	13. On your browser, go to url: "http://rbi.ddns.net/getBreadCrumbData". rbi.ddns.net is just
	an alias domain name and may change in the future.

