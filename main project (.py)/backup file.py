from tkinter import* 
from tkinter import ttk
conversion_can_do=('png','gif','tiff','ico','jpg','bmp')
from tkinter import filedialog
from PIL import Image
import os
root=Tk()
opend_file_path=Label(root,text=None)
saved_file_path=Label(root,text=None)
root.maxsize(400,200)
root.minsize(400,200)
Slect_FILE_FROM_DONW_BELOW_OPTIOn=Label(root,text='Select A Fromat To Import From Down Below Than Select File Type To Save')
Slect_FILE_FROM_DONW_BELOW_OPTIOn.pack()
def tkinter_window_is_cloase():
    from tkinter import messagebox
    question=messagebox.askquestion('?','Are You Sure Quit?')
    if question=='yes':
       root.destroy()
    if question=='no':
        None
root.protocol('WM_DELETE_WINDOW',tkinter_window_is_cloase)
root.title('Image Converter')
root.geometry('400x210')
def pngconversion():
    import tkinter.messagebox
    import tkinter
    from PIL import Image
    import os
    from tkinter import filedialog
    filename_1=filedialog.asksaveasfile()
    rela_file_name=filename_1
    name=os.path.basename(str(rela_file_name))
    print(name)
    print(rela_file_name)
    if filename==None:
        import tkinter.messagebox
        tkinter.messagebox.showinfo('info','Please Import A File Than Convert!')
    if filename!=None:
        image=Image.open(f'{filename.name}') 
        image__=image.save(f'{str(filename_1.name)}.png')
        from tkinter import messagebox
        messagebox.showinfo('(:',f' File Succesfully Converted! (Saved At)--{filename_1.name}.png')
        import time
        time.sleep(0.50)
        os.startfile(f'{str(filename_1.name)}.png')
        value_1=conversion_text.get()
        saved_file_path.config(text=f'''Saved File Path- {filename_1.name}.{value_1}''')
        saved_file_path.place(x=1,y=125),'⟶''' 
def icoconversion():
    import tkinter
    from PIL import Image
    import os
    from tkinter import filedialog
    filename_1=filedialog.asksaveasfile()
    rela_file_name=filename_1
    name=os.path.basename(str(rela_file_name))
    print(name)
    print(rela_file_name)
    if filename==None and filename_1:
        tkinter.messagebox.showinfo('info','Please Import A File Than Convert!')
    if filename!=None and filename_1:
        image=Image.open(f'''{str(filename.name)}''')
        rgba_=image.convert('RGBA')
        image__=rgba_.save(f'{str(filename_1.name)}.ico')
        from tkinter import messagebox
        messagebox.showinfo('(:',f'File Succesfully Converted! (Saved At)--{filename_1.name}.ico')   
        import time
        time.sleep(0.50)
        os.startfile(f'{str(filename_1.name)}.ico')
        value_1=conversion_text.get()
        saved_file_path.config(text=f'''Saved File Path- {filename_1.name}.{value_1}''')
        saved_file_path.place(x=1,y=125),'⟶''' 
def gifconversion():
    import tkinter
    from PIL import Image
    import os
    from tkinter import filedialog
    filename_1=filedialog.asksaveasfile()
    rela_file_name=filename_1
    name=os.path.basename(str(rela_file_name))
    print(name)
    print(rela_file_name)
    if filename==None:
        tkinter.messagebox.showinfo('info','Please Import A File Than Convert!')
    if filename!=None:
        image=Image.open(f'''{str(filename.name)}''')
        image__=image.save(f'{str(filename_1.name)}.gif')
        from tkinter import messagebox
        messagebox.showinfo('(:',f'File Succesfully Converted! (Saved At)--{filename_1.name}.gif')   
        import time
        time.sleep(0.50)
        os.startfile(f'{str(filename_1.name)}.gif')
        value_1=conversion_text.get()
        saved_file_path.config(text=f'''Saved File Path- {filename_1.name}.{value_1}''')
        saved_file_path.place(x=1,y=125),'⟶''' 
def tiffconversion():
    import tkinter
    from PIL import Image
    import os
    from tkinter import filedialog
    filename_1=filedialog.asksaveasfile()
    rela_file_name=filename_1
    name=os.path.basename(str(rela_file_name))
    print(name)
    print(rela_file_name)
    if filename==None:
        tkinter.messagebox.showinfo('info','Please Import A File Than Convert!')
    if filename!=None:
        image=Image.open(f'{filename.name}').convert('RGB')
        image__=image.save(f'{str(filename_1.name)}.tiff',format='TIFF', compression='tiff_lzw')
        from tkinter import messagebox
        messagebox.showinfo('(:',f'File Succesfully Converted! (Saved At)--{filename_1.name}.tiff')   
        import time
        time.sleep(0.50)
        os.startfile(f'{str(filename_1.name)}.tiff')
        value_1=conversion_text.get()
        saved_file_path.config(text=f'''Saved File Path- {filename_1.name}.{value_1}''')
        saved_file_path.place(x=1,y=125),'''⟶''' 
def jpgconversion():
    from PIL import Image
    import os
    from tkinter import filedialog
    filename_1=filedialog.asksaveasfile()
    rela_file_name=filename_1
    name=os.path.basename(str(rela_file_name))
    print(name)
    print(rela_file_name)
    if filename==None:
        tkinter.messagebox.showinfo('info','Please Import A File Than Convert!')
    if filename!=None:
        image=Image.open(f'{filename.name}')
        jpg_to_png=image.convert('RGB')
        jpg_to_png.save(f'{str(filename_1.name)}.jpg')
        from tkinter import messagebox
        messagebox.showinfo('(:',f'File Succesfully Converted! (Saved At)--{filename_1.name}.jpg')   
        import time
        time.sleep(0.50)
        value_1=conversion_text.get()
        os.startfile(f'{str(filename_1.name)}.jpg')
        saved_file_path.config(text=f'''Saved File Path- {filename_1.name}.{value_1}''')
        saved_file_path.place(x=1,y=125),'''⟶''' 
def bmpconversion():
    from PIL import Image
    import os
    value_1=conversion_text.get()
    from tkinter import filedialog
    filename_1=filedialog.asksaveasfile()
    rela_file_name=filename_1
    name=os.path.basename(str(rela_file_name))
    print(name)
    print(rela_file_name)
    print(rela_file_name)
    if filename==None:
        tkinter.messagebox.showinfo('info','Please Import A File Than Convert!')
        saved_file_path.config(text=None)
    if filename!=None:
        image=Image.open(f'''{str(filename.name)}''')
        image__=image.save(f'{str(filename_1.name)}.bmp')
        from tkinter import messagebox
        messagebox.showinfo('(:',f'File Succesfully Converted! (Saved At)--{filename_1.name}.bmp')   
        import time
        time.sleep(0.50)
        os.startfile(f'{str(filename_1.name)}.bmp')
        saved_file_path.config(text=f'''Saved File Path- {filename_1.name}.{value_1}''')
        saved_file_path.place(x=1,y=125),'''⟶''' 
def png_to_all_aviable_formats():
    from tkinter import filedialog 
    global filename
    try:
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=100)
    except Exception:
        opend_file_path.config(text=None)
    filename=filedialog.askopenfile(filetypes=(("png file","*.png"),("png file","*.png")))
    if filename == None:
        import tkinter.messagebox
        tkinter.messagebox.showwarning('info','Please Import A File!! Aotherwise File Will Not Convert!')
        opend_file_path.config(text='')
        save_as_combox['state']='Disabled'
        save_as_combox['state']='readonly'
    if filename !=None:
        save_as_combox['state']='normal'
        save_as_combox['state']='readonly'
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=100)

    print(len(str(filename)))
def ico_to_all_aviable_formats():
    from tkinter import filedialog 
    global filename
    filename=filedialog.askopenfile(filetypes=(("ico file","*.ico"),("ico file","*.ico")))
    try:
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=100)
    except Exception:
        opend_file_path.config(text='')
    if filename == None:
        opend_file_path.config(text='')
        import tkinter.messagebox
        tkinter.messagebox.showwarning('info','Please Import A File!! Aotherwise File Will Not Convert!')
        save_as_combox['state']='Disabled'
        save_as_combox['state']='readonly'
    if filename !=None:
        save_as_combox['state']='normal'
        save_as_combox['state']='readonly'
def gif_to_all_aviable_formats():
    from tkinter import filedialog 
    global filename
    filename=filedialog.askopenfile(filetypes=(("gif file","*.gif"),("gif file","*.gif")))
    try:
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=100)
    except Exception:
        opend_file_path.config(text='')
    if filename == None:
        opend_file_path.config(text='')

        import tkinter.messagebox
        tkinter.messagebox.showwarning('info','Please Import A File!! Aotherwise File Will Not Convert!')
        save_as_combox['state']='Disabled'
        save_as_combox['state']='readonly'
    if filename !=None:
        save_as_combox['state']='normal'
        save_as_combox['state']='readonly'
def tiff_to_all_aviable_formats():
    from tkinter import filedialog
    global filename
    filename=filedialog.askopenfile(filetypes=(("tiff file","*.tiff"),("tiff file","*.tiff")))
    try:
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=100)
    except Exception as e:
        opend_file_path.config(text='')
    if filename == None:
        opend_file_path.config(text='')
        import tkinter.messagebox
        tkinter.messagebox.showwarning('info','Please Import A File!! Aotherwise File Will Not Convert!')
        save_as_combox['state']='Disabled'
        save_as_combox['state']='readonly'
    if filename !=None:
        save_as_combox['state']='normal'
        save_as_combox['state']='readonly'
def jpg_to_all_aviable_formats():
    from tkinter import filedialog 
    global filename
    filename=filedialog.askopenfile(filetypes=(("jpg file","*.jpg"),("jpg file","*.jpg")))
    try:
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=100)
    except Exception:
        opend_file_path.config(text='')
    if filename== None:
        opend_file_path.config(text='')
        import tkinter.messagebox
        tkinter.messagebox.showwarning('info','Please Import A File!! Otherwise Your File Will Not Convert!')
        save_as_combox['state']='Disabled'
        save_as_combox['state']='readonly'
    if filename !=None:
        save_as_combox['state']='normal'
        save_as_combox['state']='readonly'
def bmp_to_all_aviable_formats():
    
    from tkinter import filedialog 
    global filename
    filename=filedialog.askopenfile(filetypes=(("bmp file","*.bmp"),("bmp file","*.bmp")))
    try:
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=100)
    except Exception:
        opend_file_path.config(text='')
    if filename == None:
        opend_file_path.config(text='')
        import tkinter.messagebox
        tkinter.messagebox.showwarning('info','Please Import A File!! Otherwise Your File Will Not Convert!')
        save_as_combox['state']='Disabled'
        save_as_combox['state']='readonly'
    if filename !=None:
        save_as_combox['state']='normal'
        save_as_combox['state']='readonly'
def value_of_chekbox_(slef):
    value=conversion_text.get()
    print(value)
    if value=='':
        save_as_button.config(state=DISABLED)
    if value=='png':
        save_as_button.config(state=NORMAL)
        save_as_button.config(command=pngconversion)
    if value=='ico':
        save_as_button.config(state=NORMAL)
        save_as_button.config(command=icoconversion)
    if value=='gif':
        save_as_button.config(state=NORMAL)
        save_as_button.config(command=gifconversion)
    if value=='tiff':
        save_as_button.config(state=NORMAL)
        save_as_button.config(command=tiffconversion)
    if value=='jpg':
        save_as_button.config(state=NORMAL)
        save_as_button.config(command=jpgconversion)
    if value=='bmp':
        save_as_button.config(state=NORMAL)
        save_as_button.config(command=bmpconversion)
def value_of_chekbox(self):
    slection_chekbox_value=text.get()
    print(slection_chekbox_value)
    if slection_chekbox_value=='png':
        import_button.config(state=NORMAL)
        import_button.config(command=png_to_all_aviable_formats)
        import_button.config(text='Import A Png Type File')
        png_to_all_aviable_formats()
    if slection_chekbox_value=='ico':#
        import_button.config(state=NORMAL) 
        import_button.config(command=ico_to_all_aviable_formats) 
        import_button.config(text='Import A Icon Type File')
        ico_to_all_aviable_formats()
    if slection_chekbox_value=='gif':
        import_button.config(state=NORMAL)
        import_button.config(command=gif_to_all_aviable_formats)
        import_button.config(text='Import A Gif Type File')
        gif_to_all_aviable_formats()
    if slection_chekbox_value=='tiff':
        import_button.config(state=NORMAL)
        import_button.config(command=tiff_to_all_aviable_formats)
        import_button.config(text='Import A Tiff Type File')
        tiff_to_all_aviable_formats()
    if slection_chekbox_value=='jpg':
        import_button.config(state=NORMAL)
        import_button.config(command=jpg_to_all_aviable_formats)
        import_button.config(text='Import A jpg Type File')
        jpg_to_all_aviable_formats()
    if slection_chekbox_value=='bmp':
        import_button.config(state=NORMAL)
        import_button.config(command=bmp_to_all_aviable_formats)
        import_button.config(text='Import A Bmp Type File')
        bmp_to_all_aviable_formats()
to_label=ttk.Label(root,text='Convert To',font=(2))
to_label.place(x=155,y=35)
text=StringVar()
conversion_text=StringVar()
show_formats=ttk.Combobox(root,text=text)
show_formats['values']=conversion_can_do
show_formats['state']='readonly'
show_formats.bind('<<ComboboxSelected>>',value_of_chekbox)
show_formats.place(x=1,y=35)
save_as_combox=ttk.Combobox(root,text=conversion_text)
save_as_combox.place(y=35,x=250)
save_as_combox['state']='readonly'
save_as_combox['state']='disabled'
save_as_combox['values']=conversion_can_do
save_as_combox.bind('<<ComboboxSelected>>',value_of_chekbox_)
import_button=Button(root,text='Import A Image File',state=DISABLED)
import_button.place(x=1,y=65)
save_as_button=Button(root,text='Save As',state=DISABLED)
save_as_button.place(x=275,y=65)
root.mainloop()
