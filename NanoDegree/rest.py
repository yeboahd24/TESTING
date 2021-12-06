import time
import webbrowser
from selenium import webdriver

def scrap_all_my_linkind_connectios_name_and_job_position(driver):
    """
    Scrap all my linkind connections name and job position
    """
    # Click on the "Connections" tab
    driver.find_element_by_xpath("//a[@class='nav-link'][contains(text(),'Connections')]").click()
    time.sleep(2)
    # Click on the "All" tab
    driver.find_element_by_xpath("//a[@class='nav-link'][contains(text(),'All')]").click()
    time.sleep(2)
    # Click on the "View All" button
    driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']").click()
    time.sleep(2)
    # Get all the connections name and job position
    connections_name_and_job_position = driver.find_elements_by_xpath("//div[@class='card-body']")
    return connections_name_and_job_position

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/")
    scrap_all_my_linkind_connectios_name_and_job_position(driver)
    time.sleep(2)
       