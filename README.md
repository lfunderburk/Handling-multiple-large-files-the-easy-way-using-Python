# Handling multiple large files the easy way using Python
##### Workshop facilitator: Laura Gutierrez Funderburk | Department of Mathematics | Simon Fraser University

##### Workshop date: April 24 2018

## Abstract

In this repository, I will walk through a series of exercises whose purpose is to make the process of handling multiuple files easier via the use of Python dictionaries, tables and comprehension lists. I will provide examples, files and a series of commands for participants to explore. Throughout this workhop and for pedagogical purposes, I will be using Jupyter notebooks. 

## Prep

### Important: 

If you have an SFU login account, you can skip installing Python and simply access one of [SFU's Jupyter servers](https://sfu.syzygy.ca/)

### Otherwise...

Ensure you have installed Python on your local computer. Throughout these exercises, I will be using Python 3.6. One of the easiest ways to install Python on your local computer is by downloading and installing [Anaconda](https://www.anaconda.com/download/#linux). I strongly recommend installing Anaconda as it includes Jupyter Notebooks, Pandas and other scientific packages that will be used throughout this workshop. 

### Documentation

[Installing Anaconda](https://docs.anaconda.com/anaconda/install/#detailed-installation-information)

[Installing Jupyter](http://jupyter.org/install)

## Introduction

Imagine your job is to extract specific information from a file A with over 600 entries. Such information acts as an identifier. Your job is to use the identifiers from file A to extract coordinates and key words from file B. What is the catch? File B has thousands of entries and the coordinates and keywords in each entry act as another identifier. You will use the identifiers found on file B to extract specific subsets of data from at least a dozen of other files (some with hundreds or thousands of lines). Once you get the data, your job is to run open source software and generate results. Once you get results, you clean the output and plot your findings. 

In this workshop I will take a subset of a dataset I have been working on and share how tabulating data, using comprehension lists, dictionaries and dataframes made my work a lot easier. Although the scope of this project calls for more, I will only focus on the aspects that involved using these tools. 

## Exercises

In this section I will provide a short description of each exercise. All exercises are inclucded in the repository. You can find a direct link to each in this list. 

### Exercise 0: <a href="https://github.com/lfunderburk/Handling-multiple-large-files-the-easy-way-using-Python/blob/master/EXERCISES/Exercise_0_Basic_Tools_For_This_Workshop.ipynb" target="_blank">Basic Tools for this Workshop</a>

### Exercise 1: <a href="https://github.com/lfunderburk/Handling-multiple-large-files-the-easy-way-using-Python/blob/master/EXERCISES/Exercise_1_Comprehension_Lists.ipynb" target="_blank">Comprehension Lists</a>

### Exercise 2: <a href="https://github.com/lfunderburk/Handling-multiple-large-files-the-easy-way-using-Python/blob/master/EXERCISES/Exercise_2_Dictionaries.ipynb" target="_blank">Dictionaries</a>

### Exercise 3: <a href="https://github.com/lfunderburk/Handling-multiple-large-files-the-easy-way-using-Python/blob/master/EXERCISES/Exercise_3_Introduction_to_Dataframes.ipynb" target="_blank">Introduction to Dataframes</a>

### Exercise 4: [Bringing it all together]()

### Bonus: [From Jupyter Notebook to scripting]()


