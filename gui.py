import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from scrapbook import Scrapbook
from PIL import Image, ImageTk

class ScrapbookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Scrapbook Creator")

        self.scrapbook = Scrapbook()
        self.bg_image = Image.open("images/penguin.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        self.canvas.pack()
        
        self.add_page_button = tk.Button(root, text="Add Page", command=self.add_page)
        self.add_page_button.pack()

        self.add_text_button = tk.Button(root, text="Add Text", command=self.add_text)
        self.add_text_button.pack()

        self.add_image_button = tk.Button(root, text="Add Image", command=self.add_image)
        self.add_image_button.pack()

        self.save_button = tk.Button(root, text="Save Project", command=self.save_project)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load Project", command=self.load_project)
        self.load_button.pack()

        self.export_button = tk.Button(root, text="Export to PDF", command=self.export_to_pdf)
        self.export_button.pack()


    def add_page(self):
        self.scrapbook.add_page()
        self.refresh_canvas()

    def add_text(self):
        text = "Sample Text"
        x, y = 100, 100
        self.scrapbook.add_element({'type': 'text', 'text': text, 'x': x, 'y': y})
        self.refresh_canvas()

    def add_image(self):
        filepath = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg")])
        if filepath:
            image = {'type': 'image', 'path': filepath, 'x': 200, 'y': 200}
            self.scrapbook.add_element(image)
            self.refresh_canvas()

    def save_project(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            self.scrapbook.save_project(filename)
            messagebox.showinfo("Saved", "Project saved successfully.")

    def load_project(self):
        filename = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if filename:
            self.scrapbook.load_project(filename)
            self.refresh_canvas()
            messagebox.showinfo("Loaded", "Project loaded successfully.")

    def export_to_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if filename:
            self.scrapbook.export_to_pdf(filename)
            messagebox.showinfo("Exported", "Project exported as PDF.")

    def add_decorative_element(self):
        """Add a decorative element (e.g., a sticker)."""
        filepath = filedialog.askopenfilename(title="Select a Sticker", filetypes=[("Image files", "*.png;*.jpg")])
        if filepath:
            element = {'type': 'image', 'path': filepath, 'x': 300, 'y': 300}
            self.scrapbook.add_element(element)
            self.refresh_canvas()

    def resize_image(self, filepath, width, height):
        """Resize an image to the given width and height."""
        img = Image.open(filepath)
        img = img.resize((width, height), Image.ANTIALIAS)
        return img

    def choose_text_color(self):
        """Allow the user to choose a text color."""
        color = askcolor()[1]
        if color:
            self.text_color = color


    def refresh_canvas(self):
        """Redraw the current page on the canvas."""
        self.canvas.delete("all")
        if self.scrapbook.pages:
            page_elements = self.scrapbook.pages[self.scrapbook.current_page]
            for element in page_elements:
                if element['type'] == 'text':
                    self.canvas.create_text(element['x'], element['y'], text=element['text'], anchor="nw")
                elif element['type'] == 'image':
                    img = Image.open(element['path'])
                    img.thumbnail((100, 100))
                    img = ImageTk.PhotoImage(img)
                    self.canvas.create_image(element['x'], element['y'], image=img, anchor="nw")
                    self.canvas.image = img


root = tk.Tk()
gui = ScrapbookGUI(root)
root.mainloop()
