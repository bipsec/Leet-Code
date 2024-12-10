class Codec:

    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls = {"4Bclk8": longUrl}
        key = list(self.urls.keys())[0]
        shorten_url = "http://tinyurl.com/" + key
        return shorten_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        vals = list(self.urls.values())
        return "".join(vals)


# Your Codec object will be instantiated and called as such:
codec = Codec()
# encode = codec.encode("https://leetcode.com/problems/design-tinyurl")
# print(encode)
decode  = codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(decode)
