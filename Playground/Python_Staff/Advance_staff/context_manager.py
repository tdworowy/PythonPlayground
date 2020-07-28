class TraceBlock:
    def message(self,arg):
        print("Executing",arg)

    def __enter__(self):
        print("Start with block")
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Normal exit \n")
        else:
            print("Exception raised" , exc_type)
            return False


if __name__ == "__main__":

    with TraceBlock() as action:
        action.message("Test 1")
        print("Done")

    with TraceBlock() as action:
        action.message("Test 2")
        raise TypeError
        print("Not Done")