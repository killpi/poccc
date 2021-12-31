def url_agreement_check(url):
    if ('https://' not in url) and ('http://' not in url):
        return 'http://' + url
    return url

def url_backslash_check(url):
    if url[-1] != '/':
        return url + '/'
    return url 