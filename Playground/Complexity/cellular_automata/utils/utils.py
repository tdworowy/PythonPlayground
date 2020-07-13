class RoundList(list):
    def __getitem__(self, index):
        while index not in range(0, len(self)):
            if index >= len(self):
                index = index - len(self)
            else:
                if index < 0: index = len(self) - (index * -1)
        return list.__getitem__(self, index)
