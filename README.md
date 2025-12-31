# 📊 Quote Scraper – Web Scraping Assignment

A Python-based web scraping project that extracts quotes from **https://quotes.toscrape.com** using **Selenium** for browser automation and **BeautifulSoup** for HTML parsing.  
The scraper navigates through pagination, collects structured data, and stores it in a CSV file.

---

## 🚀 Objective

The goal of this assignment is to demonstrate the ability to:
- Scrape structured web data using Python
- Use Selenium for browser interaction and pagination handling
- Use BeautifulSoup for clean and efficient HTML parsing
- Handle basic exceptions and synchronization
- Export scraped data into a structured CSV format

---

## 🌐 Target Website

🔗 https://quotes.toscrape.com

---

## 📌 Features

✔ Scrapes data from the **first 3 pages**  
✔ Uses **Selenium** for navigation  
✔ Uses **BeautifulSoup** for parsing HTML  
✔ Handles pagination automatically  
✔ Uses **explicit waits** for stability  
✔ Handles basic exceptions (timeouts, missing elements)  
✔ Saves output in **CSV format**

---

## 📂 Project Structure

```bash
quote_scraper/
│
├── scraper.py # Main scraping script
├── output.csv # Scraped data output
└── README.md # Project documentation
```


## 📑 Data Extracted

For each quote, the following details are captured:

- **Quote Text**
- **Author Name**
- **Tags** (comma-separated)
- **Page Number** (source page)

---

## 📄 Output Format (CSV)

The generated `output.csv` file contains the following columns:

```bash
quote | author | tags | page_number
```

---

## 🛠️ Tech Stack & Libraries Used

- **Python 3.9+**
- **Selenium** – browser automation & pagination
- **BeautifulSoup (bs4)** – HTML parsing
- **CSV module** – structured data storage

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- Python 3.9 or above
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

---

## 📦 Installation

Install required Python libraries using pip:

```bash
pip install selenium beautifulsoup4
```

Execute the script using below command:

```bash
python scraper.py
```