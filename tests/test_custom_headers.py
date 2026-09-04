import unittest

from jellyfin_mpv_shim.clients import parse_custom_headers


class CustomHeadersTest(unittest.TestCase):
    def test_parse_json_headers(self):
        parsed = parse_custom_headers('{"X-Test": "abc", "X-Other": "123"}')
        self.assertEqual(parsed, {"X-Test": "abc", "X-Other": "123"})

    def test_parse_line_headers(self):
        parsed = parse_custom_headers("X-Test: abc\nX-Other: 123")
        self.assertEqual(parsed, {"X-Test": "abc", "X-Other": "123"})

    def test_parse_empty_headers(self):
        self.assertEqual(parse_custom_headers(""), {})
        self.assertEqual(parse_custom_headers(None), {})


if __name__ == "__main__":
    unittest.main()
