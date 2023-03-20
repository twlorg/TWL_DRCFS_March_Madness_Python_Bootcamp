import csv
from PIL import Image, ImageDraw, ImageFont

NAME_FONT = ImageFont.truetype("bold.ttf", 72)
NAME_COORDS = (150, 735)

CODE_FONT = ImageFont.truetype("semi.ttf", 25)
CODE_CORDS = (1160, 1024)

def read_csv():
    data = []

    with open("src/student_details.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append({"name": row[0].strip(), "code": row[1]})

    return data

def write_name(name,code):
    template = Image.open("src/cert.png")
    CANVAS = ImageDraw.Draw(template)

    CANVAS.text(NAME_COORDS, name, font=NAME_FONT, fill=(0, 0, 0))
    CANVAS.text(CODE_CORDS, code, font=CODE_FONT, fill=(0, 0, 0))

    return template
        
def main():

    data = read_csv()

    for item in data:
        template = write_name(item['name'], item['code'])
        template.save(f"generated/{item['name']}.png")


if __name__ == "__main__":
    main()



###### Comments on how the code works

"""
The code imports the csv module to read the data from the CSV file and the PIL library to manipulate images. 
Two fonts are defined, one for the student's name and another for the code. The code defines the coordinates
where the text will be written on the certificate image.

The read_csv() function reads the CSV file and returns a list of dictionaries, 
where each dictionary contains the name and code of a student.

The write_name() function takes the name and code of a student, 
opens the certificate template image, writes the name and code at
the specified coordinates, and returns the modified template image.

The main() function calls read_csv() to get the student details,
iterates over each student, calls write_name() to generate the 
certificate image for that student, and saves the image to a file in the generated directory.
"""