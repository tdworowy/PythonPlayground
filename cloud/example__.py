import gzip
import json
import urllib

import dask.bag


# client = Client()

def getGithubeEvents(month,day,hour):
    return 'http://data.githubarchive.org/2017-{:02d}-{:02d}-{}.json.gz'.format(month,day,hour)

urls = [getGithubeEvents(7,1,x) for x in range(1,10)]
urls_bag = dask.bag.from_sequence(urls,partition_size=1)


records = urls_bag \
    .map(urllib.request.urlopen)\
    .map(lambda  s : gzip.GzipFile(fileobj=s))\
    .flatten()\
    .map(lambda s : s.decode())\
    .map(json.loads)

records.count().compute()
#%time records.count().compute() works only from jupyter notebook

#TODO