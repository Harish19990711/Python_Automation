import os
from datetime import datetime

def capture_screenshot(driver, name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    driver.save_screenshot(filename)
