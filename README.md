# Scrapefy

Scrapefy is an AI-powered web scraper that allows users to extract, clean easily, and parse website content. With a simple and interactive interface built on Streamlit, Scrapefy enables users to scrape data from any website and utilize AI to extract specific information based on custom instructions. The tool leverages Selenium for web scraping, BeautifulSoup for HTML parsing, and a language model (Ollama) to process and return relevant data.

## Features

- **Web Scraping**: Uses Selenium to automate the fetching and scraping of website data.
- **HTML Parsing**: Extracts and cleans body content using BeautifulSoup.
- **AI Parsing**: Employs a large language model (Ollama) to intelligently parse content based on user-defined instructions.
- **Streamlit Interface**: Simple, user-friendly UI for entering URLs and viewing results.
- **Flexible Content Parsing**: Split large DOM content into smaller chunks for precise, efficient AI analysis.

## Technologies Used

- **Python**
- **Streamlit**
- **Selenium**
- **BeautifulSoup**
- **Langchain**
- **Ollama LLM**

## Installation

To run Scrapefy locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/scrapefy.git 
   cd scrapefy
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
3. Install the required dependencies:
   ```bash
   pip install -r req.txt
4. Download and configure ChromeDrive:
   ```bash
   # Place the ChromeDriver in the project directory or update the path
   chrome_driver_path = "./chromedriver"
5. Run the Streamlit App:
   ```bash
   streamlit run app.py
