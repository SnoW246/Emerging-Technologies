# Emerging Technologies
Emerging Technologies module is part of my [B.Sc. (Hons) in Software Development](https://www.gmit.ie/software-development/bachelor-science-honours-software-development) studies at [Galway-Mayo Institute of Technology](http://www.gmit.ie/)

This repository consists of set of solutions to [Python](https://www.python.org/doc/essays/blurb/) and [Jupiter Notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) problem sheets which can all be found in the following sub-folders of the repository:
  1. [Python-Fundamentals](https://github.com/SnoW246/Emerging-Technologies/tree/master/Python-Fundamentals)
  2. [MINST Data Sets](https://github.com/SnoW246/Emerging-Technologies/tree/master/MINST%20Data%20Sets)
  3. [Jupyter, Numpy & Pyplot](https://github.com/SnoW246/Emerging-Technologies/tree/master/Jupyter%2C%20Numpy%20%26%20Pyplot)
  4. [Tensorflow](https://github.com/SnoW246/Emerging-Technologies/tree/master/Tensorflow)

## What is Emerging Technologies Module?
It is a subject to introduce new and emerging technologies in computing. Technologies such as new programming languages, new types of data structures, new types of software infrastructure, and new communications protocols.

## What are it's learning outcomes?
This module is designed to allow individuals to be able to do the following:
* Quickly adapt to new programming languages and styles.
* Discuss and explain proposed new web technology standards.
* Identify new types of applications that can be developed using newly available data infrastructures.
* Utilise new systems and frameworks to analyse data.

## Emerging Technologies is to bring in dept understanding in the following fields:
### 1. Programming languages
  * Comparison of current industry-standard programming languages.
  * Consideration of emerging programming languages and their goals.
  * Quickly learning new programming languages.
  * Programming language selection. 
### 2. Data analysis
  * Comparison of current data analytics infrastructures.
  * Consideration of emerging data analytics infrastructures.
  * Refactoring of data.
### 3. Emerging standards
  * Review of existing web standards and protocols.
  * Introduction to emerging web standards and protocols.
  
Description of Emerging Technology Module was adapted from [here](https://emerging-technologies.github.io/).

Each problem sheet was given to me by [lecturer/instructor](https://ianmcloughlin.github.io/) of this module. The original problem sheet questions can be found in the following links:
  1. [Python-Fundamentals](https://emerging-technologies.github.io/problems/python-fundamentals.html)
  2. [MINST Data Sets](https://emerging-technologies.github.io/problems/mnist.html)
  3. [Jupyter, Numpy & Pyplot](https://emerging-technologies.github.io/problems/jupyter.html)
  4. [Tensorflow](https://emerging-technologies.github.io/problems/tensorflow.html)
  
# How to get started
## 1. Downloading necessary software (Latest Technologies)
  * [Python 3.6.3](https://www.python.org/downloads/)
  * [Python Anaconda](https://www.anaconda.com/download/)
  * [Cmder](http://cmder.net/) or any other command-line/console emulator 
  
  **NOTE** Console emulator is not mandatory since every Operating System already have one, so user can use that instead. I suggested Cmder because I prefer it over every other emulator because it is simply easier to visualise everything.
  When the files are downloaded, install each individual one. 
  **NOTE** If the Python 3.6.3 instalation gives you option to add it to the path variables, by all means tick the box to make your life easier.
## 2. Setting up the environments
  * Open up Cmder/console emulator on your operating system and check if your python has been installed correctly by using `Python` command

The above command shoulf display the following or similar in your console emulator: 

`Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32`

`Type "help", "copyright", "credits" or "license" for more information.`

It basically displays the version of the python that you are running on your machine. However in the case that console emulator will not pick up `Python` command, the file path of Python isntalation will need to be added. For that you will need to do the following:
  * Navigate to control panel of your operating system.
  * Look for advanced System Settings.
  * Furthermore, direct to Environment Variables...
  * In that section add Python execitables into the path of your Operating System so it can be recognised as local command while using console emulator.
  
The further information and instructions on how to do that can be found [here](https://docs.python.org/3/using/windows.html).

## 3. Installation of further modulules
  Once all of the above instructions are followed and the environment is set up correctly, in the Cmder/console emulator type in the following command:
  * `pip3 install numpy` command will download and automatically isntall [NumPy](https://docs.scipy.org/doc/numpy-1.13.0/reference/) Module necessary for us to deal with numbers.
  
  Once NumPy Module is installed launch Anaconda Prompt which will open up another version of console emulator but this time only for Anaconda Python itself. In that console type the following commands:
  * `conda install tensorflow` will download and install [Tensorflow](https://www.tensorflow.org/api_docs/) Module which is necessary for machine learning.
  * `conda install keras` will also download and install, this time [Keras](https://keras.io/getting-started/functional-api-guide/) Module which is extension module for Tensorflow allowing us to deal with machine learning with less amount of code/work which is always good if we need to save time.
  
