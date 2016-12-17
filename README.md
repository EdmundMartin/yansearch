# yansearch
Python wrapper over the Yandex Search API makes the task of making a Yandex Search API request more easy to make. Additional features to be added.
### Usage Examples
```python
from yansearch import search_api

search_scraper = search_api('yandex_user_name','yandex_api_key')

xml_file = search_scraper.get_results('Your Keyword')
```
The wrapper sits over the Yandex Search API and requires only one argument to work, the keyword you want to collect results for. At the moment there is only way in which they returned results can be grouped is by relevancy. This seems to make the most sense as it is the way which results are grouped when you make a search in Yandex. 

## Optional Arguments

```python
from yansearch import search_api

search_scraper = search_api('yandex_user_name','yandex_api_key')

xml_file = search_scraper.get_results('Your Keyword','ru',213,rlv,'none',50)
```

The function also takes a number of optional arguments.
* Language - The Yandex search supports a number of languages - however the accepted languages depend on which version of the API you use. Worldwide supports only 'en' (English), while the standard local variant of the API supports Russian, Ukrainian, and Kazakh. 
* The '213' number refers to the location in which the search is being made. The full list of various locations can be found 
