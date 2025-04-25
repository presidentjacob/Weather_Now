from selenium import webdriver
import time

# List of city URLs
city_urls = [
    "http://127.0.0.1:8000/colorado_springs/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/denver/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/winter_park_colorado/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/winter_park_florida/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/alexandria_ontario/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/melbourne_florida/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/melbourne_victoria/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/venice_italy/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/mexico_city/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/seattle/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
    "http://127.0.0.1:8000/alexandria_virginia/?firstname=Jacob&lastname=Yepez&city=Chicago&state=Illinois&country=United%20States",
]

driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument('--headless'))

for url in city_urls:
    driver.get(url)
    time.sleep(2) 

    # Extract the city name from the URL for the screenshot filename
    city_name = url.split("/")[-2]
    screenshot_filename = f"{city_name}.png"

    # Capture the screenshot
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved: {screenshot_filename}")

driver.quit()