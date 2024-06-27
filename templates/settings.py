import customtkinter as ctk
from db.database import create_connection
from logging_function.logger_function import get_logger

logger = get_logger(__name__)

class SettingsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_color_scheme = ctk.CTkLabel(self, text="Color Scheme")
        self.label_color_scheme.pack(pady=10)
        self.color_var = ctk.StringVar(value="light")
        self.radio_light = ctk.CTkRadioButton(self, text="Light", variable=self.color_var, value="light", command=self.change_color_scheme)
        self.radio_light.pack(pady=10)
        self.radio_dark = ctk.CTkRadioButton(self, text="Dark", variable=self.color_var, value="dark", command=self.change_color_scheme)
        self.radio_dark.pack(pady=10)

        self.label_scale = ctk.CTkLabel(self, text="Scale")
        self.label_scale.pack(pady=10)
        self.scale_var = ctk.StringVar(value="100%")
        self.scale_option = ctk.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"], variable=self.scale_var, command=self.change_scale)
        self.scale_option.pack(pady=10)

    def change_color_scheme(self):
        color_scheme = self.color_var.get()
        if color_scheme == "light":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE settings SET color_scheme = ?", (color_scheme,))
        conn.commit()
        conn.close()
        logger.info(f"Color scheme changed to {color_scheme}")

    def change_scale(self, scale):
        scale_value = int(scale[:-1]) / 100
        self.master.tk.call('tk', 'scaling', scale_value)

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE settings SET scale = ?", (scale,))
        conn.commit()
        conn.close()
        logger.info(f"Scale changed to {scale}")
