import tkinter as tk
from tkinter import ttk
from tkinter import font, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("Text Editor")

########################## main menu ##########################
main_menu = tk.Menu()

### File ###
# file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)

### Edit ###
# Edit icon #
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)

### View ###
# View icons #
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)

### Color Theme ###
# Color icons #
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0e'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}

# cascade
main_menu.add_cascade(label='file', menu=file)
main_menu.add_cascade(label='edit', menu=edit)
main_menu.add_cascade(label='view', menu=view)
main_menu.add_cascade(label='color theme', menu=color_theme)
# -----------------&&&&&&& end main menu &&&&&------------------


########################## toolbar ##########################

# Label #
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

## Font Box ##
font_tuple = tk.font.families()
#print(font_tuple)
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, state='readonly', textvariable=font_family)
font_box['values'] = font_tuple
font_box.current(font_tuple.index('FontAwesome'))
font_box.grid(row=0, column=0, padx=5)

## Font Sixe Box ##
font_size_tuple = tuple(range(10, 80, 2))
font_size_var = tk.StringVar()
font_size_box = ttk.Combobox(tool_bar, width=15, state='readonly', textvariable=font_size_var)
font_size_box['values'] = font_size_tuple
font_size_box.current(3)
font_size_box.grid(row=0, column=1, padx=5)

## Bold Button ##
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

## Italic Button ##
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## Underline Button ##
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

## Font Button ##
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_btn = ttk.Button(tool_bar, image=font_color_icon)
font_btn.grid(row=0, column=5, padx=5)

## Align Left ##
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## Align Center ##
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

## Align Right ##
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=8, padx=5)

# -----------------&&&&&&& end toolbar &&&&&------------------


########################## text editor ##########################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


# -----------------&&&&&&& end text editor &&&&&------------------


########################## status bar ##########################
# -----------------&&&&&&& end status bar &&&&&------------------


########################## main menu functionality ##########################

# File #
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='CTRL+O')
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Save As', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')

# Edit #
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+P')
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

# View #
view.add_checkbutton(label='Tool Bar', image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar', image=status_bar_icon, compound=tk.LEFT)

# Color Theme #
count = 0
for color in color_dict:
    color_theme.add_radiobutton(label=color, image=color_icons[count], compound=tk.LEFT,
                                variable=theme_choice)
    count += 1

# -----------------&&&&&&& end main menu functionality &&&&&------------------

main_application.config(menu=main_menu)
main_application.mainloop()
