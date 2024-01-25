colors = 'blue,red,green'
#splits string into list of strings using comma separator
colors_list = colors.split(',')
print(colors_list)
print(colors_list[2])
print(colors_list[:])
print(colors_list[0:-2])
#joins list of strings using a separator value
colors = ','.join(colors_list)
print(colors)