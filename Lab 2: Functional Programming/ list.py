if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]

    def list_comprehension(list):
        return [list[i] + list[i+1] for i in range(len(list)-1)]

    print(list_comprehension(list))
