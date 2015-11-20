import lucene
import sys
from lucene import *

lucene.initVM()
dir_name = "text_index"
index_dir = SimpleFSDirectory(File(dir_name))
analyser = WhitespaceAnalyzer(Version.LUCENE_35)

search = IndexSearch(index_dir)

print "Insert query"
input_query = sys.a....
