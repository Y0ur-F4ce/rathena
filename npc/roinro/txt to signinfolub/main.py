# Define input and output file names
input_file = "input.txt"
output_file = "newvalues.txt"

# Define the constant string to append
extra_data = '0, IT_BMP, "À¯ÀúÀÎÅÍÆäÀÌ½º\\\\information\\\\over_healer.bmp"'

# Read and process input lines
with open(input_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

formatted_lines = []
for line in lines:
    # Split the line at tab and then take the first part
    parts = line.strip().split('\t')[0]
    # Now split that part by comma and take first 3 values
    coords = parts.split(',')[:3]
    if len(coords) == 3:
        mapname, x, y = coords
        formatted_line = f'{{ "{mapname}", {x}, {y}, {extra_data} }},\n'
        formatted_lines.append(formatted_line)

# Write to output file
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.writelines(formatted_lines)

print("Conversion complete. Check newvalues.txt for results.")
