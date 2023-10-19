from customtkinter import CTkLabel, CTkFont, CTkEntry, CTkButton, CTkComboBox


class MyLabel(CTkLabel):
    def __init__(self, parent, text, text_color, font_size, x, y, image=None):
        super().__init__(parent)
        self.font = CTkFont("arial", font_size)
        self.configure(text=text, text_color=text_color, font=self.font, image=image)
        self.place(x=x, y=y)


class MyEntry(CTkEntry):
    def __init__(self, parent, place_holder_text, x, y, text=None):
        super().__init__(parent)
        self.place(x=x, y=y)
        self.configure(placeholder_text=place_holder_text, textvariable=text, width=300)


class MyBottom(CTkButton):
    def __init__(self, parent, text, fg_color, text_color, hover_color,
                 x, y, width, command, height=30, state="normal"):
        super().__init__(parent)
        self.configure(bg_color=fg_color, width=width, height=height, text=text, fg_color=fg_color,
                       text_color=text_color, hover_color=hover_color,
                       command=command, state=state,font=("Roman", 17, "bold"))

        self.place(x=x, y=y)


class MyCombo_Box(CTkComboBox):
    def __init__(self, parent, x, y, width, items_list, current_value):
        super().__init__(parent)
        self.configure(width=width, values=items_list)
        self.set(f"{current_value}")
        self.place(x=x, y=y)