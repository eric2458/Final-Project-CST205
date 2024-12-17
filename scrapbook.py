from PIL import Image, ImageDraw, ImageFont
import json
import os

class Scrapbook:
    def __init__(self):
        self.pages = []
        self.current_page = 0

    def add_page(self):
        """Adds a new empty page."""
        self.pages.append([])
        self.current_page = len(self.pages) - 1

    def add_element(self, element):
        """Adds an element (image or text) to the current page."""
        if self.pages:
            self.pages[self.current_page].append(element)

    def save_project(self, filename):
        """Saves the scrapbook data to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.pages, f)

    def load_project(self, filename):
        """Loads scrapbook data from a JSON file."""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.pages = json.load(f)
                self.current_page = 0

    def export_to_pdf(self, output_filename):
        """Exports the scrapbook pages as a PDF."""
        images = []
        for page_elements in self.pages:
            page_image = Image.new('RGB', (800, 600), color=(255, 255, 255))
            draw = ImageDraw.Draw(page_image)
            for element in page_elements:
                if element['type'] == 'image':
                    img = Image.open(element['path'])
                    img = img.resize((100, 100))
                    page_image.paste(img, (element['x'], element['y']))
                elif element['type'] == 'text':
                    font = ImageFont.load_default()
                    draw.text((element['x'], element['y']), element['text'], font=font, fill=(0, 0, 0))
            images.append(page_image)

        images[0].save(output_filename, save_all=True, append_images=images[1:], resolution=100.0, quality=95)

