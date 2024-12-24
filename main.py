from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse
import datetime


def get_screenshot(url: str) -> None:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--start-fullscreen")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.NAME, "q")))

        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        parse = urlparse(url)
        fname = f"./result/{parse.netloc}_{now}.png"
        driver.save_screenshot(fname)
        print(f"{url} のスクリーンショットを取得しました")

    except TimeoutException as e:
        print(f"タイムアウトしました: {e}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

    finally:
        driver.quit()


def main():
    urls = [
        "https://www.google.com",
        "https://www.yahoo.co.jp",
        "https://www.bing.com",
    ]

    for url in urls:
        get_screenshot(url)


if __name__ == "__main__":
    main()
