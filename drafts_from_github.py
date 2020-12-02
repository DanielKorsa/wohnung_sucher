# TODO: add argparser to set these values using arguments
search_location = "Berlin"
dump_folder = "data"

base_url = "https://www.immobilienscout24.de"
search_location_data = json.loads(
    requests.get(
        base_url + "/geoautocomplete/v3/locations.json?i=" + search_location
    ).text  # get location search results
)


# get the URL of first the entry of location search results,
# this is needed to limit the scraping to that location
search_url = (
        base_url
        + "/Suche"
        + search_location_data[0]["entity"]["geopath"]["uri"].split("?")[0]
        + "/wohnung-mieten?sorting=2"
          "&pagenumber="
)


#&enteredFrom=result_list