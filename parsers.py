import re


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
        parse_tag = try_split(k)
        if type(v) == type([]):
            tags_list.append('<{0}>{1}</{2}>'.format(parse_tag[0], parse_list(v), parse_tag[1]))
        else:
            tag_str = '<{0}>{1}</{2}>'.format(parse_tag[0], check_values(v), parse_tag[1])
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
        print(income_list)
        tags_list.append('<li>{}</li>'.format(parse_specific(item)))
    tag_str = "\n".join(tags_list)
    tag_str = '<ul>{}</ul>'.format(tag_str)
    return tag_str


def try_split(tag_type):
    """
    Функция проверяет сожержит ли т.г идентификаторы и классы
    :param tag_type: строка с тэгом
    :return: форматированный тэг
    """
    tag_with_id = re.split("\#", tag_type)
    tag_with_no_id = re.split("\.", tag_type)
    if tag_with_id != [tag_type]:
        id = tag_with_id[-1]
        classes = re.split("\.", tag_with_id[0])
        tag = classes[0]
        return '{} id = \"{}\"class=\"{}\"'.format(tag, id, ".".join(classes[1:])), tag
    elif tag_with_no_id != [tag_type]:
        return '{} class=\"{}\"'.format(tag_with_no_id[0], ".".join(tag_with_no_id[1:])), tag_with_no_id[0]
    else:
        print(tag_type)
        return tag_type, tag_type


def check_values(value_to_check):
    """
    Функция проверяет наличие скобок внутри содержимого тэга
    :param value_to_check: отформатированное значение
    :return:
    """
    if str(value_to_check).__contains__("<") or str(value_to_check).__contains__("<"):
        res_str = str(value_to_check).replace("<", "&lt;")
        res_str = res_str.replace(">", "&gt;")
        return res_str;
    else:
        return value_to_check
