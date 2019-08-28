name = []
lon  = []
lat  = []
with open('../raw_data/westermost_rough.txt') as f:
    for line in f.readlines():
        bits = line.split(',')


        def convert_str(string):
            bits1 = string.split('°')
            bits2 = bits1[1].split('\'')

            return float(bits1[0]) + float(bits2[0])/60.

        name.append( bits[0] )
        lat.append( convert_str(bits[1]) )
        lon.append( convert_str(bits[2]) )

with open('../data/westermost_rough.txt', 'w') as f:
    f.write('# Name: Westermost Rough\n')
    f.write('# Source: http://www.kis-orca.eu/media/76975/WestermostRough_LRes.pdf\n')
    f.write('# name, latitude, longitude\n')
    for i in range(len(name)):
        f.write('{0:>5s}, {1:12.6f}, {2:12.6f}\n'.format(name[i], lat[i], lon[i]))
