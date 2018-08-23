
def parse_as_header(income_dict):
    """
    простой парсер из первого задания
    :param income_dict: json-объект из файла
    :return: тэги
    """
    return '<h1>{title}</h1><p>{body}</p>'.format(title=income_dict["title"],
                                                  body=income_dict["body"])


def parse_specific(income_dict):
    """
    парсер из задания 2, способный открывать, закрывать тэги
    :param income_dict: json-объект из файла
    :return: тэги
    """
    tags_list = []
    for k, v in dict(income_dict).items():
        if type(v) == type([]):
            tags_list.append('<{0}>{1}</{0}>'.format(k, parse_list(v)))
        else:
            tag_str = '<{0}>{1}</{0}>'.format(k, v)
            tags_list.append(tag_str)
    return "\n".join(tags_list)


def parse_list(income_list):
    """
        парсер из задания 3, способный строить списки
        :param income_list: json-объект из файла
        :return: тэги
        """
    tags_list = []
    tag_str = ''
    for item in income_list:
        tags_list.append('<li>{}</li>'.format(parse_specific(item)))
    tag_str = "\n".join(tags_list)
    tag_str = '<ul>{}</ul>'.format(tag_str)
    return tag_str
