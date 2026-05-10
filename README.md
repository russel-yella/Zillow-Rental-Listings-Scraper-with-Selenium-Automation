# Zillow Rental Listings Scraper with Selenium Automation

## Overview

This Python project scrapes rental property listings from Zillow and automatically uploads the data to a Google Form using Selenium.

The scraper extracts:

* Property prices
* Property addresses
* Listing links

The project demonstrates:

* Web scraping with BeautifulSoup
* Browser automation with Selenium
* Data cleaning using Regex
* Automated form submission

---

## Technologies Used

* Python
* Selenium
* BeautifulSoup4
* Requests
* Regex
* Chrome WebDriver

---

## Project Structure

```bash
.
├── main.py
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/russel-yella/Zillow-Rental-Listings-Scraper-with-Selenium-Automation.git
```

### 2. Navigate Into the Project

```bash
cd Zillow-Rental-Listings-Scraper-with-Selenium-Automation
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Add your Google Form URL inside the script:

```python
form_url = "YOUR_GOOGLE_FORM_URL"
```

2. Run the scraper:

```bash
python main.py
```

3. The bot will:

* Open Zillow
* Scrape rental listings
* Extract addresses, prices, and links
* Automatically submit the data to the Google Form

---

## Features

* Zillow rental listing scraping
* Dynamic content handling with Selenium
* Automated Google Form submission
* Regex-based price extraction
* Automated browser interaction

---

## Requirements

Install dependencies:

```bash
pip install selenium beautifulsoup4 requests webdriver-manager
```

---

## Disclaimer

This project is for educational purposes only.

Please review Zillow’s Terms of Service before scraping their website.

---

