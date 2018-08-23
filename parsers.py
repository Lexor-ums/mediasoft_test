def parse_as_header(income_dict):
    return '<h1>{title}</h1><p>{body}</p>'.format(title=income_dict["title"],
                                                  body=income_dict["body"])
