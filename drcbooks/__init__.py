"""
drcbooks
========

Book handling module.

"""


ISBN_REST_URL = "http://isbndb.com/api/v2/json/{0}/book/{1}"


def get_book_url(isbn):
    return url_format.format(web_key, isbn)


def load_catalog(filename):
    import pickle
    return pickle.load(open(filename, "rb"))


def dump_catalog(filename, catalog_data):
    pickle.dump(catalog_data, open(filename, "wb"))

