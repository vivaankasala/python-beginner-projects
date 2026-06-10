from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)


contact_name = input("Enter the exact WhatsApp contact name: ").strip()
message = input("Enter the message to send: ").strip()

if not contact_name or not message:
    raise ValueError("The contact name and message cannot be empty.")

profile_directory = Path(__file__).resolve().parent / ".chrome-profile"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir={profile_directory}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com")
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "pane-side"))
)

search_box = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[aria-label="Search or start a new chat"]')
    )
)
search_box.send_keys(contact_name)


def click_chat_result(browser):
    try:
        result = browser.find_element(
            By.XPATH,
            f'//*[@id="pane-side"]//*[@title="{contact_name}"]'
        )
        result.click()
        return True
    except ElementClickInterceptedException:
        ActionChains(browser).send_keys(Keys.ESCAPE).perform()
        return False
    except StaleElementReferenceException:
        return False


WebDriverWait(driver, 30).until(click_chat_result)
message_box = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]')
    )
)
message_box.send_keys(message)
send_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            'button[aria-label="Send"], [data-testid="compose-btn-send"]'
        )
    )
)
send_button.click()


def message_has_sent(browser):
    return browser.execute_script(
        """
        const expectedMessage = arguments[0];
        const outgoingMessages = [...document.querySelectorAll('.message-out')];
        const matchingMessage = outgoingMessages
            .reverse()
            .find(element => element.innerText.includes(expectedMessage));

        if (!matchingMessage) {
            return false;
        }

        const statusIcons = [...matchingMessage.querySelectorAll('[data-icon]')]
            .map(element => element.getAttribute('data-icon'));

        return statusIcons.some(icon =>
            icon === 'msg-check' || icon === 'msg-dblcheck'
        );
        """,
        message,
    )


WebDriverWait(driver, 60).until(message_has_sent)
driver.quit()
