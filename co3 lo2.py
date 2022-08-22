# tkinter programming:
  # it is standard gui library for python
  # python+ tkinter= fast and easy to create gui applications.
  # tkiter provides a powerful object-oriented interface to the Tk gui toolkit.
  # creating a gui application using tkinter is an easy task .
      # following options are to perform:
         # import the tkinter module.
         # create the gui application main window.
         # Add one or more of the above-mentioned widgets to the gui application.
         # enter the main event loop to take action against each event triggered by the user.
import tkinter
top= tkinter.Tk()
top.mainloop() # here the tk screen pop-up.which is blank.
  # there are two main methods used which the user needs to remember while creating the python application with gui.
    # Tk(screenName=None, baseName=None, className='Tk', useTk=1):
       # to create a main window tkinter offers a method: Tk(screenName=None, baseName=None, className='Tk', useTk=1)
       # to change the name of the window , you can change the className to the desired one.
       # the basic code used to create the main window of the application is :m= tkinter.Tk()
                                                                      # where m is the name of the main window object.
        # mainloop():
            # there is a method known by the name mainloop() is used when your application is ready to run.
            # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
            # m.mainloop()

       # tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows.
          # there are mainly three geometry manager classes class.
            # 1.pack() method: it organizes the widgets in blocks before placing in the parent widget.
            # 2.grid() method: it organizes the widgets in grid(table-like structure) before placing in the parent widget.
            # 3.place() method: it organizes the widgets by placing them on specific positions directed by the programmer.
          # there are a number of widgets which you can put in your tkinter application.
            # tkinter widgets: # button
                               # label
                               # entry
                               # text
                               # Canvas
                               # frames
                             # these used to build the python gui applications.

                        # python tkinter button:
                           # the button widget is used to add various types of buttons to the python application.
                           # python allows us to configure the look of the button according to our requirements.
                           # various options can be set or reset depending upon the requirements.
                           # another method or function with a button which is called when the button is pressed.
                           # syntax to use the button widget is given below.
                               # W = Button(parent,options)
                                 # 1. activebackground = it represents the background  of the button when the mouse hover the button.
                                 # 2. activeforeground = it represents the font color of the button when the mouse hover the button.
                                 # 3. bd = it represents the border width in pixels.
                                 # 4. bg = it represents the background color of the button.
                                 # 5. command = it is set to the function call which is scheduled when the function is called.
                                 # 6. fg = foreground color of the button.
                                 # 7. Font = the font of the button text.
                                 # 8. height = the height of the button.the height is represented in the number of text lines for the texual lines or the number of pixels for the images.
                                 # 9. highlightcolor = the color of the highlist when the button has the focus.
                                 #10. image = it is set to the image displayed on the button.
                                 # 11. justify = it illustrates the way by which the multiple text lines are represented. it is set to LEFT for left justification, RIGHT for the right justification and CENTER for the center.
                                 # 12. Padx = additional padding to the button in the horizontal direction.
                                 # 13. Pady = additional padding to the button in the vertical direction.
                                 # 14. Relief = it represents the type of the border.it can be SUNKEN , RAISED, GROOVE AND RIDGE.
                                 # 15.state = this option is set to DISABLED to make the button unresponsive. the ACTIVE represents the active state of the button.
                                 # 16.underline = set this option to make the button text underlined.
                                 # 17. width = the width of the button . it exists as a number of letters for textual buttons or pixels for image buttons.
                                 # 18. wraplength: if the value is set to a positive number, the text lines will be wrapped to fit within this length.
from tkinter import *
top = Tk()
top.geometry("200x100")
b = Button(top,text="simple")
b.pack()
top.mainloop() # this show tk inside it in screen shows a button within it simple is written.

# python tkinter canvas:
  # the canvas widget is used to add the structured graphics to the python application.
  # it is used to draw the graph and piots to the python application.
  # syntax of canvas: w = canvas(parent,options)
       # 1.bd = it represents the border width. the default width is 2.
       # 2.bg = it represents the background color of the canvas.
       # 3.confine = it is set to make the canvas unscrollable outside the scroll region.
       # 4. cursor = the cursor is used as the arrow , circle,dot etc. on the canvas.
       # 5. height = it represents the size of the canvas in the vertical direction.
       # 6. highlightcolor = it represents the highlight color when the widget is focused.
       # 7. relief = it represents the type of the border. the possible values are SUNKEN, RAISED , GROOVE AND RIDGE.
       # 8. scrollregion = it represents the coordinates specified as the tuple containing the area of the canvas .
       # 9. width = it represents the width of the canvas.
       # 10. xscrollincrement = if it is set to a positive value. the canvas is placed only to the multiple of this  value.
       # 11. xscrollcommand = if the canvas is scrollable, this attribute should be the .set() method of the horizontal scrollbar.
       # 12. yscrollincrement = works like xscrollincrement , but governs vertical movement.
       # 13. yscrollcommand = if the canvas is scrollable, this attribute should be the .set() method of the vertical scrollbar.
      # Eg:
from tkinter import *
top = Tk()
top.geometry("600x1000")
# creating a simple canvas
c = Canvas(top,bg="blue",height = "800")
c.pack()
top.mainloop()   # in this we can see the long thik blue box.

# Eg: Creating an arc:
from tkinter import *
top = Tk()
top.geometry("200x200")
# creating a simple canvas
c = Canvas(top,bg="blue", height="200", width =200)
arc=c.create_arc((5,10,150,200),start = 0, extent=150, fill="white")
c.pack()
top.mainloop()  # arc of 270 degree is fomed inside the blue rectangle.


# PYTHON TKINTER LABEL:
  # the label is used to specify the container box where we can place the text or images.
  # this widget is used to provide the message to the user about other widgets used in the python application.
  # there are various options which can be specified to configure the text or the part of the text shown in the label.
  # syntax:
    # w = Label(master,options)
    # 1. anchor = it specifies the exact position of the text within the size provided to the widget. the default value is center , which is used to center the text within the specified space.
    # 2. bg = the background color displayed behind the widget.
    # 3. bitmap = it is used to set the bitmap to the graphical object specified so that  the label can represent the graphics instead of text.
    # 4. bd = it represents the width of the border. the default is 2 pixels.
    # 5. cursor = the mouse pointer will be changed to the type of the cursor specified, i.e. arrow,dot,etc.
    # 6. font = the font type of the text written inside the widget.
    # 7. fg = the foreground color of the text written inside the widget.
    # 8. height = the height of the widget.
    # 9. image = the image that is to be shown as the label.
    # 10. justify = it  is used to show the orientation of the text if the text contains multiple lines.it can be  set to LEFT for left justification, RIGHT  for right justification, and CENTER for center justification.
    # 11. padx = the horizontal padding of the text. the default value is 1.
    # 12. pady = the vertical padding of the text . the default  value is 1.
    # 13. relief = the type of the border. the default value is FLAT.
    # 14. text = this is set to the string variable which may contain one or more line of text.
    # 15. textvariable = the text written inside the widget is set to the control variable StringVar so that it can be accessed and changed accordingly.
    # 16. underline = we can display a line under the specified letter of the text. set this option to the number of the letter under which the line will be displayed.
    # 17. width = the width of the widget. it is specified as the number of characters.
    # 18. wraplength = instead of having only one line as the label text, we can break it to the number of lines where each line has the number of characters specified to this option.
from tkinter import *
top = Tk()
top.geometry("400x250")
# creating label
uname = Label(top,text="username").place(x=30,y=50)
# creating label
password= Label(top,text= "Password").place(x=30,y=90)
sbmitbtn= Button(top,text= "Submit", activebackground="pink",activeforeground = "blue").place(x=30,y = 120)
top.mainloop() # this shows username and password with submit button which changes color after clicking on it.

# python tkinter entry:
 # entry widget is used to provide the single line text-box to the user to accept a value from the user.
 # we can use the entry widget to accept the text strings from the user.
 # it can only be used for one line of the text from the user.
 # for multiple lines of text, we must use the text widget.
 # syntax : w = Entry(parent,options
   # bg = the background color of the widget.
   # bd = the border width of the widget in pixels.
   # cursor = the mouse pointer will be changed to the cursor type set to the arrow, dot, etc.
   # exportselection = the text written inside the entry box will be automatically copied to the clipboard by default. we can set the exportselection to 0 to not copy this.
   # fg = it represents the color of the text.
   # font = it represents the font type of the text.
   # highlightbackground = it represents the color to display in the traversal highlight region when the widget does not have the input focus.
   # highlightcolor = it represents the color to use for the traversal highlight rectangle that is drawn around the widgets when it has the input focus.
   # highlightthickness = it represents a non-negative value indicating the width of the highlight rectangle to draw around the outside of the widget when it has the input focus.
   # insertbackground = it represents the color to use as background in the area covered by the insertion cursor .this color will normally override  either the normal background for the widget.
   # insertborderwidth = it represents a non-negative value indicating the width of the 3-D border to draw around the insertion cursor. the value may have any of the forms  acceptable to Tk_GetPixels.
   # insertofftime = it represensts a non-negative integer value indicating the number of milliseconds the insertion cursor should remain "off"  in each blink cycle . if this option is zero , then the cursor doesn't   blink: it is on all the time.
   # insertontime = specifies a non-negative integer value indicating the number of milliseconds  the insertion cursor should remain'on' in each blink cycle.
   # insertwidth = it represents the value indicating the total width of the insertion cursor. the value may have any of the forms acceptable to Tk_GetPixels.
   # justify = it specifies how the text is organized if the text contains multiple lines.
   # relief = it specifies the type of the border . its default value is FLAT.
   # selectbackground = the background color of the selected text.
   # selectforeground = the font color of the selected task.
   # show = it is used to show the entry text of some other type instead of the string.For example, the password is typed using stars(*).
   # textvariable = it is set to the instance of the StringVar to retrieve the text from the entry.
   # width = the width of the displayed text or image.
   # xscrollcommand = the entry widget can be linked  to the horizontal scrollbar if we want the user to enter more text then the actual width of the widget.
   # eg:
from tkinter import *
top = Tk()
top.geometry("400x250")
name = Label(top,text="Name").place(x = 30,y = 50)
email = Label(top,text="Email").place(x = 30,y=90)
password = Label(top,text="Password").place(x=30,y= 130)
sbmitbtn = Button(top,text="submit",activebackground = "pink", activeforeground = "blue").place(x=30,y=170)
e1=Entry(top).place(x=80,y=50)
e2 = Entry(top).place(x=80,y=90)
e3 = Entry(top).place(x=95,y=130)
top.mainloop()



# Python tkinter text:
  #  the text widget is used to show the text data on the python application.
  # tkinter provides us the entry widget which is used to implement the single line text box.
  # the text widget is used to display the multi-line formatted text with various styles and attributes.
  # the text widget is mostly used to provide the text editor to the user.
  # syntax: w = Text(top,options)
  # Eg:
from tkinter import *
top = Tk()
text = Text(top)
text.insert(INSERT,"Name..")
text.insert(END,"Salary....")
text.pack()
top.mainloop()


# Python tkinter frame:
  # python tkinter frame widget is used to organize the group of widgets.
  # It acts like a container which can be used to hold the other widgets.
  # the rectangular areas of the screen are used to organize the widgets to the python application.
  # syntax = w = Frame(parent,options)
    # bd = it represents the border width.
    # bg = the background color of the widget.
    # cursor = the mouse pointer is changed to the cursor type set to different values like an arrow,dot,etc.
    # height = the height of the frame.
    # highlightbackground = the color of the background color when it is under focus.
    # highlightcolor = the text color when the widget is under focus.
    # highlightthickness = it specifies the thickness around the border when the widget is under the focus .
    # relief = it specifies the type of the border.the default value if FLAT.
    # width = it represents the width of the widget.

from tkinter import *
top = Tk()
top.geometry("140x100")
frame = Frame(top)
frame.pack()
leftframe = Frame(top)
leftframe.pack(side=LEFT)
rightframe = Frame(top)
rightframe.pack(side=RIGHT)
btn1 = Button(frame,text= 'submit',fg="red", activebackground = "red")
btn1.pack(side= LEFT)
btn2 = Button(frame,text="Remove",fg="brown",activebackground="brown")
btn2.pack(side = RIGHT)
btn3 = Button(rightframe,text="Add", fg = "blue",activebackground="blue")
btn3.pack(side = LEFT)
btn4 = Button(leftframe, text="Modify", fg="black",activebackground="white")
btn4.pack(side=RIGHT)
top.mainloop()
