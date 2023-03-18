# WebAccess Backend

WebAccess is a webapp with two tools to help web developers create more accessible content. The first tool is an automatic web accessibility evaluator, which allows the evaluation of HTML code by inserting the URL of a web page or the HTML code itself, applying up to 11 techniques proposed by the WCAG in its version 2.1. On the other hand, the second tool is a contrast evaluator, which allows knowing if the contrast ratio between two colors (text and background) meets any of the levels established by the WCAG.

&nbsp;

## Links

- [Repo](https://github.com/JoanR99/web-access-server-fastapi 'WebAccess Backend repo')
- [Frontend](https://github.com/JoanR99/web-access-client 'WebAccess Frontend repo')
- [Live Demo](https://github.com/JoanR99/web-access-client 'Live View')

&nbsp;

## Screenshots

![Home Page](/screenshots/web-access.png 'Home Page')

![Evaluation Page](/screenshots/wa-3.png 'Evaluation Page')

![Results Page](/screenshots/wa-4.png 'Results Page')

![Contrast Page](/screenshots/wa-5.png 'Contrast Page')

&nbsp;

## About

This REST Api allows the user to evaluate the accessibility of their websites, exposing a route to evaluate through URL and another to evaluate through HTML code. Eleven WCAG techniques are applied to the html code during an evaluation, returning the number of elements evaluated and errors found, if any.

&nbsp;

## Stack

![Python] ![Fastapi]

This repository contains the third backend version of WebAccess, developed with Python and Fastapi framework, in addition to a library called BeautifulSoup. I decided to build this version with Python because I wanted to improve my skills regardless this language and because Python is one of the most used programming languages to do web scrapping. Also, I choose Fastapi because this is a simple REST Api and use something like Django may be overkill.

&nbsp;

## How to install and run

### Prerequisites

1. You need to have Python installed in your machine

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/JoanR99/web-access-server-fastapi.git
   ```

2. Go to file

   ```sh
   cd web-access-server-fastapi
   ```

3. Create virtual environment

   ```sh
   python3 -m venv env
   ```

4. Activate environment

- On Unix or MacOS, using the bash shell:

  ```sh
  source env/bin/activate
  ```

- On Windows using PowerShell:

  ```sh
  env\Scripts\Scripts\Activate
  ```

5. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

6. Start server. You can choose the port you prefer.

   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   &nbsp;

## Author

**Joan Romero**

- [Profile](https://github.com/JoanR99 'Github Joan Romero')
- [Email](mailto:romerojoan1999@gmail.com?subject=Hi 'Hi!')
- [Linkedin](https://www.linkedin.com/in/joanr99/ 'Linkedin Joan Romero')
- [Portfolio](https://portfolio-joan-romero.vercel.app/ 'Portfolio Joan Romero')

[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[fastapi]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
