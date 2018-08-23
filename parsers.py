
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
    :param income_dict:
    :return: json-объект из файла
    """
    tags_list = []
    for k, v in dict(income_dict).items():
        tag_str = '<{0}>{1}</{0}>'.format(k, v)
        tags_list.append(tag_str)
    return "\n".join(tags_list)
