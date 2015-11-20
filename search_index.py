import lucene
import sys
from lucene import *

if __name__ == "__main__":
    lucene.initVM()
    dir_name = "test_index"
    index_dir = SimpleFSDirectory(File(dir_name))
    analyzer = WhitespaceAnalyzer(Version.LUCENE_35)
    searcher = IndexSearcher(index_dir)
    while True:
        print "Insert a query:"
        input_query = sys.stdin.readline().strip()
        query = QueryParser(Version.LUCENE_35, "title",
                            analyzer).parse(input_query)
        MAX = 1000

        hits = searcher.search(query, MAX)
        print u"Found {0} document(s) that matched query '{1}':".format(hits.totalHits, query)
        for hit in hits.scoreDocs:
            doc = searcher.doc(hit.doc)
            print u"score:{0} doc_id:{1} \nTITLE:{2} \nYEAR:{4} \n{3}\n ".format(hit.score, hit.doc,  doc.get("title"), doc.get('synopsis'), doc.get('year'))
