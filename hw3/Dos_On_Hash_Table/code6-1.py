file = open("input6-1.txt", 'w')
totle_number = 50000

bucket_list = [11, 23, 47, 97, 199, 409, 823, 1741, 3739, 7517, 15173, 30727, 62233]
bucket_index = 0
file.write('%d\n' %totle_number)

index = 1
for number in range(1, totle_number):
    print number
    bucket_size = bucket_list[bucket_index]
    file.write('%d\n' %(index * bucket_size))
    index = index + 1
    if number == bucket_size:
        bucket_index = bucket_index + 1
        index = 1
file.close()