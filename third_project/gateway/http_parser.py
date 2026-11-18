import json


def parse_request(raw: bytes) -> dict:
    head, _, body = raw.partition(b'\r\n\r\n')
    start, *lines = head.decode('latin-1').split('\r\n')
    method, path, version = start.split(' ')
    headers: dict[str, str] = {}
    for line in lines:
        name, _, value = line.partition(':')
        headers[name.strip().lower()] = value.strip()
    length = int(headers.get('content-length', 0))
    data = json.loads(body[:length]) if length else None
    return {'method': method, 'path': path, 'version': version, 'headers': headers, 'json': data}


if __name__ == '__main__':
    req = parse_request(b'POST /notify HTTP/1.1\r\nContent-Length: 15\r\n\r\n{"source":"ci"}')
    print(req)
