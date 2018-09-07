import logging
import requests
import json


logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def scrap_process(self, storage):

        # You can iterate over ids, or get list of objects
        # from any API, or iterate throught pages of any site
        # Do not forget to skip already gathered data
        # Here is an example for you

        # UK Street-level crimes statistics:
        url = 'https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592&date=2018-07'
        response = requests.get(url)

        if not response.ok:
            logger.error(response.text)
            # then continue process, or retry, or fix your code

        else:
            # Note: here json can be used as response.json

            # save scrapped objects here
            # you can save url to identify already scrapped objects

            with open('scrapped_data.txt', 'w') as outfile:
                json.dump(response.json(), outfile)
