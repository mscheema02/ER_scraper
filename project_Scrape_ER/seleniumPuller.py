from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary 
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request

class FileDownloader:
    def __init__(self, url):
        self.url = url
        try:
            self.chromeOptions = webdriver.ChromeOptions()
            self.chromeOptions.add_experimental_option("prefs", {"download.default_directory" : "C:\\Projs\\project_Scrape_ER\\DownloadTest"})
            self.driver = webdriver.Chrome(executable_path="C:/Applicationz/chromedriver_win32_version108/chromedriver.exe", options=self.chromeOptions)
            self.driver.maximize_window()
        except Exception as e:
            print("ERROR 1: ", e)
        
    
    def download(self):
        self.driver.get(self.url)

        download_link_element = self.driver.find_element(By.XPATH, "//a[@aria-label='2022 Q3 10-Q PDF']")
        download_link_element.click()

        # Wait for the download to complete
        try:
            download_link_element = self.driver.find_element(By.ID, "download")
            download_link_element.click()
            wait = WebDriverWait(self.driver, 1)
            # wait.until(lambda driver: len(driver.get_log("browser")) > 1)
        # except NoSuchElementException as e:
        #     print("Element not found: ", e)
        # except TimeoutException as e:
        #     print("A timeout occured: ", e)
        except Exception as e:
            print("ERROR 2: ", e)
            self.close()
        finally:
            self.driver.close()

    def close(self):
        self.driver.close()



# Create an instance of the FileDownloader class
downloader = FileDownloader("https://abc.xyz/investor/")

# Download the file
downloader.download()

# Close the web driver
downloader.close()



