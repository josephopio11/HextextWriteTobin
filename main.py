import sys

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'wb')

output_data = bytes()
for line in input_file:
    data = line.split()
    for d in data:
        if len(d) == 1:
            d = '0' + d
        output_data += bytes.fromhex(d)
output_file.write(output_data)