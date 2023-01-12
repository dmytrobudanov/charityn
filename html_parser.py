from time import sleep
from seleniumwire import webdriver
from bs4 import BeautifulSoup as bs


def get_soup(html: str) -> bs:
    return bs(html, 'html.parser')

def get_number_of_pages(driver: webdriver, url: str) -> int:
    return 1000

def collect_link_to_charity(driver: webdriver, url: str) -> list:
    # response = requests.get(url).content
    driver.get(url)
    sleep(1)
    soup = get_soup(driver.page_source)
    grid_block = soup.find('div',{'class':'tw-mt-3 tablet:tw-mt-14 tablet:tw-px-12 tw-w-full tw-max-w-[1200px]'}) \
                     .find('div',{'class':'tw-space-y-3 tablet:tw-space-y-5'}) \
                     .find_all('a',{'class':'SearchResult-module__SearchResult___Z0d4h'})
    links = ["https://www.charitynavigator.org" + link['href'] for link in grid_block]
    return links

def get_title(soup: bs) -> str:
    title = ''
    try:
        title = soup.find_all('div',{'class':'row-no-margin-mobile row'})[-1].find_all('p')[2].text
    except Exception as e:
        print(f"title - {str(e)}")

    return title

def get_site(soup: bs) -> str:
    site = ''
    try:
        site = soup.find('div',{'class':'charity-profile-bullets row-no-margin-mobile row'}).find_all('div')[-1]\
                .find('p').find('span').find('a')['href']
    except Exception as e:
        print(f"site - {str(e)}")

    return site

def get_location(soup: bs) -> str:
    location = ''
    try:
        location = soup.find('div',{'class':'charity-profile-bullets row-no-margin-mobile row'}).find_all('div')[-1]\
                .find_all('p')[1].text.strip()
    except Exception as e:
        print(f"location - {str(e)}")

    return location

def get_ein(soup: bs) -> str:
    ein = ''
    try:
        ein = soup.find_all('div',{'class':'row-no-margin-mobile row'})[-1].find_all('p')[0].text
    except Exception as e:
        print(f"ein - {str(e)}")

    return ein

def get_description(soup: bs) -> str:
    description = ''
    try:
        description = soup.find_all('div',{'class':'row-no-margin-mobile row'})[-1].find_all('p')[2].text
    except Exception as e:
        print(f"description - {str(e)}")

    return description

def get_rating(soup: bs) -> str:
    rating = ''
    try:
        rating = soup.find_all('span',{'class':'dashboard-rating'})[0].text
    except Exception as e:
        print(f"rating - {str(e)}")

    return rating
