from bs4 import BeautifulSoup
from yansearch import search_api

def output_ranks(xml):
    soup = BeautifulSoup(xml,'lxml-xml')
    groups = soup.find_all('group')
    rank_num = 1
    query = soup.find('query').contents
    for group in groups:
        url = group.find('url').contents
        domain = group.find('domain').contents
        rank = rank_num
        output_line = '"{}","{}","{}","{}"\n'.format(query[0],url[0],domain[0],rank)
        rank_num += 1
        with open('SearchResults.csv','a',encoding='utf-8') as result_file:
            result_file.write(output_line)

keyword_list = ['houses in london','flights to moscow']

search_scraper = search_api('Yandex_User_Name','Yandex_API_Key')

for keyword in keyword_list:
    xml_file = search_scraper.get_results(keyword)
    output_ranks(xml_file)
