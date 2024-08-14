from botasaurus_server.server import Server
from src.get_g2_products import get_g2_products
from casefy import titlecase
from urllib.parse import urlparse
from botasaurus_server.ui import (
    filters,
    sorts,
)


def get_category_from_url(url):
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split("/")
    return path_segments[-1]


# split_task accepts a data dictionary and returns a list of URLs for each task.
def split_task(data):
    result = []
    categories = []
    products = []
    max_reviews = data["max_reviews"]
    if max_reviews is None:
        max_reviews = 2500

    for query in data["search_queries"]:
        if "categories" in query:
            categories.append(query)
        else:
            products.append(query)
    ps = make_categories(data, categories, max_reviews)
    
    result.extend(ps) 
    
    if products:
        result.append(
            {
                "type": "product",
                "search_queries": products,
                "max_reviews": max_reviews,
                "api_key": data["api_key"],
            }
        )

    return result 

def make_categories(data, categories, max_reviews):
    ps = []
    p_set = set()
    if categories:
        for category in categories:            
            if category not in p_set:
                ps.append(
                    {
                        "type": "category",
                        "search_queries": category,
                        "max_reviews": max_reviews,
                        "api_key": data["api_key"],
                    }
                )
                p_set.add(category)
    if data["categories"]:
        for category in data["categories"]:
            category = "https://www.g2.com/categories/" + category
            if category not in p_set:
                ps.append(
                    {
                        "type": "category",
                        "search_queries": category,
                        "max_reviews": max_reviews,
                        "api_key": data["api_key"],
                    }
                )       
                p_set.add(category)
    return ps # Add the scraper to the server


def get_task_name(data):
    if data["type"] == "category":
        return titlecase(get_category_from_url(data["search_queries"]))
    return "All Products"


Server.add_scraper(
    get_g2_products,
    split_task=split_task,
    get_task_name=get_task_name,
    filters=[
        filters.SearchTextInput("product_name"),
        filters.MinNumberInput("reviews", label="Min Reviews"),
        filters.MaxNumberInput("reviews", label="Max Reviews"),
    ],
    sorts=[
        sorts.NumericDescendingSort("reviews"),
        sorts.NumericAscendingSort("reviews"),
        sorts.AlphabeticAscendingSort("product_name"),
    ],
)

Server.set_rate_limit(task=2, request=2, browser=2)


Server.configure(
    title="G2 Scraper",
    header_title="Made with Botasaurus",
    description="G2 Scraper helps you collect G2 product data, including names, product descriptions, reviews, ratings, comparisons, alternatives, and more.",
    right_header={
        "text": "Love It? Star It! ★",
        "link": "https://github.com/omkarcloud/g2-scraper/",
    },
)