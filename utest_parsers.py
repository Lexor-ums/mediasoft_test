import parsers
import unittest


class CalcTests(unittest.TestCase):
    def test_parse_as_header(self):
        test_dict = dict(title="Title #1",
                         body="Hello, World 1!")
        res_str = "<h1>Title #1</h1><p>Hello, World 1!</p>"
        self.assertEqual(parsers.parse_as_header(test_dict), res_str)

    def test_parse_specific(self):
        test_dict = dict(h3="Title #1",
                         div="Hello, World 1!")
        res_str = "<h3>Title #1</h3>\n<div>Hello, World 1!</div>"
        self.assertEqual(parsers.parse_specific(test_dict), res_str)

    def test_parse_list(self):
        test_list = [dict(h3="Title #1",
                          div="Hello, World 1!")]
        res_str = "<ul><li><h3>Title #1</h3>\n<div>Hello, World 1!</div></li></ul>"
        self.assertEqual(parsers.parse_list(test_list), res_str)

    def test_try_split_with_class(self):
        test_tag = "p.my-class1.my-class2"
        formatted_tag = "p class=\"my-class1.my-class2\""
        tag_name = "p"
        self.assertEqual(parsers.try_split(test_tag), (formatted_tag, tag_name))

    def test_try_split_with_id(self):
        test_tag = "p.my-class#my-id"
        formatted_tag = "p id=\"my-id\" class=\"my-class\""
        tag_name = "p"
        self.assertEqual(parsers.try_split(test_tag), (formatted_tag, tag_name))

    def test_right_bracket(self):
        test_val = "a > b"
        res = "a &gt; b"
        self.assertEqual(parsers.check_values(test_val), res)

    def test_left_bracket(self):
        test_val = "a < b"
        res = "a &lt; b"
        self.assertEqual(parsers.check_values(test_val), res)

    def test_both_brackets(self):
        test_val = "example<a>asd</a>"
        res = "example&lt;a&gt;asd&lt;/a&gt;"
        self.assertEqual(parsers.check_values(test_val), res)


if __name__ == '__main__':
   unittest.main()