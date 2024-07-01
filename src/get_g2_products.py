from botasaurus.task import task
from .g2 import G2
@task
def get_g2_products(data):
    if data['type'] == "category":
        cats = G2.get_categories(data["search_queries"], data["max_reviews"] , data["api_key"]) 
        return G2.get_products([x['link'] for x in cats['results']], data["max_reviews"], data["api_key"])
    else:
        return G2.get_products(data["search_queries"], data["max_reviews"] , data["api_key"])