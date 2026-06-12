import json
import re
import time


def retrieve_phone_code(driver):

    for _ in range(30):

        logs = driver.get_log("performance")

        for log in logs:

            try:
                message = json.loads(
                    log["message"]
                )["message"]

                body = str(message)

                code_search = re.search(
                    r'(\d{4})',
                    body
                )

                if code_search:
                    return code_search.group(1)

            except Exception:
                pass

        time.sleep(1)

    raise Exception("Phone confirmation code not found")