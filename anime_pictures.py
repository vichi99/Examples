##############################################################################
# The program do not nothing special, only shows animation pictures
##############################################################################
import tkinter
#init
##########################################
main = tkinter.Tk()
bg = tkinter.PhotoImage(file="data/sprites/background.png") #must be png
canvas = tkinter.Canvas(width=bg.width(), height=bg.height())
canvas.pack()
canvas.create_image(bg.width()/2,bg.height()/2, image = bg)

# make list of sprites
##########################################
sprites = []
braid_id = canvas.create_image(bg.width()/2,bg.height()/2)

#if we have many small pictures
# for i in range(27):
#     img = tkinter.PhotoImage(file="data/sprites/braid_{:02d}.png".format(i))
#     sprites.append(img)

#if we have one picture
def load_sprites(file_path, rows, cols):
    sprite_img = tkinter.PhotoImage(file=file_path)
    height = sprite_img.height()//rows
    width = sprite_img.width()//cols
    for row in range(rows):
        for col in range(cols):
            l = col*width
            t = row*height
            r = (col+1)*width
            b = (row+1)*height
            subimage = create_sub_image(sprite_img, l, t, r, b)
            sprites.append(subimage)
    # return sprites

def create_sub_image(img, left, top, right, bottom):
    subimage = tkinter.PhotoImage()
    subimage.tk.call(subimage, 'copy', img, '-from',
                      left, top, right, bottom, '-to', 0, 0)
    return subimage



#animate
def animate():
    global sprite_idx
    sprite_idx = (sprite_idx + 1) % 27
    canvas.itemconfig(braid_id, image = sprites[sprite_idx])
    canvas.after(50, animate)

sprite_idx=0
load_sprites("data/sprites/braid.png",1,27)
animate()
canvas.mainloop()
