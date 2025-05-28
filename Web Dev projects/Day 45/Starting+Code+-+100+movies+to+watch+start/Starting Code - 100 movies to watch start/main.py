import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
titles = soup.find_all(name="h3",class_="title")
movies_titles = [item.getText() for item in titles]
for n in range(len(movies_titles) -1,-1,-1):
    Movies = movies_titles[n]

with open ("movies.txt", mode="w") as file:
    for moves in Movies:
        file.write(f"{moves}\n")