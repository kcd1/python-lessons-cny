nw_quadrant = []
ne_quadrant = []
se_quadrant = []
sw_quadrant = []

address1 = raw_input('Enter the first address. ')
address1 = address1.lower()
address1_as_list = address1.split(' ')
if 'nw' in address1_as_list:
    nw_quadrant.append(address1)
elif 'ne' in address1_as_list:
    ne_quadrant.append(address1)
elif 'se' in address1_as_list:
    se_quadrant.append(address1)
elif 'sw' in address1_as_list:
    sw_quadrant.append(address1)
else:
    'Could not place address1 into a quadrant list.'

address2 = raw_input('Enter the second address. ')
address2 = address2.lower()
address2_as_list = address2.split(' ')
if 'nw' in address2_as_list:
    nw_quadrant.append(address1)
elif 'ne' in address2_as_list:
    ne_quadrant.append(address2)
elif 'se' in address2_as_list:
    se_quadrant.append(address2)
elif 'sw' in address2_as_list:
    sw_quadrant.append(address2)
else:
    'Could not place address2 into a quadrant list.'

###########
print "Number of addresses in NW quadrant: {0}".format(len(nw_quadrant))
print nw_quadrant

print len(ne_quadrant)
print ne_quadrant

print len(se_quadrant)
print se_quadrant

print len(sw_quadrant)
print sw_quadrant
