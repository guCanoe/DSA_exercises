""" English line """
def draw_line(len):
    if len==1:
        print '-'
    else:
        draw_line(len-1)
        print '-'*len
        draw_line(len-1)
        
def draw_ruler(tick_len, tick_max):
    print 
    print '-'*tick_len + " " + str(0)
    for tick in range(1,tick_max+1):
        draw_line(tick_len-1)
        print '-'*tick_len + " " + str(tick)

draw_ruler(2, 1) 
draw_ruler(3, 1) 
draw_ruler(4, 1) 

