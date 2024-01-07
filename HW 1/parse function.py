from urllib.parse import urlparse, parse_qs
def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    return {k: v[0] for k, v in parse_qs(parsed_url.query).items()}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    # Split the query at ';', which separates different key=value pairs
    tokens = query.split(';')

    # Remove any trailing or leading spaces
    tokens = map(str.strip, tokens)

    # Ignore any empty strings in `tokens`
    tokens = filter(bool, tokens)

    # Each token is a 'key=value' string. Split each token into a key and value.
    kv_pairs = map(lambda s: s.split('=', 1), tokens)

    # Pack the key-value pairs into a dictionary and return it
    return dict(kv_pairs)


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
