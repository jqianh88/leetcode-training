import string


class ShortenUrl:
    def __init__(self):
        self.url_to_short = {}
        self.short_to_url = {}
        self.counter = 0  # Unique ID counter for URLs
        self.base_url = "https://short.url/"

    def _encode(self, num: int) -> str:
        """Encodes a number into Base62 format."""
        characters = string.ascii_letters + string.digits  # 62 characters
        base62 = []
        while num > 0:
            base62.append(characters[num % 62])
            num //= 62
        return "".join(reversed(base62))

    def _decode(self, short: str) -> int:
        """Decodes a Base62 string into a number."""
        characters = string.ascii_letters + string.digits
        base = len(characters)
        num = 0
        for char in short:
            num = num * base + characters.index(char)
        return num

    def shorten_url(self, url: str) -> str:
        """Shortens a URL and returns the shortened version."""
        if url in self.url_to_short:
            return self.url_to_short[url]

        # Generate a unique ID and encode it
        self.counter += 1
        short_path = self._encode(self.counter)
        short_url = self.base_url + short_path

        # Store mappings
        self.url_to_short[url] = short_url
        self.short_to_url[short_path] = url

        return short_url

    def get_original_url(self, short_url: str) -> str:
        """Retrieves the original URL given a shortened URL."""
        short_path = short_url.replace(self.base_url, "")
        if short_path not in self.short_to_url:
            raise ValueError("Shortened URL not found.")
        return self.short_to_url[short_path]


# Testing
if __name__ == "__main__":
    shortener = ShortenUrl()
    original_url = "https://chatgpt.com"
    shortened = shortener.shorten_url(original_url)
    print(f"Shortened URL: {shortened}")
    restored = shortener.get_original_url(shortened)
    print(f"Restored URL: {restored}")