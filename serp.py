from serpwow.google_search_results import GoogleSearchResults
import json

import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SERP_TOK = os.environ.get("SERP_TOKEN")
serpwow = GoogleSearchResults(SERP_TOK)

#Using SERPWOW library to search google history
def search_google(params):
    result = serpwow.get_json(params)
    links_result = ""
    for i in range(0,(len(result["organic_results"]))):
        links_result += result["organic_results"][i]["link"] + "\n"
    links_result += "\n\nFriendly Reminder, only " + str(result["request_info"]["credits_remaining"]) + " searches are remaining."
    return(links_result)
