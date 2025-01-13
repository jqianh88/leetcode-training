'''
Problem Statement: Shorten URL
You need to design a service that shortens URLs. The service should:

Encode a given URL into a shortened version.
Decode the shortened URL back to the original URL.
Ensure that shortened URLs are unique and consistent (a given URL should always result in the same shortened URL).
Constraints:

The service should handle billions of URLs.
The shortened URL should be as short as possible.
Optimize for fast encoding/decoding.
Assume no special character constraints in URLs.

Classes
- ShortenUrl
    - short_to_original: {}
    - original_to_short: {}
    - counter = 0
    - base_url = "https://short.url"

- _encode
- _Decode
_ get_original_url
- shorten_url
'''

import string


class ShortenUrl:
    def __init__(self):
        self.short_to_original = {}
        self.original_to_short = {}
        self.counter = 0
        self.base_url = "https://short.url"

    def _encode(self, num: int) -> str:
        characters = string.ascii_letters + string.digits
        base62 = []
        while num > 0:
            base62.append(characters[num%62])
            num //=62
        return "".join(reversed(base62))

    def _decode(self, short: str) -> int:
        characters = string.ascii_letters + string.digits
        num = 0
        base = len(short)
        for char in short:
            num = num * base + characters.index(char)
        return num


    def get_original_url(self, short_url: str) -> str:
        short_path = short_url.replace(self.base_url, "")
        if short_path not in self.short_to_original:
            raise ValueError(f"No url found for {short_path=}")
        return self.short_to_original[short_path]

    def shorten_url(self, original_url: str) -> str:
        if original_url in self.original_to_short:
            return self.original_to_short[original_url]

        self.counter += 1
        shortened = self._encode(self.counter)
        short_url = self.base_url + shortened
        self.original_to_short[original_url] = short_url
        self.short_to_original[short_url] = original_url
        return short_url