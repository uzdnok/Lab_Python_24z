from bs4 import BeautifulSoup
import requests
# Wczytywanie zawartości strony HTML
html_file_path = "https://www.rankinguefa.pl"#"https://www.mimuw.edu.pl/pl/"
response = requests.get(html_file_path)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())
lista_h3 = soup.find_all('h3', class_='nlg-entry-title')
#print(soup.find_all('h3', class_='nlg-entry-title'))
#print(lista_h3)
i = 0
for element in lista_h3:
    print(element)