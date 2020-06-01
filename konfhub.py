
import json
import sys
from collections import OrderedDict

# Opening JSON file 
f = open('get-list-of-conferences.json',) 

data = json.load(f) 
  
reload(sys)
sys.setdefaultencoding('utf8')



#to remove to duplicate according to confRegUrl
data["paid"] = { each['confRegUrl'] : each for each in data["paid"] }.values()



j=0
for i in data["paid"]:
	city_name = data["paid"][j]["city"]
	conf_start_date = data["paid"][j]["confStartDate"]
	conf_entry_type = data["paid"][j]["entryType"]
	conf_url = data["paid"][j]["confUrl"]

	print '"{}"'.format(city_name),",",conf_start_date,",",conf_entry_type,",",'"{}"'.format(conf_url)
	j = j+1

# Closing file 
f.close() 
