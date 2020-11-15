#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    The main programm that is responsible for the calling funtions from other programms    
"""

import tkinter as tk

root = tk.Tk()

my_lable = tk.Label(root, text = "hello world", 
                    fg = 'white',
                    bg = 'black'
                    )

my_lable.pack(expand = 1)

root.mainloop()    