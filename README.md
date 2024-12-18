# Final-Project-CST205
# Eric Rubio Salazar
# CST205
# Dec 18, 2024
# https://trello.com/b/RuNkjWup
# 


Final Project for CST205 Digital ScrapBook Creator 

The Digital Scrapbook Creator allows users to design a customizable scrapbook by adding pages, text elements, and images. Users can save their work, load existing scrapbooks, and export the final design as a PDF.

Features:

Add Pages: Create new blank pages in the scrapbook.

Add Text: Place text at specific positions on a page.

Add Images: Insert images at specified coordinates.

Save Project: Save the scrapbook to a JSON file for future editing.

Load Project: Load an existing scrapbook from a JSON file.

Export to PDF: Generate a PDF version of the scrapbook with all pages and elements included.

Launch the Application:
Run the main script:

python final_project.py

User Guide

Main Interface

Buttons:

Add Page: Adds a new blank page to your scrapbook.

Add Text: Opens a dialog to input text and specify its position.

Add Image: Opens a file dialog to select an image and specify its position.

Save: Saves the current project to a JSON file.

Load: Loads an existing scrapbook from a JSON file.

Export to PDF: Exports all pages to a PDF file.

Adding Elements

Add Page:

Click the "Add Page" button to create a new blank page. You must add a page before adding any text or images.

Add Text:

Click the "Add Text" button.

Enter the desired text in the input dialog.

Specify the X and Y coordinates for the text placement (values between 0 and 800 for X, and 0 and 600 for Y).

Add Image:

Click the "Add Image" button.

Select an image file from your computer (“.png”, “.jpg”, “*.jpeg” supported).

Specify the X and Y coordinates for the image placement (values between 0 and 800 for X, and 0 and 600 for Y).

Saving and Loading Projects

Save: Click "Save" and choose a filename to save the scrapbook in JSON format.

Load: Click "Load" and select a previously saved JSON file to restore your scrapbook.

Exporting to PDF

Click "Export to PDF".

Enter the desired filename for the PDF.

The application will generate a PDF with all pages and elements included.

Common Issues

"No Pages Available" Error:

Ensure you have added at least one page before attempting to add text or images.

Crash When Adding Images:

Verify that the selected file is a valid image and in the supported format (“.png”, “.jpg”, “*.jpeg”).

Exported PDF Looks Blank:

Ensure you have added elements to your pages before exporting.


