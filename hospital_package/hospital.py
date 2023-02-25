class Hospital:
    docs = []
    pats = []
    transaction = {

    }

    def assign(self, pat_index, doc_index, hour):
        doc = self.docs[doc_index]
        pat = self.pats[pat_index]
        pat.hour = hour
        self.transaction[doc] = pat
