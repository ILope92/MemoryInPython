from pympler import asizeof


def counter_size(obj):
    return asizeof.asizeof(obj)

def obj_memory(tup):
    memory = 0

    flag_tuple = True
    flag_list = True

    if type(tup) is tuple:
        memory += counter_size(())
        print('RETURNS TUPLE:', counter_size(()))
    elif type(tup) is list:
        memory += counter_size([])
        print('RETURNS LIST:', counter_size([]))
        
    for t in tup:
        tt = type(t)
        if tt is not tuple and tt is not list:
            memory += counter_size(t)
            print('COUNT', counter_size(t))
        elif tt is list or tt is tuple:
            if flag_tuple is True and tt is tuple:
                memory += counter_size(())
                print('SEARCH TUPLE:', counter_size(()))
                flag_tuple = False
            elif flag_list is True and tt is list:
                memory += counter_size([])
                print('SEARCH LIST:', counter_size([]))
                flag_list = False
            for num, a in enumerate(t):
                tmp_mem = counter_size(a)
                memory += tmp_mem
                print('INDEX:', num, '\n\tVALUE:', a, '\n\tMEMORY:', tmp_mem)
        
    return memory

def string_plus(name):
    text = 'hello, my friend. My name is ' + name + '.'
    return text

def string_format(name):
    name_format = 'hello, {}.'.format(name)
    return name_format

def count_link():
    # Не оставлять ссылки (счётчик ссылок не равен 0)
    # Предпочтителен Tuple
    a = (100, 9) # 32
    b = [9, 100] # 104

def memory_func():
    a = 3
    b = 5
    return a, b

test = [(), (), 100, 9, [], 9, 100]
#objects = (string_plus('Andrey'), string_format('Andrey'), count_link())
m = 0
for i in test:
    m += counter_size(i)
print(m)
qwe = count_link()
df = 16
mem = obj_memory(memory_func())
print(
    'FUNC MEMORY:', df, '\n'
    'MEMORY OBJ:', mem, '\n'
    'MEMORY ALL:', mem + df
    )