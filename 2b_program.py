import numpy as np

data = np.asarray([1127, 2456, 3786, 4562, 5579, 6016, 6134, 6351, 7576, 8608, 
                    9379, 9916, 10111, 10335, 11967, 12158, 12721, 14471, 15900,
                    16315, 16419, 17102, 17193, 17460, 19257, 19857, 19963, 20012,
                    20485, 20721, 21422, 22029, 24052, 24335, 25642, 25963, 26446,
                    26842, 27477, 28481, 28926, 29112, 29408, 29548, 30729, 31428,
                    32403, 33125, 33875, 34871, 35312, 35526, 35600, 37641, 37773,
                    41351, 41463, 42016, 42200, 42513, 43590, 43934, 43967, 45357,
                    46305, 46625, 46684, 47477, 48441, 48679, 49659, 49844, 50069,
                    50135, 50197, 52086, 52325, 52368, 53171, 53684, 54501, 55037,
                    55263, 56343, 56739, 57289, 58569, 58640, 59317, 59453, 60596,
                    60598, 62457, 62794, 63816, 64743, 64831, 65010, 65363, 65423])


def get_fingerTable(m, data_len, node_num):
    '''
        m: the number of bit
        node_num: node
    '''
    
    num_m = 2**m
     
    ret = np.array([])

    for i in range(m):
#         print("i: ", i, "; what_to_append: ", node_num + 2**i)
        tmp = int(node_num + 2**i) % num_m
        
        for j in range(data_len):
            if data[j] > tmp:
                ret = np.append(ret, [int(data[j])], axis=0)
                ret = np.int_(ret)
                break
        
        
#         print("ret: ", ret)

    return ret



def get_largest(table, m, key_val):
    
    for i in reversed(range(m)):
        if table[i] < key_val:
            return table[i]
        
    return table[0]



def get_largest_with_failure(table, m, key_val, node_num):
    
    for i in reversed(range(m)):
        if table[i] < key_val and table[i] % 2 == 0:
            return table[i]
        
        
    return node_num




def perform_lookup(table, node_num, m, key_val, data_len):
    
    num_m = 2 ** m
    
    new_key = key_val % num_m
    
    curr_node = node_num
    next_node = table[0]
#     largest_node = table[-1]
    largest_node = get_largest(table, m, key_val)
    
    ret = np.array([node_num])
    i = 0
    while True:
#     for i in range(20):
        print("i: ", i)
        print("new_key: ", new_key, "curr_node: ", curr_node, "next_node: ", next_node)
        if new_key > curr_node and new_key <= next_node:
            
            ret = np.append(ret, [next_node])
            ret = np.int_(ret)
            return ret
        
        else:
            
            ret= np.append(ret, [largest_node])
            
            table = get_fingerTable(m, data_len=data_len, node_num=largest_node)
            
            curr_node = largest_node
            next_node = table[0]
            largest_node = get_largest(table, m, key_val)
            
            print("curr_node: ", curr_node, "; next_node: ", next_node, "; largest_node: ", largest_node)
            
        i+=1
    ret = np.int_(ret)
    return ret




def lookup_with_failure(table, node_num, m, key_val, data_len):
     
    num_m = 2 ** m
    
    new_key = key_val % num_m
    
    curr_node = node_num
    next_node = table[0]
#     largest_node = table[-1]
    largest_node = get_largest(table, m, key_val)
    
    ret = np.array([node_num])
    i = 0
    
    while True:
#     for i in range(20):
        print("i: ", i)
        print("new_key: ", new_key, "curr_node: ", curr_node, "next_node: ", next_node)
        if new_key > curr_node and new_key <= next_node:
            
            ret = np.append(ret, [next_node])
            ret = np.int_(ret)
            return ret
        
        else:
            
            ret= np.append(ret, [largest_node])
            
            table = get_fingerTable(m, data_len=data_len, node_num=largest_node)
            
            curr_node = largest_node
#             next_node = table[0]
            p = 0
    
            while table[p] % 2 == 1:
                if p >= len(table):
                    break
                p += 1
                
            next_node = table[p]
            
            largest_node = get_largest_with_failure(table, m, key_val, curr_node)
            
            print("curr_node: ", curr_node, "; next_node: ", next_node, "; largest_node: ", largest_node)
            
        i+=1
        
    ret = np.int_(ret)
    
    
    return ret


# MAIN


m = 16
data_len = len(data)

key_val = 29200

node_num_given = 49844


finger_table = get_fingerTable(m, data_len, node_num=node_num_given)
print(finger_table)
len_table = len(finger_table)
print(len_table)





result = perform_lookup(finger_table, node_num=node_num_given, m=m, key_val=key_val, data_len=data_len)
print(result)
print("len: ", len(result))



result2 = lookup_with_failure(finger_table, node_num=node_num_given, m=m, key_val=key_val, data_len=data_len)
print(result2)
print("len: ", len(result2))