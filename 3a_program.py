from random import sample
import numpy as np


sampleData = np.array([[1,2,3],
                       [3,4,7],
                       [5,6,8],
                       [7,8,10]])


########## FORMING INPUTS ############

# Form Inputs
n = np.size(sampleData)

# n: the number of vectors
n = len(sampleData)

# N: dimension
N = len(sampleData[0])

#### For 0 base array ####
n_arr = np.asarray(range(n))
N_arr = np.asarray(range(N))

xx, yy = np.meshgrid(n_arr, N_arr)

xx = xx.flatten()
yy = yy.flatten()

# HERE "PAIRS" IS INPUT KEY
pairs = zip(yy, xx)
pairs = list(pairs)

# VALUE:
values = (sampleData.T).flatten()

inputs = zip(pairs, values)
inputs = list(tuple(inputs))
inputs = np.asarray(inputs, dtype=object)

#################################

correct_ans = np.dot(sampleData[0]+sampleData[1], sampleData[2]+sampleData[3])
print("CORRECT ANSWER: ", correct_ans)


'''
    keys: np.array
    values: np.array

'''
def mapper1(keys, values):

    num = len(keys)
    
    curr_key = ""
    ret = np.empty([1,2])
        
    for i in range(num):
        
        curr_key += str(int(keys[i][1] / 2))
        curr_key += str(keys[i][0])
        
#         print('{0}\t{1}'.format(curr_key, values[i]))
        ret = np.vstack((ret, [curr_key, values[i]]))
    
        curr_key = ""
        
        pass
        
        
    return ret[1:]


'''



'''
def reducer1(mapped_data):
    
    num = len(mapped_data)
    sum_dict = {key: 0 for key in mapped_data[:,0]}

    for i in range(num):
        sum_dict[mapped_data[i][0]] += int(mapped_data[i][1])
    
    return np.asarray(list(sum_dict.keys())), np.asarray(list(sum_dict.values()))
    

'''

'''
def mapper2(keys, values):
    
    num = len(keys)
    new_keys = np.array([])
    

    for i in range(num):
        curr_key = keys[i][1]
        new_keys = np.append(new_keys, curr_key)
        
    return np.asarray(list(zip(new_keys, values)))



'''

'''
def mapper3(keys, values):
    
    num = len(keys)
         
    tmp_dict = {key: np.array([]).astype(int) for key in keys}
  
    for i in range(num):

        tmp_dict[keys[i]] = np.append(tmp_dict[keys[i]], [int(values[i])])
    
   
        pass

    return np.asarray(list(zip(list(tmp_dict.keys()), list(tmp_dict.values()))), dtype=object)

    
'''

'''
def mapper4(keys, values):
    
    
    num = len(keys)
    new_vals = np.array([]).astype(int)
  
    for i in range(num):

        new_vals = np.append(new_vals, [np.prod(values[i])])

    return np.asarray(list(zip(keys, new_vals)))



'''

'''
def mapper5(keys, values):
    
    num = len(keys)

    new_keys = np.array([0]*num)
    
    return np.vstack((new_keys, values)).T


'''

'''
def reducer2(data):
    
    num = len(data)
    sum_dict = {key: 0 for key in data[:,0]}


    for i in range(num):
        sum_dict[data[i][0]] += int(data[i][1])
        

    # return np.hstack((np.asarray(list(sum_dict.keys())), np.asarray(list(sum_dict.values()))))
    # return np.hstack((np.asarray(list(sum_dict.keys())), np.asarray(list(sum_dict.values()))))
    return tuple(np.asarray(list(zip(list(sum_dict.keys()), list(sum_dict.values()))))[0])


    
mapped1 = mapper1(pairs, values)

new_keys, new_vals = reducer1(mapped1)

mapped2 = mapper2(new_keys, new_vals)
mapped3 = mapper3(mapped2[:,0], mapped2[:, 1])
mapped4 = mapper4(mapped3[:,0], mapped3[:, 1])
mapped5 = mapper5(mapped4[:, 0], mapped4[:, 1])

# final_keys, final_vals = reducer2(mapped5)
final_output = reducer2(mapped5)
# print(final_output)

final_ans = final_output[1]
print("FINAL OUTPUT: ", final_output)
print("FINAL ANSWER: ", final_ans)
