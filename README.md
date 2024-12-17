# Final-Project-CST205
Final Project for CST205 Digital ScrapBook Creator 
Week 1: Project Planning and Initial Setup
Goal: Plan the core functionality of the Digital Scrapbook Creator and set up the development environment.
Research:
Decided on using Python and Tkinter for the GUI development.
Chose Pillow for image manipulation and handling.
Identified features like adding images, text, and saving projects as JSON.
Initial Setup:
Installed necessary libraries (tkinter, Pillow).
Created project structure, including separate files for the GUI (scrapbook_gui.py), scrapbook logic (scrapbook.py), and asset files (backgrounds, icons).
Set up basic UI elements: window title, buttons, and placeholders for scrapbook content.

Week 2: Basic Functionality Implementation
Goal: Implement basic features like adding pages, adding text, and saving/loading scrapbook data.
Implemented Features:
Created the Scrapbook class, allowing users to add pages and elements (text and images) to each page.
Built Add Page functionality to add a new page to the scrapbook.
Implemented the Add Text functionality with a simple text field for users to input and add text.
Used file dialogs to allow users to upload images and save projects as Python files.
Challenges:
Figuring out how to store and retrieve elements (text and images) for each page.
Handling image resizing and displaying multiple images on a page without overlaps.
Outcome:
A scrapbook that allows adding pages and basic content (text/images).
Save/load functionality with JSON format.

Week 3: Enhancing User Interface and Adding Styling
Goal: Improve the user interface with styling, background images, and better button interactions.
Implemented Features:
Added a background image for the main window to make the scrapbook feel more immersive.
Styled buttons with custom colors, fonts, and hover effects for better user experience.
Created a refresh canvas function to redraw the scrapbook page after adding elements.
User Experience Improvements:
Improved the layout with better padding and spacing between elements.
Updated text elements to support custom fonts and colors.
Outcome:
A more polished and visually appealing GUI.
Better user interaction with styled buttons and backgrounds.

Week 4: Finalizing Features and Export Functionality
Goal: Add advanced features like exporting the scrapbook to a PDF and final bug fixes.
Implemented Features:
Added Export to PDF functionality to allow users to save their scrapbook as a PDF file.
Refined the image handling to allow resizing and placement of images with drag-and-drop.
Fixed bugs related to saving and loading multiple pages with different content types (text/images).
Testing:
Tested the scrapbook with different combinations of text and images.
Ensured the PDF export maintains the layout and quality of images.
Outcome:
A non functional Digital Scrapbook Creator that supports adding text, images, saving/loading projects, and exporting to PDF.
Conclusion
Final Outcome: Developed a Digital Scrapbook Creator with the ability (yet to be addded) to add text and images, save and load scrapbook projects, and export them as PDFs. The user interface has been polished with custom backgrounds and styled buttons.
Challenges: The main challenge was ensuring integration between the GUI and the scrapbook logic, particularly for handling images and saving/loading project data.
Future Enhancements:
Add more customization options like changing fonts, text sizes, and colors.
Introduce additional scrapbooking features like adding stickers or decorative frames.
Implement drag-and-drop functionality for images and text. 
Having a working Digital Scrapbook.
