import re
import sys
import time

import scanner
import requests


# Banner
def banner():
    print("""      

 #     # ######  #           #####   #####     #    #     # #     # ####### ######  
 #     # #     # #          #     # #     #   # #   ##    # ##    # #       #     # 
 #     # #     # #          #       #        #   #  # #   # # #   # #       #     # 
 #     # ######  #           #####  #       #     # #  #  # #  #  # #####   ######  
 #     # #   #   #                # #       ####### #   # # #   # # #       #   #   
 #     # #    #  #          #     # #     # #     # #    ## #    ## #       #    #  
  #####  #     # #######     #####   #####  #     # #     # #     # ####### #     #     
######################################################################################                                                                                                                                                                                      
    """)


# This function will confirm if the entered URL is valid (return a boolean)
def isValid_url(url):
    pattern = ("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}"
               "\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$")

    try:
        # Work on the online ping
        if re.match(pattern, url):
            response = requests.head(url)
            if response.status_code != '404':
                return True
    except requests.ConnectionError:
        print('Cannot connect to the url. Try again')
        sys.exit()


# Goes through a list(txt) of blacklisted/Suspicious URLS
# first read the Suspicious_list.txt, then find the match on the list
def blacklisted_urls(url):
    file = open('List/blacklisted_URLS.txt', 'r')
    # Read the list
    for b_url in file:
        b_url = b_url.rstrip()
        if b_url == url:
            print("\nSCAN RESULTS\n", end='=' * 12)
            print(f'\nThis URL "{url}" was found on the blacklist')
            print("\n===== END =====")
            # if the URL is found the rating must be 0. Then program stops.
            file.close()
            sys.exit()

    file.close()


if __name__ == '__main__':
    banner()

    URL = input('Enter a URL/Link: ').strip()
    URL = URL.lower()
    if isValid_url(URL):
        # This method checks for blacklisted URLs
        blacklisted_urls(URL)

        # This module method receives the valid URL
        r = scanner.url_scanner(URL)
        # More methods can be added here.
        print("\nSCAN RESULTS\n", end='=' * 12)
        if 5 <= r[1] < 10:
            print(f"\n#The rating of this URL: {r[0]} is {r[1]}. "
                  f"Therefore browse with CAUTION!{r[2]}")
        elif r[1] == 10:
            # print("SCAN RESULTS\n", end='='*12)
            print(f"\n#The rating of this URL: {r[0]} is {r[1]}. Happy safe browsing!")
        else:
            print(f"\n#The rating of this URL: {r[0]} is {r[1]}. "
                  f"The website might be a SCAM!!{r[2]}")
    else:
        print("SCAN RESULTS\n", end='=' * 12)
        print('\nThe url is not valid! Try again.')

    print("\n===== END =====")
