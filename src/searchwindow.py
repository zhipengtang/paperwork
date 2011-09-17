from util import load_uifile

class SearchWindow(object):
    def __init__(self, docsearch):
        self.docsearch = docsearch
        self.wTree = load_uifile("searchwindow.glade")

        self.searchwin = self.wTree.get_object("windowSearch")
        assert(self.searchwin)
        self.suggestionList = self.wTree.get_object("liststoreSuggestions")
        self.matchList = self.wTree.get_object("liststoreMatch")

        self.connect_signals()
        self.searchwin.set_visible(True)

    def update_results(self, objsrc):
        txt = unicode(self.wTree.get_object("entrySearch").get_text())
        print "Search: " + txt

        suggestions = self.docsearch.get_suggestions(txt.split(" "))
        print "Got %d suggestions" % len(suggestions)
        documents = self.docsearch.get_documents(txt.split(" "))
        print "Got %d documents" % len(documents)

        self.suggestionList.clear()
        for suggestion in suggestions:
            self.suggestionList.append([ suggestion ])
        self.matchList.clear()
        for document in documents:
            self.matchList.append([document])

    def apply(self):
        # TODO
        return True

    def connect_signals(self):
        self.searchwin.connect("destroy", lambda x: self.destroy())
        self.wTree.get_object("entrySearch").connect("changed", self.update_results)
        self.wTree.get_object("buttonSearchCancel").connect("clicked", lambda x: self.destroy())
        self.wTree.get_object("buttonSearchOk").connect("clicked", lambda x: self.apply() and self.destroy())

    def destroy(self):
        self.wTree.get_object("windowSearch").destroy()


