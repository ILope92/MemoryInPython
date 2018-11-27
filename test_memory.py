from pympler import asizeof


class ObjectMemory:
    def __init__(self, obj, show=False):
        self.__memory = 0
        self.__in = True
        self.show = show

    def __counter_size(self, obj):
        size = asizeof.asizeof(obj)
        if self.show is True:
            print(size, 'bytes in:', obj)
        return size

    def memory_null(self):
        self.__memory = 0

    def size_obj(self, obj):
        if self.__in:
            if type(obj) is tuple:
                self.__memory += self.__counter_size(())
                self.__in = False
            elif type(obj) is list:
                self.__memory += self.__counter_size([])
                self.__in = False
            else:
                return self.__counter_size(obj)

        for i in obj:
            if type(i) is tuple:
                self.__memory += self.__counter_size(())
                self.size_obj(i)
            elif type(i) is list:
                self.__memory += self.__counter_size([])
                self.size_obj(i)
            else:
                cnt = self.__counter_size(i)
                self.__memory += cnt

        return self.__memory
