# This program says hello - jim doran


import json, urllib
'''
for x in range(0, 3):
    print "We're on loop %d" % (x)
'''

j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
print j['two']

url="http://bluepages.ibm.com/BpHttpApisv3/slaphapi?ibmperson/uid=305385897.list/byjson?*"
#  "name": "glTeamLead", "value": [ "uid=331567848,c=ch,ou=bluepages,o=ibm.com" ] },


response = urllib.urlopen(url)
data = json.loads(response.read())
print data
print data['glTeamLead']

# blah blah


'''
  hits_hits = []
    flist = glob.glob("lon02/compliance/compliance-2016.10.*.json")
    flist.sort()
    for f in flist:
        print "Loading",f
        with open(f) as json_file:
            data = json.load(json_file)
        if "hits" in data.keys() and  "hits" in data["hits"]:
            tmp_list = data["hits"]["hits"]

            for i in range(0,len(tmp_list)):

                description = tmp_list[i]["_source"]["description"]
                namespace = tmp_list[i]["_source"]["namespace"]
                # skip container
                if "registry" not in namespace:
                    continue
                # skip garbage images
                if is_garbage(namespace):
                    continue
                # skip verdict
                if description=="Overall compliance verdict":
                    continue
                # append to hits_hits
                hits_hits.append(tmp_list[i])
                '''

