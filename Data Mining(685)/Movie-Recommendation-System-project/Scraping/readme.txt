Dependencies:
	BeautifulSoup
	tqdm

The whole scraping took about ~10hr on 50Mbps connection.

The scraping process is as follows:
- Scrape movies box office collection from boxofficeindia.com.
- Scrape actors and their movies from boxofficeindia.com.
- Find imdb id of scraped movies by matching names and release year by imdb dataset.
- Scrape lead actors of movies from imdb.com.
