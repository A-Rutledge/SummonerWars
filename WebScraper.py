from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize a WebDriver instance
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://www.plaidhatgames.com/accounts/login/?next=/redirect-swo')

# Find the username and password input fields and submit button
username = driver.find_element(By.NAME, 'login')  # Replace with the actual element locator
password = driver.find_element(By.NAME, 'password')  # Replace with the actual element locator
login_button = driver.find_element(By.CLASS_NAME, "primaryAction")  # Replace with the actual element locator

# Input your login credentials
username.send_keys('@@@user_name@@@')
password.send_keys('@@@Password@@@')

# Click the login button
login_button.click()

# List of target URLs
target_urls = ['https://summonerwars.plaidhatgames.com/#H/jbr9NuZxhgZ', 'https://summonerwars.plaidhatgames.com/#H/_jidDdzxIXA', 'https://summonerwars.plaidhatgames.com/#H/CgDkojjkTC-', 'https://summonerwars.plaidhatgames.com/#H/gi2EtelFNn2', 'https://summonerwars.plaidhatgames.com/#H/Asp4EouEB5T', 'https://summonerwars.plaidhatgames.com/#H/hfaMFZM-QWO', 'https://summonerwars.plaidhatgames.com/#H/Z22Z3ZEBvk-', 'https://summonerwars.plaidhatgames.com/#H/mf9JN2SA7fJ', 'https://summonerwars.plaidhatgames.com/#H/fo3LnNNu4K5', 'https://summonerwars.plaidhatgames.com/#H/kzd81J0ress', 'https://summonerwars.plaidhatgames.com/#H/f8Mpf6bSopd', 'https://summonerwars.plaidhatgames.com/#H/pigJX0rGojh', 'https://summonerwars.plaidhatgames.com/#H/TmLDKo0f_oy', 'https://summonerwars.plaidhatgames.com/#H/4XrkGgZC8jg', 'https://summonerwars.plaidhatgames.com/#H/PFfgqySYDBg', 'https://summonerwars.plaidhatgames.com/#H/U9JVZDMFzsU', 'https://summonerwars.plaidhatgames.com/#H/CvThQUzmOhK', 'https://summonerwars.plaidhatgames.com/#H/a0AN2CHz9M_', 'https://summonerwars.plaidhatgames.com/#H/2W8LH7jRpuN', 'https://summonerwars.plaidhatgames.com/#H/R0vajX5ElCl', 'https://summonerwars.plaidhatgames.com/#H/-vCuzmcyE0Z', 'https://summonerwars.plaidhatgames.com/#H/Knkef_jpSzX', 'https://summonerwars.plaidhatgames.com/#H/v5gBjXFpRJN', 'https://summonerwars.plaidhatgames.com/#H/ljVL7moXH4-', 'https://summonerwars.plaidhatgames.com/#H/awfuPgzpuZR', 'https://summonerwars.plaidhatgames.com/#H/3ukFdkkHdSs', 'https://summonerwars.plaidhatgames.com/#H/xli0StDLTJT', 'https://summonerwars.plaidhatgames.com/#H/IhDW4m4d6Hi', 'https://summonerwars.plaidhatgames.com/#H/rZs_6JRqIKk', 'https://summonerwars.plaidhatgames.com/#H/5hoAa6d5BTJ', 'https://summonerwars.plaidhatgames.com/#H/eapP1mRBoaH', 'https://summonerwars.plaidhatgames.com/#H/JWrdTPpsPgq', 'https://summonerwars.plaidhatgames.com/#H/xu60QluAk-F', 'https://summonerwars.plaidhatgames.com/#H/oWAQR-rakA8', 'https://summonerwars.plaidhatgames.com/#H/3JafO7PnNP7', 'https://summonerwars.plaidhatgames.com/#H/gl-ZwbcQdib', 'https://summonerwars.plaidhatgames.com/#H/Bbmbtdl70G7', 'https://summonerwars.plaidhatgames.com/#H/cvnEghI0MhG', 'https://summonerwars.plaidhatgames.com/#H/nWzVkBd7pbL', 'https://summonerwars.plaidhatgames.com/#H/f7UrlFoePfq', 'https://summonerwars.plaidhatgames.com/#H/bsDoXTFKQHt', 'https://summonerwars.plaidhatgames.com/#H/_iHshHFXuxO', 'https://summonerwars.plaidhatgames.com/#H/klgtJ__hJMc', 'https://summonerwars.plaidhatgames.com/#H/tj0AjXTSN4l', 'https://summonerwars.plaidhatgames.com/#H/5GhqA46WfV2', 'https://summonerwars.plaidhatgames.com/#H/KP-Ztx7VQNt', 'https://summonerwars.plaidhatgames.com/#H/8Jx68Q0zgV2', 'https://summonerwars.plaidhatgames.com/#H/6XSmANLCTfb', 'https://summonerwars.plaidhatgames.com/#H/4SPxvhYrrfr', 'https://summonerwars.plaidhatgames.com/#H/ItZoClnMkrB', 'https://summonerwars.plaidhatgames.com/#H/SemgupiHAZF', 'https://summonerwars.plaidhatgames.com/#H/LmuVnr7dmXM', 'https://summonerwars.plaidhatgames.com/#H/OSqjnBt_7Mw', 'https://summonerwars.plaidhatgames.com/#H/nhoyvEj-P4R', 'https://summonerwars.plaidhatgames.com/#H/EnpSexGmmO5', 'https://summonerwars.plaidhatgames.com/#H/lK5mfolxSBE', 'https://summonerwars.plaidhatgames.com/#H/mMTsJCYfkew', 'https://summonerwars.plaidhatgames.com/#H/bA1AeZv4JsL', 'https://summonerwars.plaidhatgames.com/#H/bIREgfVmE0L', 'https://summonerwars.plaidhatgames.com/#H/tIZ2qDx5V-J', 'https://summonerwars.plaidhatgames.com/#H/2_CbRsfMixq', 'https://summonerwars.plaidhatgames.com/#H/P7C-56GC5lY', 'https://summonerwars.plaidhatgames.com/#H/nERLcbzNHgx', 'https://summonerwars.plaidhatgames.com/#H/CWN_AeLKeKZ', 'https://summonerwars.plaidhatgames.com/#H/CgBEIgOSeAK', 'https://summonerwars.plaidhatgames.com/#H/rBP6Sqi43r-', 'https://summonerwars.plaidhatgames.com/#H/QPKNYPvudw3', 'https://summonerwars.plaidhatgames.com/#H/XoHP3oYXgum', 'https://summonerwars.plaidhatgames.com/#H/F92PZCqvHrr', 'https://summonerwars.plaidhatgames.com/#H/c9jUiabAhYS', 'https://summonerwars.plaidhatgames.com/#H/WpThbJS2TlS', 'https://summonerwars.plaidhatgames.com/#H/_TcNf8jbKu3', 'https://summonerwars.plaidhatgames.com/#H/QEA8xX0A50u', 'https://summonerwars.plaidhatgames.com/#H/ltdX74fkvyu', 'https://summonerwars.plaidhatgames.com/#H/oVTowoggZoG', 'https://summonerwars.plaidhatgames.com/#H/okVZ2pqrXzB', 'https://summonerwars.plaidhatgames.com/#H/K5joCwvD-EV', 'https://summonerwars.plaidhatgames.com/#H/q_qwFi0SNUw', 'https://summonerwars.plaidhatgames.com/#H/MV9ni8Ps9Tb', 'https://summonerwars.plaidhatgames.com/#H/dt6_VnT-CFK', 'https://summonerwars.plaidhatgames.com/#H/U0z0UF5AFWi', 'https://summonerwars.plaidhatgames.com/#H/92QSbzaIYAb', 'https://summonerwars.plaidhatgames.com/#H/tMb0Y04KfFS', 'https://summonerwars.plaidhatgames.com/#H/LlpaKwITIlt', 'https://summonerwars.plaidhatgames.com/#H/EV3JiqyadHy', 'https://summonerwars.plaidhatgames.com/#H/Vs9LcykEVMc', 'https://summonerwars.plaidhatgames.com/#H/7cH8J8mp4PA', 'https://summonerwars.plaidhatgames.com/#H/LA99EIUtiJk', 'https://summonerwars.plaidhatgames.com/#H/PCL_nBZQdep', 'https://summonerwars.plaidhatgames.com/#H/g9BmA35A6UT', 'https://summonerwars.plaidhatgames.com/#H/qdQ86PxsTAC', 'https://summonerwars.plaidhatgames.com/#H/rHUd0Xhh4WO', 'https://summonerwars.plaidhatgames.com/#H/ahFFEHAz6KT', 'https://summonerwars.plaidhatgames.com/#H/Tl8kOPnmb-g', 'https://summonerwars.plaidhatgames.com/#H/96fCDaql_Z3', 'https://summonerwars.plaidhatgames.com/#H/3R2KH_PCVFM']

for target_url in target_urls:
    # Open a new tab
    driver.execute_script("window.open('', '_blank');")

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])

    # Navigate to the target URL in the new tab
    driver.get(target_url)

    try:
        # Wait for the specific element to load. You can customize this selector.
        time.sleep(10)
        
        # Extract player names using find_element
        player1_name = driver.find_element(By.CLASS_NAME, 'user-framed-name.framed-nonbot').text
        player2_name = driver.find_elements(By.CLASS_NAME, 'user-framed-name.framed-nonbot')[1].text

        # Find the log container by class name
        log_container = driver.find_element(By.CLASS_NAME, 'full-log')

        # Find all <div> elements within the log container
        all_log_entries = log_container.find_elements(By.TAG_NAME, 'div')

        # Filter log entries by class name
        log_entries = [entry for entry in all_log_entries if 'full-log-entry' in entry.get_attribute('class')]

        log_texts = [entry.find_element(By.TAG_NAME, 'span').text for entry in log_entries]

        # Convert the game log entries to CSV format
        csv_content = '\n'.join(log_texts)

        # Generate a unique file name with player names and a timestamp
        file_name = f'{player1_name}_v_{player2_name}.csv'

        # Save the CSV content to the unique file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(csv_content)


    finally:
        # Close the current tab
        driver.close()

    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
