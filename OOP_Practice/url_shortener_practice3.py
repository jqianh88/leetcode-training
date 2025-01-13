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
    - base_url

Methods
- get_original_url
- shorten_url
- _encode
- _decode
'''

import string


class ShortenUrl:
    def __init__(self):
        self.short_to_original = {}
        self.original_to_short = {}
        self.counter = 0
        self.base_url = "https://short.url/"

    def get_original_url(self, short_url: str) -> str:
        short_path = short_url.replace(self.base_url, "")
        if short_path not in self.short_to_original:
            raise ValueError(f"No url found for {short_path=}")
        return self.short_to_original[short_path]

    def shorten_url(self, url: str) -> str:
        if url in self.original_to_short:
            return self.original_to_short[url]

        self.counter += 1
        short_path = self._encode(self.counter)
        short_url = self.base_url + short_path
        self.short_to_original[short_path] = url
        self.original_to_short[url] = short_url
        return short_url

    def _encode(self, num: int) -> str:
        characters = string.ascii_letters + string.digits
        base62 = []
        while num > 0:
            base62.append(characters[num%62])
            num //= 62
        return "".join(reversed(base62))

    def _decode(self, short_path: str) -> int:
        characters = string.ascii_letters + string.digits
        base = len(characters)
        num = 0
        for char in short_path:
            num = num * base + characters.index(char)
        return num


if __name__ == "__main__":
    url_shortener = ShortenUrl()
    original_url = "https://chatgpt.com"
    short_url = url_shortener.shorten_url(url=original_url)
    print(f"This is the {short_url=} for {original_url=}")
    url_shortener.get_original_url(short_url=short_url)
    print(f"This is the {original_url=} for {short_url=}")



'''
Strengths
Clear Structure: You adhered to the CARM approach, resulting in clean and modular code with good separation of concerns.
Accurate Implementation: The implementation correctly handles encoding, decoding, and bidirectional mapping between the original and shortened URLs.
Debugging Proficiency: You quickly identified and resolved a critical issue with using short_path instead of url as the key in short_to_original.
Time Management: Completing within 19 minutes, including debugging, is well within the interview expectations.
Areas for Improvement
Depth of Testing:

While your testing was functional, ensure you include edge cases:
What happens when the same URL is shortened multiple times?
What happens when you decode an invalid short URL?
Ensure the counter works for large values.
Include performance testing concepts (e.g., simulating billions of URLs).
Custom Short Paths:

Some variations of this problem may include supporting custom aliases (e.g., short.url/customAlias).
This can be added with minimal changes by checking if a short_path is already used in short_to_original before assigning.
Base62 Decoding:

Your _decode method incorrectly uses base = len(short_path) instead of base = len(characters) (Base62 has 62 characters). Fix this for accuracy.
Error Handling:

Explicitly handle edge cases where the input URL or short URL is invalid.
Consider returning None or a clear error message instead of raising a generic ValueError.
Is This Based on Memory?
Your implementation reflects a strong understanding of the problem's requirements and the Base62 encoding process. Memory played a role, but the goal is not to write novel solutions each time—it’s to solve problems efficiently under time constraints. Redoing the problem multiple times solidifies your intuition, which is exactly what practice is for.


'''