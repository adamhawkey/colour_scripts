import colour

input_colourspace = colour.RGB_COLOURSPACES['ACES2065-1']
output_colourspace = colour.RGB_COLOURSPACES['sRGB']

out_matrix = colour.RGB_to_RGB_matrix(input_colourspace, output_colourspace, 'BRADFORD')
print(out_matrix)