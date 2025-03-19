import sys
import deepURL_scanner


# This module/method will return the results to user, about what has been found on the url
def url_scanner(url):
    results = deepURL_scanner.start_scanning(url)

    if results[1] < 5:
        # Add the URL to the blacklisted list
        try:
            file = open('List/blacklisted_URLS.txt', 'a')
            file.write(results[0])
            file.write('\n')
            file.close()
            results[2] += f"\n#The URL '{results[0]}' has been added to the blacklist, due to low rating '{results[1]}'."
        except Exception:
            raise Exception('Failed to write the URL to the blacklist file. Try again!')

    return results
