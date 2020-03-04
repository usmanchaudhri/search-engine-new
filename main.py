from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
from sanic_openapi import swagger_blueprint, openapi_blueprint
from sanic_openapi import doc as openapi
from indexer import Indexer
from searcher import SearchService
from searcher import UsersSearchService
from searcher import TicketsSearchService
from searcher import OrganizationSearchService

import sanic.response
import logging
import typing
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Sanic()
CORS(app, expose_headers=['qtime'])  # enabling Cross-origin Resource Sharing for all endpoints
app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)
# app.error_handler = None

# initializes indexer data this could be from file or data source
search_indexer: Indexer = Indexer()

# initialize search services with data
userSearch: SearchService = UsersSearchService(search_indexer.userDoc)
ticketSearch: SearchService = TicketsSearchService(search_indexer.ticketDoc)
organizationSearch: SearchService = OrganizationSearchService(search_indexer.organizationDoc)

@app.route("/")
async def test(request):
    return json({"hello: world"})

@app.route("/1")
async def tos(request):
    return sanic.response.text('Proprietary Software! Absolutely No Public License Granted for Any Use or Any Purpose')

@app.route("/search", methods=["GET"], strict_slashes=True)
async def search(request):
    query_args: typing.List = request.query_args
    query: str = '&'.join([f'{key}=="{value}"' for key, value in query_args if value != ''])
    logging.info("search query %s", query)

    userSearchResponse: pd.DataFrame = userSearch.search_by_query(query)
    ticketSearchResponse: pd.DataFrame = ticketSearch.search_by_query(query)
    organizationSearchResponse: pd.DataFrame = organizationSearch.search_by_query(query)

    response = sanic.response.json(None)
    return response

@openapi.summary("User searches")
@app.route("/usersearch", methods=["GET"], strict_slashes=True)
async def user_search(request):
    query_args = request.query_args

    query = '&'.join([f'{key}=="{value}"' for key, value in query_args if value != ''])
    res = userSearch.search_by_query(query.lower())
    response = sanic.response.json(res.to_dict())
    return response

@openapi.summary("Ticket searches")
@app.route("/ticketsearch", methods=["GET"], strict_slashes=True)
async def ticket_search(request):
    query_args = request.query_args

    query = '&'.join([f'{key}=="{value}"' for key, value in query_args if value != ''])
    res = ticketSearch.search_by_query(query.lower())
    response = sanic.response.json(res.to_dict())
    return response

@openapi.summary("Organizatin searches")
@app.route("/organizationsearch", methods=["GET"], strict_slashes=True)
async def organization_search(request):
    query_args = request.query_args

    query = '&'.join([f'{key}=="{value}"' for key, value in query_args if value != ''])
    res = organizationSearch.search_by_query(query.lower())
    response = sanic.response.json(res.to_dict())
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")