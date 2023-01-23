# ER_scraper

Earning Reports Scraper and Parser is a tool for collecting and analyzing earning reports from publicly traded companies.

### Features
- Scrapes earning reports from various financial websites
- Parses the reports into a structured format for easy analysis
- Allows for customization of which data points to collect and analyze
- Can be run on a schedule for automated data collection

### Installation
1. Clone the repository
> git clone https://github.com/<your-github-username>/ER_scraper.git
2. Install the dependencies
> pip install -r requirements.txt

### Usage
1. Run the scraper to collect earning reports
> python seleniumPuller.py
2. Run the parser to structure the collected data
> python mainScrape.py

### Roadmap
- Add support for more companies
- Implement natural language procesing to better analyze earning report
- Create user interface
- Add support for exporting data (e.g. CSV, Excel)

### Note
The tool is for educational and research purposes only and should not be used for financial or investment advice. Make sure to comply with the terms of service of any website from which you are scraping data.
