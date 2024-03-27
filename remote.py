from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import reversegeo as loc
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
import time  

def get_current_location():
    options=webdriver.ChromeOptions()
    options.enable_downloads=True
    capabilities={
                "browserName":"chrome",
                "platformName":"windows",
                "deviceName":"guhoij"    
            }

    #Enabling cababilities of a chrome

    display = Display(visible=0,size=(800,600))
    display.start()

    #Grant permission automatically by usng this commet use--fake-ui-for-media-stream byDefault
    options.add_argument("--use--fake-ui-for-media-stream")
    
    #select a webdriver chrome,firebox,etc...
    driver=webdriver.Remote(command_executor='server',options=options,DesiredCapabilities=capabilities) 
    wait=WebDriverWait(driver,timeout=10)

    #web address we want to navigate into 
    driver.get("https://www.maps.ie/coordinates.html")

    time.sleep(5) #wait to till loading page

    driver.find_element("id","find-loc").click()

    time.sleep(5)

    lat=driver.find_element("id","marker-lat")
    lat=driver.find_element("id","marker-lat")
    
    try:
        
        latitude=wait.until(EC.visibility_of_element_located(("id","marker-lat"))).get_attribute("value")
        print("Current latitude : ",latitude)
        
        longitude=wait.until(EC.visibility_of_element_located(("id","marker-lng"))).get_attribute("value")
        print("Current longitude : ",longitude)

        print("Located address :")

        Address=loc.address_details(latitude,longitude)
        return Address

    except Exception as e:

        print(e)

    driver.close()
    display.stop()

print(get_current_location())