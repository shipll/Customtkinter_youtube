from customtkinter import CTk, CTkImage, END, CTkFrame, StringVar
from PIL import Image
from widgets import *
from pytube import YouTube
from tkinter import messagebox, filedialog
from urllib.request import urlopen


class MainSystem(CTk):
    def __init__(self):
        super().__init__()
        self.main_label = None
        self.link_entry = None
        self.video_link = ""
        self.check_button = None
        self.location_button = None
        self.quality_combo = None
        self.file_location = None
        self.download_button = None
        self.title = ""
        self.info_frame = CTkFrame(self, width=400, height=120, fg_color="#800000")
        self.geometry("600x400")
        self.configure(fg_color="#803005")
        self.resizable(False, False)
        self.logo = CTkImage(dark_image=Image.open("youtube.png"), size=(400, 200))
        CTkLabel(self, image=self.logo, text="").pack()
        self.main_windows()
        self.mainloop()

    def main_windows(self):
        self.main_label = MyLabel(self, "enter youtube link :", "white", 16, 240, 220)
        self.link_entry = MyEntry(self, " ", 150, 250)
        self.check_button = MyBottom(self, "check", "#5d84e2", "white", "red", 245, 290, 100,
                                     lambda: self.check(self.link_entry))

    def check(self, entry):
        if not entry.get():
            messagebox.showerror(message="you must put youtube link")
            return

        try:
            youtube_link = YouTube(entry.get())
            self.video_link = entry.get()
        except:
            messagebox.showerror(message="invalid link")
            entry.delete(0, END)
            return

        self.location_button = MyBottom(self, "LOCATION", "#5d84e2", "white", "red", 300, 330, 50,
                                        lambda: self.set_location())
        self.quality_combo = MyCombo_Box(self, 120, 330, 150, ["HIGH QUALITY VIDEO", "LOW QUALITY VIDEO", "AUDIO"],
                                         "HIGH QUALITY VIDEO")
        thumbnail_url = str(YouTube(entry.get()).thumbnail_url)
        url_pic = urlopen(thumbnail_url)
        self.info_frame.place(x=150, y=210)
        photo = CTkImage(dark_image=Image.open(url_pic), size=(100, 100))
        CTkLabel(self.info_frame, image=photo, text="", width=90, height=70).place(x=0, y=0)
        title = YouTube(entry.get()).title
        CTkLabel(self.info_frame, width=90, height=70, text=f"title :\n{title[0:20]}").place(x=120, y=30)
        self.main_label.place_forget()
        self.link_entry.place_forget()
        self.check_button.place_forget()

    def set_location(self):
        self.file_location = filedialog.askdirectory()
        self.download_button = MyBottom(self, "download", "#5d84e2", "white", "red",
                                        390, 330, 90, lambda: self.download(self.quality_combo))
        self.location_button.place_forget()

    def download(self, combo):
        if combo.get() == "HIGH QUALITY VIDEO":
            YouTube(self.video_link).streams.get_highest_resolution().download(self.file_location)
            messagebox.showinfo(message="download completed")
            combo.place_forget()
            self.download_button.place_forget()
            self.info_frame.place_forget()
            self.main_windows()
        if combo.get() == "LOW QUALITY VIDEO":
            YouTube(self.video_link).streams.get_lowest_resolution().download(self.file_location)
            messagebox.showinfo(message="download completed")
            combo.place_forget()
            self.download_button.place_forget()
            self.info_frame.place_forget()
            self.main_windows()

        if combo.get() == "AUDIO":
            YouTube(self.video_link).streams.get_audio_only().download(self.file_location)
            messagebox.showinfo(message="download completed")
            combo.place_forget()
            self.download_button.place_forget()
            self.info_frame.place_forget()
            self.main_windows()


if __name__ == "__main__":
    MainSystem()
