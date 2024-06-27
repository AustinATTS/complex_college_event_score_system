def scale_widget(widget, width_factor, height_factor):
    width = widget.winfo_width()
    height = widget.winfo_height()
    widget.config(width=int(width * width_factor), height=int(height * height_factor))
