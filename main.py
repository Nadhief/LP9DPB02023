from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image
import requests
import io
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3))
hunians.append(Rumah("Sekar MK", 5, 2))
hunians.append(Indekos("Bp. Romi", "Cahya"))
hunians.append(Rumah("Satria", 1, 4))

root = Tk()
root.title("Praktikum DPBO Python")
photo_images = []

def detail(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    image_url = "https://s.kaskus.id/r540x540/images/2020/08/19/10718126_202008190718400168.jpg"
    response = requests.get(image_url)
    image = response.content
    img = Image.open(io.BytesIO(image))
    img = img.resize((250, 250))
    photo_img = ImageTk.PhotoImage(img)
    photo_images.append(photo_img)
    rumahLanding = Frame(top, padx=5, pady=5)
    rumahLanding.pack(padx=5, pady=5)
    img_detail = Label(rumahLanding, image=photo_img)
    img_detail.pack()

    Label(d_frame, text="Summary: " +"\n" +hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")

def listResiden(): 
    label.destroy()
    button.destroy()
    
    label2 = Label(root, text="List Residen", font=('Arial', 16))
    label2.pack()
    rumahLanding.destroy()
    label_img_landing.destroy()
    
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Detail ", command=lambda index=index: detail(index))
        b_detail.grid(row=index, column=3)
            
# label nya
label = Label(root, text="Landing Page Gan", font=('Arial', 16))
label.pack()

# # URL of the image

# # Open the image from the response content
# image = Image.open(BytesIO(response.content))

# # Display the image
# image.show()

image_url = "https://s.kaskus.id/r540x540/images/2020/08/19/10718126_202008190718400168.jpg"
response = requests.get(image_url)
image = response.content
img = Image.open(io.BytesIO(image))
img = img.resize((250, 250))
photo_img = ImageTk.PhotoImage(img)
photo_images.append(photo_img)
rumahLanding = Frame(root, padx=5, pady=5)
rumahLanding.pack(padx=5, pady=5)
label_img_landing = Label(rumahLanding, image=photo_img)
label_img_landing.pack()

# button ke halaman list residen
button = Button(root, text='DAFTAR RESIDEN', font=('Arial', 16), command=listResiden)
button.pack(side=RIGHT)


root.mainloop()
