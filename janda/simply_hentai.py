import requests
import json
from .utils.parser import *

BASE_URL = Api()

class SimplyHentai(object):
    """ Simply-hentai API wrapper 
    
    Methods
    -------
    get : function
        Gets doujin from path given

    get_related: function
        Gets related or similar doujin from path given

    get_random : function
        Gets random doujin on Hentai2read
    """

    def __init__(self, api_key: str = ''):
        """Initializes the Pururin.

        Parameters
        ----------
        api_key : str
            scathach.dev API key (optional)
        """
        if api_key == '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}

    async def get(self, path: str):
        """Gets doujin from path given

        path: https://www.simply-hentai.com/fate-grand-order/perros => 'fate-grand-order/perros'

        Parameters
        ----------
        path : str
            The path url

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the specific path response.
        """

        if str(path).isdigit():
            raise ValueError('Invalid path, must be a str')

        path = path.strip('/')
        self.specs['g'] = path

        try:
            path = str(path)

        except ValueError or path.isdigit():
            raise ValueError('Path must be a str')

        data = requests.get(BASE_URL.simply_hentai, params=self.specs)

        self.final = json.loads(better_object(data.json()), encoding="utf-8")
   
        return better_object(self.final)

    async def get_related(self, path: str):
        """Gets related or similar doujin from path given

        path: https://www.simply-hentai.com/fate-grand-order/perros => 'fate-grand-order/perros'

        Parameters
        ----------
        path : str
            The path url

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the specific path response.
        """

        if str(path).isdigit():
            raise ValueError('Invalid path, must be a str')

        path = path.strip('/')
        self.specs['query'] = path

        try:
            path = str(path)

        except ValueError or path.isdigit():
            raise ValueError('Path must be a str')

        data = requests.get(BASE_URL.simply_hentai + "args.php", params=self.specs)

        self.final = json.loads(better_object(data.json()), encoding="utf-8")
   
        return better_object(self.final)

    async def get_random(self):
        """Gets random doujin on Hentai2read

        Returns
        -------
        dict
            The book object that represents the doujin response.
        """
        data = requests.get(BASE_URL.simply_hentai + 'random')

        return better_object(data.json())

