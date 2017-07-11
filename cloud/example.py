import dask.bag


def getGithubeEvents(month,day,hour):
    return 'http://data.githubarchive.org/2017-{:02d}-{:02d}-{}.json.gz'.format(month,day,hour)

urls = [getGithubeEvents(7,1,x) for x in range(1,10)]
urls_bag = dask.bag.from_sequence(urls,partition_size=1)

# client = Client()
# client

#TODO