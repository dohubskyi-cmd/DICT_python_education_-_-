import requests
import string
import os
from bs4 import BeautifulSoup

def scrape_page(page_num, target_type):
    dir_name = f"Page_{page_num}"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={page_num}"
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = soup.find_all('article')
    for article in articles:
        a_type = article.find('span', {'data-test': 'article.type'})
        if a_type and a_type.text.strip() == target_type:
            link_tag = article.find('a', {'data-track-action': 'view article'})
            title = link_tag.text.strip()
            filename = title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_') + ".txt"
            
            art_res = requests.get("https://www.nature.com" + link_tag['href'])
            art_soup = BeautifulSoup(art_res.content, 'html.parser')
            body = art_soup.find('div', class_=lambda x: x and ('body' in x or 'content' in x))
            
            if body:
                with open(os.path.join(dir_name, filename), 'wb') as f:
                    f.write(body.text.strip().encode('utf-8'))

def main():
    try:
        pages = int(input("> "))
        a_type = input("> ")
        for i in range(1, pages + 1):
            scrape_page(i, a_type)
        print("Saved all articles.")
    except ValueError:
        print("Incorrect input.")

if __name__ == "__main__":
    main()
