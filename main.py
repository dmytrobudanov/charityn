from seleniumwire import webdriver
from time import sleep
import utils as parse_utils
import html_parser as html_parser
import io_methods as iom
import startup as stup

if __name__ == "__main__":
    driver = webdriver.Chrome()
    number_of_page = html_parser.get_number_of_pages(driver,"")
    df = parse_utils.create_df()
    base_url = "https://www.charitynavigator.org/search?sizes=large&page={page}"
    for page in range(1, number_of_page+1):
        links = html_parser.collect_link_to_charity(driver,base_url.format(page=page))
        df = parse_utils.add_charity_navigator_link(df, links)
        #break

        for index, rows in df.iterrows():
            driver.get(rows["charity_navigator_link"])
            soup = html_parser.get_soup(driver.page_source)
            info = [
                rows["charity_navigator_link"],
                html_parser.get_title(soup),
                html_parser.get_site(soup),
                html_parser.get_location(soup),
                html_parser.get_ein(soup),
                html_parser.get_description(soup),
                html_parser.get_rating(soup)
            ]
            print(info)
            df = parse_utils.add_info(df, index, info)




            df.to_csv('data.csv')