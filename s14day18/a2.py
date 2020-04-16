#coding:utf-8

def write():

    need_data = []
    for i in range(1,150):
        file_name = 'text_new_%s' % str(i).zfill(3)

        with open(file_name, 'r') as fp:
            for line in fp.readlines():
                a = (line.strip('\n').split('###'))
                title = a[0]
                info = a[1]
                need_data.append([title, info])
        #print((need_data[0][0]))
        #return

        import requests

        for u in need_data:
            data = {"add": {"doc": {"id": u[0], "*字段名*": u[1]}}}
            params = {"boost": 1.0, "overwrite": "true", "commitWithin": 1000}
            url = 'http://192.168.111.200:8983/solr/mycore/update?wt=json'
            headers = {"Content-Type": "application/json"}
            r = requests.post(url, json=data, params=params, headers=headers)
            print(r.text)

#test()
# write()

def search_data(message='龙'):
    import requests

    url = 'http://192.168.111.200:8983/solr/mycore/select?q=_____:"\%s"&wt=json&indent=true' % message
    r = requests.get(url, verify=False)
    print(r.json())
    #r.text
    #r = r.json()['response']['numFound']
    #print
    #message + ":" + str(r)


search_data()

