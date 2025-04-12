from tkinter import *
from tkinter import ttk

from main import unsw_scraper, usyd_scraper, monash_scraper, melb_scraper, uts_scraper

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="PhD Scraper Bot").grid(column=0, row=0)

ttk.Button(frm, text="UNSW", command=unsw_scraper).grid(column=0, row=1)
ttk.Button(frm, text="UniSyd", command=usyd_scraper).grid(column=0, row=2)
ttk.Button(frm, text="Monash", command=monash_scraper).grid(column=0, row=3)
ttk.Button(frm, text="Melb", command=melb_scraper).grid(column=0, row=4)
ttk.Button(frm, text="UTS", command=uts_scraper).grid(column=0, row=5)
ttk.Button(frm, text="RMIT", command=None).grid(column=0, row=6)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
