def get_short_url(url):
    return url.split('//')[-1].split('www.')[-1].split('/')[0]