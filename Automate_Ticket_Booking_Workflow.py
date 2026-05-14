from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # Needed for Dropdown menus
import time

def travel_agency_bot():
    print("🚀 Starting the Travel Agency Auto-Booking Bot...")
    
    # 1. Initialize Browser
    driver = webdriver.Chrome()
    
    try:
        # 2. Go to the client's booking portal
        print("🌐 Navigating to the travel portal...")
        driver.get("https://blazedemo.com/")
        time.sleep(2)
        
        # 3. Select Departure City from Dropdown
        print("🛫 Selecting departure city: 'Paris'")
        departure_dropdown = Select(driver.find_element(By.NAME, "fromPort"))
        departure_dropdown.select_by_value("Paris")
        time.sleep(1)
        
        # 4. Select Destination City from Dropdown
        print("🛬 Selecting destination city: 'Rome'")
        destination_dropdown = Select(driver.find_element(By.NAME, "toPort"))
        destination_dropdown.select_by_value("Rome")
        time.sleep(1)
        
        # 5. Click the 'Find Flights' button
        print("🔍 Searching for available flights...")
        driver.find_element(By.CSS_SELECTOR, "input[value='Find Flights']").click()
        time.sleep(2)
        
        # 6. Choose the first available flight in the table
        print("🎫 Selecting the first available flight...")
        driver.find_element(By.CSS_SELECTOR, "input[value='Choose This Flight']").click()
        time.sleep(2)
        
        # 7. Fill out the customer detail form
        print("📝 Filling out customer information form...")
        driver.find_element(By.ID, "inputName").send_keys("Abbas Raza")
        driver.find_element(By.ID, "address").send_keys("123 Tech Street, Silicon Valley")
        driver.find_element(By.ID, "city").send_keys("Karachi")
        driver.find_element(By.ID, "zipCode").send_keys("75000")
        
        # Selecting Credit Card type from another dropdown
        card_dropdown = Select(driver.find_element(By.ID, "cardType"))
        card_dropdown.select_by_visible_text("American Express")
        time.sleep(2)
        
        # 8. Purchase the flight (Submit the form)
        print("💳 Clicking 'Purchase Flight'...")
        driver.find_element(By.CSS_SELECTOR, "input[value='Purchase Flight']").click()
        time.sleep(3)
        
        # 9. Take screenshot of the success page
        print("📸 Taking screenshot of the booking confirmation...")
        driver.save_screenshot("booking_success.png")
        print("✅ Auto-Booking completed successfully! Client just saved 4 hours.")
        
    finally:
        # 10. Close the browser
        print("🏁 Closing the browser in 3 seconds...")
        time.sleep(3)
        driver.quit()

# Run the automation bot
travel_agency_bot()