import os
from tkinter import*
from tkinter import filedialog as fd
from tkinter import messagebox as ms

#creating the window

PROGRAM_NAME="FootPrint"
file_name=None

root=Tk()

root.title(PROGRAM_NAME)

root.geometry('600x600')

#adding stuffs for line number

def update_line_numbers(event=None):
	line_numbers=get_line_numbers()
	line_number_bar.config(state='normal')
	line_number_bar.delete('1.0','end')
	line_number_bar.insert('1.0',line_numbers)
	line_number_bar.config(state='disabled')


def highlight_line(interval=100):
	content_text.tag_remove('active_line',1.0,'end')
	content_text.tag_add("active_line","insert linestart","insert lineend+1c")
	content_text.after(interval,toggle_highlight)

def undo_highlight():
	content_text.tag_remove('active_line',1.0,'end')

def toggle_highlight(event=None):
	if to_highlight_line.get():
		highlight_line()
	else:
		undo_highlight()


def on_content_changed(event=None):
	update_line_numbers()
	root.update()

def get_line_numbers(event=None):
	output=''
	if show_line_number.get():
		row,col=content_text.index('end').split('.')
		for i in range(1,int(row)):
			output=output+str(i)+'\n'
	return output

#adding stuffs for about menu
def about():
	about_toplevel=Toplevel(root)
	Label(about_toplevel,text="FootPrint v1.0 a free text editor to edit and create text document",width=50,height=4).grid(row=0,column=0,sticky='e')
	about_toplevel.title('About')
	about_toplevel.transient(root)

def exit_editor(event=None):
	if ms.askokcancel('Quit?','Really Quit?'):
		root.destroy()
def help_function(event=None):
	ms.showinfo('Help','Learn GUI Tkinter application at python.org')
#new_file,open_file,save,save_as implementation

def new_file(event=None):
	root.title("Untitled")
	global file_name
	file_name=None
	content_text.delete(1.0,END)

def open_file(event=None):
	input_file_name=fd.askopenfilename(defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])


	if input_file_name:
		global file_name
		file_name=input_file_name
		root.title('{}-{}'.format(os.path.basename(file_name),PROGRAM_NAME))
		content_text.delete(1.0,END)
		with open(file_name)as _file:
			content_text.insert(1.0,_file.read())

def write_to_file(file_name):
	try:
		content=content_text.get(1.0,'end')
		with open(file_name,'w') as the_file:
			the_file.write(content)
	except IOError:
		pass

def save_as(event=None):

	input_file_name=fd.asksaveasfilename(defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
	if input_file_name:
		global file_name
		file_name=input_file_name
		root.title('{}-{}'.format(os.path.basename(file_name),PROGRAM_NAME))
	return "break"

def save(event=None):
	global file_name
	
	if not file_name:
		save_as()
	else:
		write_to_file(file_name)

	return "break"

#end of iteration
		
#adding text widget built in functionality

def cut():
	content_text.event_generate("<<Cut>>")
	return 'break' 

def copy():
	content_text.event_generate("<<Copy>>")
	return 'break'

def paste():
	content_text.event_generate("<<Paste>>")
	return 'break'
	

def undo(event=None):
	content_text.event_generate("<<Undo>>")
	return 'break'

def redo(event=None):
	content_text.event_generate("<<Redo>>")
	return 'break'

#Implementing select all and find_text function

def select_all(event=None):
	content_text.tag_add('sel','1.0','end')
	return "break"
def find_text(event=None):
	search_toplevel=Toplevel(root)
	search_toplevel.title('Find Text')
	search_toplevel.transient(root)
	search_toplevel.resizable(False,False)
	Label(search_toplevel,text='Find All:').grid(row=0,column=0,sticky='e')
	search_entry_widget=Entry(search_toplevel,width=25)
	search_entry_widget.grid(row=0,column=1,padx=2,pady=2,sticky='we')
	search_entry_widget.focus_set()
	ignore_case_value=IntVar()
	Checkbutton(search_toplevel,text='Ignore Case',variable=ignore_case_value).grid(row=1,column=1,sticky='e',padx=2,pady=2)
	Button(search_toplevel,text='Find All',underline=0,command=lambda:search_output(search_entry_widget.get(),ignore_case_value.get(),content_text,search_toplevel,search_entry_widget)).grid(row=0,column=2,sticky='e'+'w',padx=2,pady=2)	

	def close_search_window():
		content_text.tag_remove('match','1.0',END)
		search_toplevel.destroy()


	search_toplevel.protocol('WM_DELETE_WINDOW',close_search_window)
	return "break"

def search_output(needle,if_ignore_case,content_text,search_toplevel,search_box):
	content_text.tag_remove('match','1.0',END)
	matches_found=0
	if needle:
		start_pos="1.0"
		while True:
			start_pos=content_text.search(needle,start_pos,nocase=if_ignore_case,stopindex=END)

			#this condition checks whether start_pos has any value, if not break
			if not start_pos:
				break
			end_pos='{}+{}c'.format(start_pos,len(needle))
			content_text.tag_add('match',start_pos,end_pos)
			matches_found+=1
			start_pos=end_pos
		content_text.tag_config('match',foreground='red', background='yellow')
	search_box.focus_set()
	search_toplevel.title('{} matches found'.format(matches_found))


#command=new_callback
#command=undo_callback

menu_bar=Menu(root)#menu begins


#all the file menu items will be added here
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',accelerator='Ctrl+n',compound='left',underline=0,command=new_file)
file_menu.add_command(label='Open',accelerator='Ctrl+o',compound='left',underline=0,command=open_file)
file_menu.add_command(label='Save',accelerator='Ctrl+s',compound='left',underline=0,command=save)
file_menu.add_command(label='Save as',accelerator='Shift+Ctrl+s',compound='left',underline=0,command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit',accelerator='Altl+F4',compound='left',command=exit_editor)
menu_bar.add_cascade(label='File',menu=file_menu)#cascading

#all the edit menu items will be added here
edit_menu=Menu(menu_bar,tearoff=0)
edit_menu.add_command(label='Undo',accelerator='Ctrl+z',compound='left',command=undo)
edit_menu.add_command(label='Redo',accelerator='Ctrl+y',compound='left',command=redo)
edit_menu.add_command(label='Cut',accelerator='Ctrl+x',compound='left',command=cut)
edit_menu.add_command(label='Copy',accelerator='Ctrl+c',compound='left',command=copy)
edit_menu.add_command(label='Paste',accelerator='Ctrl+v',compound='left',command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find',accelerator='Ctrl+f',command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select all',accelerator='Ctrl+a',command=select_all)
menu_bar.add_cascade(label='Edit',menu=edit_menu)#cascading


#all the view menu items will be added here
view_menu=Menu(menu_bar,tearoff=0)
show_line_number=IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label='Show Line Number', variable=show_line_number,command=update_line_numbers)
show_cursor_info=IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label="Show cursor location at the Bottom",variable=show_cursor_info)
to_highlight_line=BooleanVar()
view_menu.add_checkbutton(label="Highlight the current line",onvalue=1,offvalue=0,variable=to_highlight_line,command=toggle_highlight)
menu_bar.add_cascade(label='View',menu=view_menu)


#about menu
about_menu=Menu(menu_bar,tearoff=0)
about_menu.add_command(label='Footprint v1.0',command=about)
about_menu.add_command(label='Help',command=help_function)
menu_bar.add_cascade(label='About',menu=about_menu)


#WE HAVE TO CONFIG THIS TO GET THE MENUBAR
root.config(menu=menu_bar)


#adding left line number bar

line_number_bar=Text(root,width=3,padx=3,takefocus=0,border=0,background='#2f3232',foreground="#ffffff",state='disabled',wrap='none')
line_number_bar.pack(side='left',fill='y')

#add the main content text widget and scroll bar

content_text=Text(root,wrap='word',undo=True)
content_text.pack(expand='yes',fill='both')

scrollbar=Scrollbar(content_text)
content_text.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=content_text.yview)
scrollbar.pack(side='right',fill='y')

#event binding
content_text.bind('<Control-z>',undo)
content_text.bind('<Control-y>',redo)
content_text.bind('<Control-a>',select_all)
content_text.bind('<Control-f>',find_text)
content_text.bind('<Control-n>',new_file)
content_text.bind('<Control-o>',open_file)
content_text.bind('<Control-s>',save)
content_text.bind('<Control-Shift-S>',save_as)
content_text.bind('<Alt-F4>',exit_editor)

#highlight line
content_text.bind('<Any-KeyPress>',on_content_changed)
content_text.tag_configure('active_line',background='ivory2')

root.protocol('WM_DELETE_WINDOW',exit_editor)
root.mainloop()