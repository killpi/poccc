def open_url(path):
    target_list = []
    with open(path,'r')as f:
        for url in f.readlines():
            target_list.append(url.strip())

    return target_list
