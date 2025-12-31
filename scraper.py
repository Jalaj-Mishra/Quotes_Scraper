import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

URL = "https://quotes.toscrape.com/"


def scrape_quote():
    output_file = "output.csv"
    driver = webdriver.Chrome()

    # list of extracted quotes
    quotes_data = []

    try:
        driver.get(url=URL)
        for page_number in range(1,4):
            print(f"Scraping Page {page_number}")

            # add wait till the quotes are being load
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

            soup = BeautifulSoup(driver.page_source, "html.parser")
            quotes = soup.find_all("div", class_="quote")

            for quote in quotes:
                try:
                    text = quote.find("span", class_="text").get_text(strip=True)
                    author = quote.find("small", class_="author").get_text(strip=True)
                    tags = quote.find("div", class_="tags")
                    tag_list = [tag.get_text(strip=True) for tag in tags.find_all("a", class_="tag")]

                    quotes_data.append({
                        "quote": text,
                        "author": author,
                        "tags": ",".join(tag_list),
                        "page_number": page_number
                    })
                
                except AttributeError:
                    print("Something bad has taken place ! please check.")

            
            # Go to the next pagenumber by clicking on the button titled Next
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
                next_button.click()
            except NoSuchElementException:
                print("No more pages are present on the site.")
                break

            
    except TimeoutException:
        print("Page loading exceeded the time limit")
    

    finally:
        driver.quit()


    # writing the data to the output.csv file.
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        write = csv.DictWriter(
            file,
            fieldnames=["quote", "author", "tags", "page_number"]
        )
        write.writeheader()
        write.writerows(quotes_data)

    print(f"Scraping has been completed. Data saved to the file named {output_file}")






# calling the function.
scrape_quote()


