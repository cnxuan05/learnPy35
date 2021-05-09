import json
import uuid
a = {'a':1}
file = str(uuid.uuid1()) + '.loglog'

with open(file, 'w+') as fp:
    fp.write(json.dumps(a))


