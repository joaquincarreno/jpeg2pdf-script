# jpeg2pdf-script
A python script that joins all the images of all the folders in a specific directory in a pdf file using jpeg2pdf. This was made to join Manga/Comic scans into a pdf with the full volume.

## Usage

In order for this simple script to work you have to make sure you have a directory which child directories only have .jpeg or .jpg files that you want to join in a pdf file.

If you care about the order, just double check that the directories are in alphabetical order and the files in them also are in alphabetical order.

To successfully  join the files you have to have both the script and jpeg2pdf in the root directory together with the folder containing the files.

To run the script you will have to execute the following command in the command line:

`python script.py file-name`

This command will make a file named `file-name.pdf`

## Example

To illustrate what is write above here is an example:

```
Root folder
│   script.py
│   jpeg2pdf.txt    
│
└───f1
│   │   0.jpg
│   │   1.jpg
│   │
│   
└───f2
    │   a.jpeg
    │   b.jpeg
```

Running the command specified above will result in a pdf file with 4 images in the following order:

1.   0.jpg
2.   1.jpg
3.   a.jpeg
4.   b.jpeg

Hope that makes it clear.
