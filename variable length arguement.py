# when we use arbitrary arguments or variable length arguements then the the function defination uses astric(*) before parameter name = variable length arguements
def fav_movie(name,*movie_list):
    print(name,movie_list)
fav_movie("jas","lalaland","incidious","newness")
fav_movie("kalra","notebook","yjhd","ddlj")
fav_movie("krish","krrish2","singham")
#the arbitary no of arguements pass  through to the function basically forms a tuple