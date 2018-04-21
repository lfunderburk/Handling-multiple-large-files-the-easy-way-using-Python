# Handling multiple large files the easy way using Python
###### Workshop facilitator: Laura Gutierrez Funderburk | Department of Mathematics | Simon Fraser University

###### Workshop date: April 24 2018

## Abstract

In this repository, I will walk through a series of exercises whose purpose is to make the process of handling multiuple files easier via the use of Python dictionaries, tables and comprehension lists. I will provide examples, files and a series of commands for participants to explore. Throughout this workhop and for pedagogical purposes, I will be using Jupyter notebooks. 

## Prep

### IMPORTANT: 

If you have an SFU login account, you can skip installing Python and simply access one of [SFU's Jupyter servers](https://sfu.syzygy.ca/)

### Otherwise...

Ensure you have installed Python on your local computer. Throughout these exercises, I will be using Python 3.6. One of the easiest ways to install Python on your local computer is by downloading and installing [Anaconda](https://www.anaconda.com/download/#linux). I strongly recommend installing Anaconda as it includes Jupyter Notebooks, Pandas and other scientific packages that will be used throughout this workshop. 

### Documentation

[Installing Anaconda](https://docs.anaconda.com/anaconda/install/#detailed-installation-information)

[Installing Jupyter](http://jupyter.org/install)

## Introduction

Imagine your job is to extract specifict information from a file A with over 600 entries. Such information acts as an identifier. Each identifier is then used to extract information from a file B containing thousands of entries. Once this is done your job is now to use the identifiers from file A to extract coordinates and key words from file B. What is the catch?  The job does not end here. We will use the information found on file B to extract very specific subsets of data from at least a dozen of other files (some with hundreds if not thousands of lines). 

We plan to run open source software on this data and generate results. Once we get results, we then want to clean the output and plot our findings. 

In this workshop I will divide the tasks at hand and provide some of the tools I have found useful while parsing large multiple files. 

## Exercises

In this section I will provide a short description of each exercise. All exercises are inclucded in the repository. You can find a direct link to each in this list. 

### Exercise 0: [Basic Tools for this Workshop](https://github.com/lfunderburk/Handling-multiple-large-files-the-easy-way-using-Python/blob/master/EXERCISES/Exercise_0_Basic_Tools_For_This_Workshop.ipynb)

### Exercise 1: [Comprehension Lists](https://github.com/lfunderburk/Handling-multiple-large-files-the-easy-way-using-Python/blob/master/EXERCISES/Exercise_1_Comprehension_Lists.ipynb)

### Exercise 2: [Dictionaries]()

### Exercise 3: [Dataframes]()

### Exercise 4: [From Jupyter Notebook to scripting]()

### Exercise 5: [Bringing it all together]()
