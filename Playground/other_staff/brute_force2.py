if __name__ == "__main__":
    for i in range(10000, 99999):
        if int(f'{i}1') == 3 * int(f'1{i}'):
            print(i)
            break
