list=[1,2,3,4,5,3,2,1,3,4,6,6,7,9,10,8,2,4,6,8,12]

freq_map=dict() 
# for i in range (0,len(list)):
#         if list[i] in freq_map:
#             freq_map[list[i]] += 1
#         else:
#             freq_map[list[i]] = 1
# print(freq_map)

for i in range(0,len(list)):
    freq_map[list[i]] = freq_map.get(list[i],0) + 1
print(freq_map)