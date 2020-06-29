import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url= 'https://www.imdb.com/search/title/?release_date=2017&sort=num_votes,desc&page=1'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
movie_containers = page_soup.find_all('div', class_ = 'lister-item mode-advanced')
filename = "filmovi.txt"
import io
with io.open(filename, 'w',encoding="utf-8") as f:
    first_movie = movie_containers [0]
    for first_movie in movie_containers:
        name= first_movie.h3.a.text
        year = first_movie.h3.find('span',class_='lister-item-year').text
        imdb=first_movie.strong.text
        vote = first_movie.find('span', attrs={'name':'nv'})['data-value']
        print("name " + name)
        print("year " + year)
        print("imdb " + imdb)
        print("votes " + vote)
        f.write(name + "," + year + ","+ imdb + ","+ vote + "\n")

    f.close()
