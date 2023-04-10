def scraper_endpoint(endpoint_extension):
    # Set up the API endpoint
    endpoint = 'https://statsapi.web.nhl.com/api/v1/' + endpoint_extension
    
    # Return the API response
    return endpoint