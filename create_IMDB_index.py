import lucene
import sys
import os
from lucene import *
from processhtml import *

rootdir = "pages/www.imdb.com/title/"

if __name__ == "__main__":
    lucene.initVM()
    dir_name = "test_index"
    index_dir = SimpleFSDirectory(File(dir_name))

    analyzer = PerFieldAnalyzerWrapper(ClassicAnalyzer(Version.LUCENE_35))
    analyzer.addAnalyzer("synopsis", ClassicAnalyzer(Version.LUCENE_35))
    analyzer.addAnalyzer("title", ClassicAnalyzer(Version.LUCENE_35))
    analyzer.addAnalyzer("year", KeywordAnalyzer(Version.LUCENE_35))

    writer = IndexWriter(index_dir, analyzer, True,
                         IndexWriter.MaxFieldLength.UNLIMITED)

    for subdir, dirs, files in os.walk(rootdir):
        for dir in dirs:
            move = os.path.join(subdir, dir, 'index.html')
            if os.path.isfile(move):
                data = html_to_data(move)
                doc = Document()
                doc.add(
                    Field("title",
                          data['title'],
                          Field.Store.YES,
                          Field.Index.ANALYZED))
                if data['synopsis']:
                    doc.add(Field("synopsis",
                            data['synopsis'],
                            Field.Store.YES,
                            Field.Index.ANALYZED))
                if data['year']:
                    doc.add(Field("year",
                                  data['year'],
                                  Field.Store.YES,
                                  Field.Index.ANALYZED))

                writer.addDocument(doc)
                print "Currently there are {0} documents in the index...".format(writer.numDocs())

    writer.optimize()
    writer.close()
