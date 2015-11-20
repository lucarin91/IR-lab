import lucene
import sys
from lucene import *

lucene.initVM()
dir_name = "text_index"
index_dir = SimpleFSDirectory(File(dir_name))
analyser = WhitespaceAnalyzer(Version.LUCENE_35)
writer = IndexWriter(index_dir, analyser, True, IndexWriter.MaxFieldLength.UNLIMITED)

for i in sys.stdin:
    doc = Document()
    text_field = Field("text", l.strip(), Field.Store.YES, Field.Index.ANALYZED)
    doc.add(text_field)
    writer_addDocument(doc)
    print "Currently there are {0} in the index..", format(writer.numDoc())

writer.optimize()
write.close()
