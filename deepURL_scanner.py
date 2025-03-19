from urllib.parse import urlparse, urlunparse

reasons = ''
rating = 10
URL = ''


# This is where the deep scan takes place.
def __clean_url__(url):
    # Parse the URL and remove the path
    parsed_url = urlparse(url)
    cleaned_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    return cleaned_url


def __break_down_url__(cleaned_url):
    parsed_url = urlparse(cleaned_url)
    domain_parts = parsed_url.netloc.split('.')

    if len(domain_parts) > 1:
        tld = domain_parts[-1]  # Last part is the TLD
        domain = domain_parts[-2]  # Second to last is the domain name
        subdomain = '.'.join(domain_parts[:-2]) if len(domain_parts) > 2 else None
    else:
        tld = None
        domain = parsed_url.netloc
        subdomain = None
    print()
    return {
        "scheme": parsed_url.scheme,
        "subdomain": subdomain,
        "domain": domain,
        "tld": tld
    }


def __scan_url_breakdown__(ls_breakdown):
    # In here we'll scan scheme, subdomain, domain, tld using the list
    # Then give a rating, if the rating is below 5 we add it to list
    # We'll return the url, rating and reasons

    # Scanning the scheme
    __scan_scheme__(ls_breakdown.get('scheme'))

    # Scanning for TLDs
    __scan_tld__(ls_breakdown.get("tld"))

    # Scanning the domain
    __scan_domain__(ls_breakdown.get('domain'))

    return [URL, rating, reasons]


def __scan_tld__(tld):
    global reasons, rating
    file = open('./List/common_TLDs.txt', 'r')
    tld = '.' + tld
    for _tld in file:
        _tld = _tld.rstrip()
        if _tld == tld:
            file.close()
            return
    file.close()

    reasons += f"\n#The URL's TLD {tld} was not found in the common list of TLD\n"
    if rating > 0:
        rating -= 2


def __scan_domain__(domain):
    global reasons, rating
    file = open('./List/suspicious_domain.txt', 'r')
    for _dmn in file:
        if _dmn.rstrip() == domain:
            if rating > 0:
                rating -= 3

            reasons += (f"\n#The URL's domain has a suspicious keyword! The domain was found "
                        f"in a list of suspicious domains.")
            file.close()
            return
    file.close()


def __scan_scheme__(scheme):
    global reasons, rating

    file1 = open('./List/schemes/unsecure_schemes.txt', 'r')
    for sch in file1:
        sch = sch.rstrip()
        if sch == scheme:
            rating -= 4
            reasons += f"\n#The URL's scheme '{scheme}' was found in the common list of unsecure schemes."
            file1.close()
            return
    file1.close()

    file2 = open('./List/schemes/secure_schemes.txt', 'r')
    for sch in file2:
        sch = sch.rstrip()
        if sch == scheme:
            file2.close()
            return
    file2.close()

    reasons = (f"\n#The URL's scheme '{scheme}' was not found in either unsecure or secure list of schemes."
               f"Therefore it is invalid!\n")
    rating = 0


def start_scanning(_url):
    global URL
    URL = _url
    return __scan_url_breakdown__(__break_down_url__(__clean_url__(_url)))
