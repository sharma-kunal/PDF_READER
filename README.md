# PDF Reader

A simple PDF Reader to extract Question, Options and Answers from the [PDF](https://drive.google.com/file/d/1qwkRXSwfguUSF2KSIUgbRV34t_fZjnth/view?usp=sharing) using python

# Installation

To run the project, you need to install the module PyPDF2, using the command

```
pip install PyPDF2
```

and you are good to go.

# Running

After installing `PyPDF2`, just run the project and it will crawl the PDF page by page and store the data in a dcitionary in the format,

- Chapter name
  - Type (I, II, .. ) (if any)
    - Question Number
      - Question (String)
      - Options (List of all options)
      - Answer (Answer to the Question)
---
**NOTE**

While running, after crawling each page, the code outputs the `Question Number` found on the page and the `Question Number whose answer are found on the page`. An example for the illustration is given below,

![output](https://github.com/sharma-kunal/PDF_READER/blob/master/media/output.png)

# About Me

I am 3rd year undergraduate, pursuing B.Tech from Jaypee Instte of Information Technology, Noida.

I have experince working with Python, Django, Web Scraping and Web Automation.

My Resume: https://drive.google.com/file/d/123Xp8bSoyf8VKikuxspv4Cl450m1lIYM/view?usp=sharing

My Portfolio: https://sharma-kunal.github.io/

### My Projects

#### 1. Movie/Series Search Engine

- Project Live on Heroku - https://sharma-kunal.github.io/SearchEngine/
- A Search Engine to search platform currently streaming specific movies/serie.
The platforms being searched are:
  - Netflix
  - Amazon Prime
  - Hotstar
  - Zee5
  - Sony LIV
  - MX Player
  - Airtel XStream
  and more..
- Tech Stack Used:
 - Django
 - Django REST Framework (REST API)
 - Web Crawling
 - XHR Request and AJAX
 - HTML, CSS, JS

#### 2. Sorting Visualizer

- https://github.com/sharma-kunal/Sorting-Visualiser
- A sorting visualizer made using python and matplotlib to visualize the sorting algorithms in real time
- It visualizes algorithms like
  - Insertion Sort
  - Bubble Sort
  - Selection Sort
  - Merge Sort
  - Quick Sort

For more projects and my experince, please have a look on my portfolio and resume.

Thank You
