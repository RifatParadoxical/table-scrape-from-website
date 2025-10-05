import pandas as pd
import requests
from io import StringIO

url = 'https://pixelscan.net/blog/scraping-twitter-guide/'
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    )
}

r = requests.get(url, headers=headers)
r.raise_for_status()

tables = pd.read_html(StringIO(r.text))
if tables:
    df = tables[0]
    df.to_csv('twitter_scrape_guide.csv', index=False, encoding='utf-8-sig')
    print(df.to_string())
else:
    print("No tables found.")