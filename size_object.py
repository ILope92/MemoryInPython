from pympler import asizeof


class Memory:
    __slots__ = ('__memory', '__in', '__show')
    def __counter_size(self, obj):
        size = asizeof.asizeof(obj)
        if self.__show is True:
            print(size, 'bytes in:', obj)
        return size

    def memory(self, obj, show=False):
        self.__memory = 0
        self.__in = True
        self.__show = show
        return self.__size_obj(obj)

    def __size_obj(self, obj):
        """Iter obj
        
        Arguments:
            obj {[all]} -- [object memory]
        
        Returns:
            [int] -- [memory in obj]
        """

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
                self.__size_obj(i)
            elif type(i) is list:
                self.__memory += self.__counter_size([])
                self.__size_obj(i)
            else:
                cnt = self.__counter_size(i)
                self.__memory += cnt

        return self.__memory


test_data_1 = (0, 1, [100, 10, 100, (99, 98, 97)], 1000)
m = Memory()

print('Real:', m.memory(test_data_1))
# Real: 440