from lxml import etree


def html_to_data(html_file):
    parser = etree.HTMLParser(remove_comments=True)
    tree = etree.parse(html_file, parser)
    if tree.getroot() is None:
        return None
    res = {'title': None, 'year': None, 'synopsis': None}
    nodes_title = tree.xpath('//meta[@property="og:title"]/@content')
    if nodes_title:
        titleDate = nodes_title[0].split('(')
        res['title'] = titleDate[0]
        if len(titleDate) > 1:
            res['year'] = titleDate[1].split(')')[0]

    nodes_description = tree.xpath('//p[@itemprop="description"]/text()')
    if nodes_description:
        res['synopsis'] = nodes_description[0].strip()

    # nodes_description = tree.xpath('//meta[@name="description"]/@content')
    # if nodes_description:
    #     res['debug'] = nodes_description[0]
    #     sentence = nodes_description[0].split('.')
    #     # print sentence
    #     sentence.pop(0)
    #     sentence.pop(0)
    #     # print sentence
    #     res['description'] = '.'.join(sentence).strip()
    return res
