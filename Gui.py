# from tkinter import *
# import sqlite3
#
#
#
# root = Tk()
# root.title("Cubes Project List")
# root.geometry('700x700')
# conn = sqlite3.connect("cubesProject.sqlite")
# c = conn.cursor()
#
#
# label = Label(root, text="Select one of the entries to view the entry data: ", fg='red').pack()
#
#
# def entryid():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT entryID FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_entryid = Button(root, text="Click to see list of Entry ID's ", command=entryid,fg='magenta').pack()
#
#
#
# def prefix():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT prefix FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_prefix = Button(root, text="Click to see list of Prefix's ", command=prefix,fg='magenta').pack()
#
#
# def first_name():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT first_name FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
#
# btn = Button(root, text="Click to see list of First Names ", command=first_name, fg='magenta').pack()
#
# def last_name():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT last_name FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_lastname = Button(root, text="Click to see list of Last Names ", command=last_name,fg='magenta').pack()
#
# def title():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT title FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_title = Button(root, text="Click to see list of Title's ", command=title,fg='magenta').pack()
#
# def org():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT org FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_org = Button(root, text="Click to see list of Organizations ", command=org,fg='magenta').pack()
#
# def email():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT email FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_email = Button(root, text="Click to see list of Emails ", command=email,fg='magenta').pack()
#
# def website():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT website FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_website = Button(root, text="Click to see list of Website's ", command=website,fg='magenta').pack()
#
# def courseproject():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT course_project FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_courseproject = Button(root, text="Click to see list of Course Projects ", command=courseproject,fg='magenta').pack()
#
#
# def guestspeaker():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT guest_speaker FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_guestspeaker = Button(root, text="Click to see list of Guest Speakers ", command=guestspeaker,fg='magenta').pack()
#
# def sitevisit():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT site_visit FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_sitevisit = Button(root, text="Click to see list of Sites Visits ", command=sitevisit,fg='magenta').pack()
#
#
# def jobshadow():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT job_shadow FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_jobshadow = Button(root, text="Click to see list of Job Shadows ", command=jobshadow,fg='magenta').pack()
#
# def internship():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT internship FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_internship = Button(root, text="Click to see list of Internships ", command=internship,fg='magenta').pack()
#
# def careerpanel():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT career_panel FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_careerpanel = Button(root, text="Click to see list of Career Panels ", command=careerpanel,fg='magenta').pack()
#
#
# def networkingevent():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT networking_event FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_networkingevent = Button(root, text="Click to see list of Networking Events ", command=networkingevent,fg='magenta').pack()
#
# def subjectarea():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT subject_area FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_subjectarea = Button(root, text="Click to see list of Subject Areas ", command=subjectarea,fg='magenta').pack()
#
#
# def description():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT description FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_description = Button(root, text="Click to see list of Descriptions ", command=description,fg='magenta').pack()
#
# def funding():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT funding FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_funding = Button(root, text="Click to see list of Fundings ", command=funding,fg='magenta').pack()
#
#
# def createddate():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT created_date FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_createddate = Button(root, text="Click to see list of Created Dates ", command=createddate,fg='magenta').pack()
#
# def createdby():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT created_by FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
#
# btn_createdby = Button(root, text="Click to see list of Created By ", command=createdby,fg='magenta').pack()
#
#
# def call_all_functions():
#     """ This function calls all functions that display the data to a new window when user clicks on a selection """
#     entryid()
#     prefix()
#     first_name()
#     last_name()
#     title()
#     org()
#     email()
#     website()
#     courseproject()
#     guestspeaker()
#     sitevisit()
#     jobshadow()
#     internship()
#     careerpanel()
#     networkingevent()
#     subjectarea()
#     description()
#     funding()
#     createddate()
#     createdby()
#
#
# def button_for_closing():
#     """Simple button for exiting the GUI"""
#     exit_button = Button(root, text="Exit ", command=root.destroy).pack()
#
#


#
#
#
# if __name__ == "__main__":
#     call_all_functions()
#     button_for_closing()
#     root.mainloop()
# #    c.commit()
#     c.close()



