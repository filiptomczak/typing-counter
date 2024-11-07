class User:

    def set_entry(self, entry_wg):
        self.entry = entry_wg

    def get_text(self):
        return self.entry.get().strip().lower()

    def clear_text(self):
        self.entry.delete(0,'end')



