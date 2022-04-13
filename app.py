######## GUI Packages ###########
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

import time
timestr = time.strftime("%Y%m%d-%H%M%S")


####### NLP Packages made by me 2 python files ##########
from spacy_summarization import text_summarizer
from gensim.summarization import summarize
from nltk_summarization import nltk_summarizer

###### Web Scraping Packages ##########
from bs4 import BeautifulSoup
from urllib.request import urlopen

########## Structure and Layout of the main window that opens ##########
window = Tk()
window.title(" Automatic Summaryzer")
window.geometry("700x400")
window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn',)


#######TAB LAYOUT that appear on the window eg Home,File,URl############ 
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

######### ADD TABS TO NOTEBOOK basically show the name on the window ############
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"Comparer ":^20s}')
tab_control.add(tab5, text=f'{"Multiple File Summary ":^20s}')
tab_control.add(tab6, text=f'{"About ":^20s}')


##when you click on each tab the following labels will show like for eg youc click on URL tab the text URL will show.###
label1 = Label(tab1, text= 'Summaryzer',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'File Processing',padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text= 'URL',padx=5, pady=5)
label3.grid(column=0, row=0)

label3 = Label(tab4, text= 'Compare Summarizers',padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab5, text= 'About',padx=5, pady=5)
label4.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')



#### ALL the Functions required to run the entire code ###


###ALL the clear and reset button functions for the entire code###


##########For TAB 1 i.e HOME #################

# Reset entry widget
def clear_text():
	entry.delete('1.0',END)
#clears the display widget
def clear_display_result():
	tab1_display.delete('1.0',END)


##########For TAB 2 i.e FILE ############
# Reset Text  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_text_result():
	tab2_display_text.delete('1.0',END)



################For TAB 3 i.e URL ##############

# Reset For URL 
def clear_url_entry():
	url_entry.delete(0,END)
# Clear entry widget 
def clear_url_text():
	url_display.delete('1.0',END)
#clear display widget
def clear_url_display():
	tab3_display_text.delete('1.0',END)


#########For TAB 4 i.e COMPARER #################

# Reset entry widget
def clear_compare_text():
	entry1.delete('1.0',END)
# CLear display widget
def clear_compare_display_result():
	tab4_display.delete('1.0',END)



#########For TAB 5 i.e MULTIPLE #################

# Reset of TEXT 1
def clear_text_file1():
	displayed_file1.delete('1.0',END)
# Clear Result of display 1
def clear_text_result1():
	tab5_display_text1.delete('1.0',END)


# Reset of Text 2  
def clear_text_file2():
	displayed_file2.delete('1.0',END)

# Clear Result of display 2
def clear_text_result2():
	tab5_display_text2.delete('1.0',END)


def clear_final_summary():
	tab5_display_text3.delete('1.0',END)



### MAIN FUNCTIONS ###


#####Function For TAB 1 i.e HOME ########
def get_summary():
	raw_text = str(entry.get('1.0',tk.END))
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	tab1_display.insert(tk.END,result)

def save_summary():
	raw_text = entry.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	file_name = 'yoursummary' + timestr + '.txt'
	with open(file_name,'w') as f:
		f.write(final_text)

##### Functions for TAB 2 i.e FILE ##########
# Open File to Read and Process
def openfiles():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)

def get_file_summary():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


##### Functions for TAB 3 i.e URL ##########
# Fetch Text From Url
def get_text():
	raw_text = str(url_entry.get())
	page = urlopen(raw_text)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	url_display.insert(tk.END,fetched_text)

def get_url_summary():
	raw_text = url_display.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab3_display_text.insert(tk.END,result)	


##### Functions for TAB 4 i.e COMPARER ##########

def use_spacy():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSpacy Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_nltk():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nNLTK Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_gensim():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = summarize(raw_text)
	print(final_text)
	result = '\nGensim Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

##### Functions for TAB 5 i.e MULTIPLE ##########

# Open File 1
def openfiles1():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file1.insert(tk.END,read_text)

# open file 2
def openfiles2():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file2.insert(tk.END,read_text)

### File 1 Summary
def get_file_summary1():
	raw_text1 = displayed_file1.get('1.0',tk.END)
	final_text1 = text_summarizer(raw_text1)
	result1 = '\nSummary:{}'.format(final_text1)
	tab5_display_text1.insert(tk.END,result1)

### File 2 Summary
def get_file_summary2():
	raw_text2 = displayed_file2.get('1.0',tk.END)
	final_text2 = text_summarizer(raw_text2)
	result2 = '\nSummary:{}'.format(final_text2)
	tab5_display_text2.insert(tk.END,result2)


### Final Summary
def get_file_final_summary():
	raw_text = displayed_file1.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	result1 = '\nCombined Summary:{}'.format(final_text)
	tab5_display_text1.insert(tk.END,result1)

	raw_text2 = displayed_file2.get('1.0',tk.END)
	final_text2 = text_summarizer(raw_text2)
	result2 = '\n{}'.format(final_text2)
	tab5_display_text2.insert(tk.END,result2)
	
	tab5_display_text3.insert(tk.END,result1+result2)


####### TAB 1 HOME ########
l1=Label(tab1,text="Enter Text To Be Summarized")
l1.grid(row=1,column=0)

entry=ScrolledText(tab1,height=15,width=150,wrap=WORD)
entry.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

# BUTTONS
button1=Button(tab1,text="Reset",command=clear_text, width=12,bg='green',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text="Summarize",command=get_summary, width=12,bg='#03A9F4',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab1,text="Clear Result", command=clear_display_result,width=12,bg='green',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab1,text="save summary", command=save_summary,width=12,bg='green',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)



# Display Screen For Result
tab1_display = ScrolledText(tab1,height=15,width=150,wrap=WORD)
tab1_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


###### TAB 2 FILE #########
l1=Label(tab2,text="Open File To Summarize")
l1.grid(row=1,column=1)

displayed_file = ScrolledText(tab2,height=15,width=150,wrap=WORD)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File", width=12,command=openfiles,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="green",fg='#fff')
b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab2,text="Summarize", width=12,command=get_file_summary,bg='#03A9F4',fg='#fff')
b2.grid(row=3,column=2,padx=10,pady=10)

b3=Button(tab2,text="Clear Result", width=12,command=clear_text_result,bg="green",fg='#fff')
b3.grid(row=5,column=1,padx=10,pady=10)



# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2,height=15,width=150,wrap=WORD)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)


##########  TAB 3 URL ###############
l1=Label(tab3,text="Enter URL To Summarize")
l1.grid(row=1,column=0)

raw_entry=StringVar()
url_entry=Entry(tab3,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

# BUTTONS
button1=Button(tab3,text="Reset",command=clear_url_entry, width=12,bg='green',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab3,text="Get Text",command=get_text, width=12,bg='#c5cae9')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab3,text="Clear Result", command=clear_url_display,width=12,bg='green',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab3,text="Summarize",command=get_url_summary, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

button5=Button(tab3,text="Clear Text",command=clear_url_text, width=12,bg='green',fg='#fff')
button5.grid(row=6,column=1,padx=10,pady=10)


# Display Screen For Result
url_display = ScrolledText(tab3,height=15,width=150,wrap=WORD)
url_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


tab3_display_text = ScrolledText(tab3,height=15,width=150,wrap=WORD)
tab3_display_text.grid(row=10,column=0, columnspan=3,padx=5,pady=5)


################### TAB 4 COMPARER ##################
l1=Label(tab4,text="Enter Text To Summarize")
l1.grid(row=1,column=0)

entry1=ScrolledText(tab4,height=15,width=150,wrap=WORD)
entry1.grid(row=2,column=0,columnspan=3,padx=5,pady=3)

# BUTTONS
button1=Button(tab4,text="Reset",command=clear_compare_text, width=12,bg='green',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab4,text="SpaCy",command=use_spacy, width=12,bg='#03A9F4',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab4,text="Clear Result", command=clear_compare_display_result,width=12,bg='green',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab4,text="NLTK",command=use_nltk, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=4,column=2,padx=10,pady=10)

button5=Button(tab4,text="Gensim",command=use_gensim, width=12,bg='#03A9F4',fg='#fff')
button5.grid(row=5,column=1,padx=10,pady=10)


# Display Screen For Result
tab4_display = ScrolledText(tab4,height=15,width=150,wrap=WORD)
tab4_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


########## TAB 5 MULTIPLE ########################


###### first open file ############
l1=Label(tab5,text="Open File 1 To Summarize")
l1.grid(row=1,column=1)

displayed_file1 = ScrolledText(tab5,height=7,wrap=WORD)
displayed_file1.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR 1st TAB/FILE READING TAB
b0=Button(tab5,text="Open File", width=12,command=openfiles1,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab5,text="Reset ", width=12,command=clear_text_file1,bg="green",fg='#fff')
b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab5,text="Summarize", width=12,command=get_file_summary1,bg='#03A9F4',fg='#fff')
b2.grid(row=3,column=2,padx=10,pady=10)

b3=Button(tab5,text="Clear Result", width=12,command=clear_text_result1,bg="green",fg='#fff')
b3.grid(row=5,column=1,padx=10,pady=10)


######## second open file ###########

l2=Label(tab5,text="Open File 2 To Summarize")
l2.grid(row=1,column=7)

displayed_file2 = ScrolledText(tab5,height=7,wrap=WORD)
displayed_file2.grid(row=2,column=7, columnspan=3,padx=5,pady=3)


# BUTTONS FOR 2nd TAB/FILE READING TAB

b0=Button(tab5,text="Open File", width=12,command=openfiles2,bg='#c5cae9')
b0.grid(row=3,column=7,padx=10,pady=10)

b1=Button(tab5,text="Reset ", width=12,command=clear_text_file2,bg="green",fg='#fff')
b1.grid(row=3,column=8,padx=10,pady=10)

b2=Button(tab5,text="Summarize", width=12,command=get_file_summary2,bg='#03A9F4',fg='#fff')
b2.grid(row=3,column=9,padx=10,pady=10)

b3=Button(tab5,text="Clear Result", width=12,command=clear_text_result2,bg="green",fg='#fff')
b3.grid(row=5,column=7,padx=10,pady=10)



# Display Screen for file 1
# tab2_display_text = Text(tab2)
tab5_display_text1 = ScrolledText(tab5,height=7,wrap=WORD)
tab5_display_text1.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab5_display_text1.config(state=NORMAL)

 
# Display Screen for file 2
# tab2_display_text = Text(tab2)
tab5_display_text2 = ScrolledText(tab5,height=7,wrap=WORD)
tab5_display_text2.grid(row=7,column=7, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab5_display_text2.config(state=NORMAL)


######## FINAL SUMMARY BUTTON #############
b4=Button(tab5,text="Final Summary", command=get_file_final_summary, width=12,bg="green",fg='#fff')
b4.grid(row=12,column=0,padx=10,pady=10)


# Display Screen final
# tab2_display_text = Text(tab2)
tab5_display_text3 = ScrolledText(tab5,height=7,wrap=WORD)
tab5_display_text3.grid(row=16,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab5_display_text3.config(state=NORMAL)


button5=Button(tab5,text="Clear Final", command=clear_final_summary,width=12,bg='green',fg='#fff')
button5.grid(row=12,column=1,padx=10,pady=10)



####### TAB 6 About #############
about_label = Label(tab6,text="Automatic Text Summaryzer using nltk and spacy ",pady=5,padx=5)
about_label.grid(column=0,row=1)

b4=Button(tab6,text="Close", width=12,command=window.destroy,bg='red')
b4.grid(row=5,column=2,padx=10,pady=10)

window.mainloop()
