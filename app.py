import json
import os
import sys
import parsers

from excetptions import ParseException

page_prefix = """
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8" />
                <title>HTML5</title>
                <!--[if IE]>
                    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
                <![endif]-->
                <style>
                    article, aside, details, figcaption, figure, footer,header,
                    hgroup, menu, nav, section { display: block; }
                </style>
            </head>
            <body>
"""

page_suffix = """
    </body>
        </html>
"""


class HTMLContentGenerator:
    def __init__(self, json_content):
        self.__generators = dict()
        self.__json_content = dict(json_content)
        self.__html_content = []

    def add_parser(self, **kwargs):
        """
        Функция добавляет новый парсер в колекцию
        :param kwargs: ключ - ссылка на функцию
        """
        self.__generators.update(kwargs)

    def __publish(self):
        with open('index.html', 'w') as f:
            f.write(page_prefix)
            f.write("\n".join(self.__html_content))
            f.write(page_suffix)

    def publish_html(self):
        """
        Генерирует HTML-документ
        """
        if len(self.__generators) == 0:
            raise ParseException("no parsers defined")
        if self.__json_content.__contains__("body"):
            self.__html_content.append(self.__generators["header_gen"](self.__json_content))
        else:
            self.__html_content.append(self.__generators["specific_gen"](self.__json_content))
        self.__publish()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        path = os.path.abspath(os.curdir) + '/source.json'
    else:
        path = os.path.abspath(os.curdir) + '/' + sys.argv[1]

    try:
        data = json.load((open(path)))
        gen = HTMLContentGenerator(data[0])
        gen.add_parser(header_gen=parsers.parse_as_header, specific_gen=parsers.parse_specific)
        gen.publish_html()

    except FileExistsError as f_err:
        print(f_err.__str__())
    except ParseException as parse_err:
        print(parse_err.what())
