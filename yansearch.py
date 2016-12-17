import requests
from random import choice

user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36']

def random_user_agent():
    agent = choice(user_agent_list)
    return {'User-Agent':agent}

class search_api(object):

    def __init__(self,user,api_key,proxies=None):
        self.user = user
        self.api_key = api_key
        self.proxies = proxies

    def get_results(self,query,lang='en',lr=213,sort_by='rlv',filter='none',num_results=10):
        user_credentials = 'https://yandex.com/search/xml?user={}&key={}'.format(self.user,self.api_key)
        query_local_lang = '&query={}&lr={}&l10n={}'.format(query.replace(' ','+'),lr,lang)
        rel_filter = '&sortby={}&filter={}'.format(sort_by,filter)
        results = '&groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D{}.docs-in-group%3D1'.format(num_results)
        final_request = '{}{}{}{}'.format(user_credentials,query_local_lang,rel_filter,results)

        try:
            if self.proxies == None:
                r = requests.get(final_request,headers=random_user_agent())
                result = r.text
            else:
                r = requests.get(final_request,headers=random_user_agent(),proxies=self.proxies)
                result = r.text
        except:
            print('Undocumented Error')
        return result
