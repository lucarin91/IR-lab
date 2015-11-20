import lucene
import sys
from lucene import *

if __name__ == "__main__":
    lucene.initVM()
    dir_name = "test_index"
    index_dir = SimpleFSDirectory(File(dir_name))
    # tAnalyzer = WhitespaceAnalyzer(Version.LUCENE_35)
    classic_analyzer = ClassicAnalyzer(Version.LUCENE_35)
    tParser = QueryParser(Version.LUCENE_35, "title", classic_analyzer)
    sParser = QueryParser(Version.LUCENE_35, "synopsis", classic_analyzer)
    searcher = IndexSearcher(index_dir)
    MAX = 1000

    while True:
        print "Insert a query:"
        title_terms = raw_input("input a title terms:")
        synopsis_terms = raw_input("input a synopsi terms:")
        # input_query = sys.stdin.readline().strip()

        query = BooleanQuery()
        if synopsis_terms:
            synopsis_query = sParser.parse(synopsis_terms)
            query.add(synopsis_query, BooleanClause.Occur.MUST)
        if title_terms:
            title_query = tParser.parse(title_terms)
            query.add(title_query, BooleanClause.Occur.MUST)

        hits = searcher.search(query, MAX)
        print u"Found {0} document(s) that matched query '{1}':".format(hits.totalHits, query)
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            print u"score:{0} doc_id:{1} \nTITLE:{2} \nYEAR:{4} \n{3}\n ".format(hit.score, hit.doc,  doc.get("title"), doc.get('synopsis'), doc.get('year'))
