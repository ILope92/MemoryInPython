from pympler import asizeof

class Memory:
    def counter_size(self, obj):
        return asizeof.asizeof(obj)

    def obj_memory(self, tup):
        memory = 0

        flag_tuple = True
        flag_list = True

        if type(tup) is tuple:
            memory += self.counter_size(())
            print('RETURNS TUPLE:', self.counter_size(()))
        elif type(tup) is list:
            memory += self.counter_size([])
            print('RETURNS LIST:', self.counter_size([]))
            
        for t in tup:
            tt = type(t)
            if tt is not tuple and tt is not list:
                memory += self.counter_size(t)
                print('COUNT', self.counter_size(t))
            elif tt is list or tt is tuple:
                if flag_tuple is True and tt is tuple:
                    memory += self.counter_size(())
                    print('SEARCH TUPLE:', self.counter_size(()))
                    flag_tuple = False
                elif flag_list is True and tt is list:
                    memory += self.counter_size([])
                    print('SEARCH LIST:', self.counter_size([]))
                    flag_list = False
                for num, a in enumerate(t):
                    tmp_mem = self.counter_size(a)
                    memory += tmp_mem
                    print('INDEX:', num, '\n\tVALUE:', a, '\n\tMEMORY:', tmp_mem)
        
        return memory

# TEST
a = (10, 100000, 999999999999999999, -999999999999, [10, 10, (10, 40)])
m = Memory()
print('REAL MEMORY:', m.obj_memory(a))