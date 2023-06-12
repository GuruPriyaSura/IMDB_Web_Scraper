import requests
from bs4 import BeautifulSoup
import datetime
import csv

def scrape_movie_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")


    movie_name = soup.select_one("h1").text.strip()

    directors = [director.text.strip() for director in soup.select(".ipc-metadata-list-item__list-content-item--link")]

    stars = [star.text.strip() for star in soup.select(".ipc-metadata-list-item__list-content-item--link")]

    storyline_element = soup.select_one(".ipc-html-content.ipc-html-content--base")
    storyline = storyline_element.text.strip() if storyline_element else "N/A"

    today = datetime.date.today()

    header = ['Movie Name', 'Directors', 'Stars', 'Storyline', 'Date']
    data = [movie_name,','.join(directors), ','.join(stars),
            storyline, today]
    with open('DOBW.csv', 'a+', newline='', encoding='UTF8') as f:

        writer = csv.writer(f)
        writer.writerow(data)


scrape_movie_info('https://www.imdb.com/title/tt0101258/')
