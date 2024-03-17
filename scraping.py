from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def scarping(query):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    query = f'route {query} indonesia'
    links = []
    n_pages = 2

    for page in range(1, n_pages):
            url = f"http://www.google.com/search?q={query}&start={(page - 1) * 10}"
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            search = soup.find_all('div', class_="tF2Cxc")
            
            for h in search:
                link = h.find('a')['href']
                links.append(link)
        
    return links
    