from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "https://www.lichfielddc.gov.uk/Inspire-data-sets/Lichfield%20District%20Council%20Polling%20Stations/LDC_Polling_Stations_Shapefile.zip"
districts_url = "https://www.lichfielddc.gov.uk/Inspire-data-sets/Lichfield%20District%20Council%20Polling%20Districts/Lichfield%20District%20Council%20Polling%20Districts%20Shapefile.zip"
council_id = 'E07000194'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts')
districts_scraper.scrape()
