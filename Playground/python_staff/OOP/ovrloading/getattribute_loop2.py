class GetA:
    def __getattribute__(self, item):
        self.other  # innfinite loop


if __name__ == "__main__":
    x = GetA()
    x.name
