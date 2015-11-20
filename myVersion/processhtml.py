from lxml import etree


def html_to_data(html_file):
    parser = etree.HTMLParser(remove_comments=True)
    tree = etree.parse(html_file, parser)

    if tree.getroot() is None:
        return Node
    title = None
    nodes_title = tree.xpath('//meta[@property="og:title"]/@content')
    if nodes_title:
        title = nodes_title[0]
    return title
