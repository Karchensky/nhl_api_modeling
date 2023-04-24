# This function sets up the API endpoint for scraping NHL data
def scraper_endpoint(endpoint_extension, api_shift_alternate=None):
    
    if api_shift_alternate is None:
        endpoint = 'https://statsapi.web.nhl.com/api/v1/' + endpoint_extension

    if api_shift_alternate is not None:
        endpoint = 'https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId=' + endpoint_extension
    
    # Return the API response
    return endpoint