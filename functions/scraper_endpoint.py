# This function sets up the API endpoint for scraping NHL data
def scraper_endpoint(endpoint_extension, api_shift_alternate=None, power_play_toi_alternate=None, penalty_kill_toi_alternate=None):

    if api_shift_alternate is None and power_play_toi_alternate is None and penalty_kill_toi_alternate is None:
        endpoint = 'https://statsapi.web.nhl.com/api/v1/' + endpoint_extension

    if api_shift_alternate is not None:
        endpoint = 'https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId=' + endpoint_extension

    if power_play_toi_alternate is not None:
        endpoint = 'https://api.nhle.com/stats/rest/en/team/powerplaytime?&cayenneExp=gameId=' + endpoint_extension
    
    if penalty_kill_toi_alternate is not None:
        endpoint = 'https://api.nhle.com/stats/rest/en/team/penaltykilltime?&cayenneExp=gameId=' + endpoint_extension

    # Return the API response
    return endpoint