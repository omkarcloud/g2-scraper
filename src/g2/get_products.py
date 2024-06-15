from botasaurus.cache import DontCache
from .helpers import  convert_unicode_dict_to_ascii_dict
from botasaurus.task import task
from time import sleep
from .utils import default_request_options
import requests

FAILED_DUE_TO_CREDITS_EXHAUSTED = "FAILED_DUE_TO_CREDITS_EXHAUSTED"
FAILED_DUE_TO_NOT_SUBSCRIBED = "FAILED_DUE_TO_NOT_SUBSCRIBED"
FAILED_DUE_TO_NO_KEY = "FAILED_DUE_TO_NO_KEY"
FAILED_DUE_TO_UNKNOWN_ERROR = "FAILED_DUE_TO_UNKNOWN_ERROR"

def do_request(data, endpoint, retry_count=3):
    print(data)
    params = data["params"]
    key = data["key"]

    if retry_count == 0:
        print(f"Failed to get data, after 3 retries")
        return DontCache(None)

    url = "https://g2-data-api.p.rapidapi.com/" + endpoint

    querystring = params
    headers = {
        "X-RapidAPI-Key": key,
    	"X-RapidAPI-Host": "g2-data-api.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=querystring)
    response_data = response.json()
    if response.status_code == 200 or response.status_code == 404:
        if isinstance(response_data, dict):
            message = response_data.get("message", "")
            if "API doesn't exists" in message:
                return DontCache({
                            "data":  None,
                            "error":FAILED_DUE_TO_UNKNOWN_ERROR
                        })

        
        return {
            "data": convert_unicode_dict_to_ascii_dict(response_data),
            "error": None
        }
    else:
        message = response_data.get("message", "")
        if "exceeded the MONTHLY quota" in message:
            return  DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_CREDITS_EXHAUSTED
                    })
        elif "exceeded the rate limit per second for your plan" in message or "many requests" in message:
            sleep(2)
            return do_request(data, endpoint, retry_count - 1)
        elif "You are not subscribed to this API." in message:
            
            return DontCache({
                        "data": None,
                        "error": FAILED_DUE_TO_NOT_SUBSCRIBED
                    })

        print(f"Error: {response.status_code}", response_data)
        return  DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_UNKNOWN_ERROR, 
                    })


@task(**default_request_options, parallel=5)
def get_products(data, metadata):
    if not metadata.get('key'):
         return  DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_NO_KEY
                    })
    
    data = {
        **metadata,
        "params": data,
    }

    return do_request(data,"g2-products")


@task(**default_request_options, parallel=5)
def get_products_by_category(data, metadata):
    if not metadata.get('key'):
         return  DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_NO_KEY
                    })
    
    data = {
        **metadata,
        "params": data,
    }

    return do_request(data,"g2-categories")
