# Goodreads Review Analyzer
The deployed app can be accessed in the link below.
<br />[Goodreads review analyzer](https://singarajup-goodreads-reviewanalyzer-streamlitapp-7o4daj.streamlit.app/)

## Overview
Reading books is a recreational activity. Based on the reviews for the selected book this app will show the percentage of emotions hidden behind the reviews by the customers who read the same book. 


## Background and Motivation

The reader will go through different emotions while reading a book. The feedback given as a review is based on the emotions they feel. These reviews are helpful for a user who wants to read a book as the reviews will summarize, criticize, appreciate the book. By analyzing the reviews given by different customers, we want to capture the emotions triggered while reading the book for the customers.

While there is no data for books with labels for the emotions, the approach we followed is to create a model for the labeled text data which is available from the huggingface/kaggle websites for emotions. We then applied the model to the test data obtained by using a library  Beautiful soup to parse the data from goodreads html webpage. 

## Goals
- Build a classifier that predicts the emotions from the text
- Build a web app to take the title from the user and give the percentage of emotions for the title from the reviews obtained from goodreads website

## Datasets

## Usage
Clone repo 
```bash
 git clone https://github.com/SingarajuP/goodreads-reviewanalyzer.git
```
<br />Setup a virtual environment
```bash
conda create -n yourenvname python=3.10.4
```
<br />Activate the virtual environment

```bash
conda activate yourenvname
```
<br />Install all requirements using pip:
```bash
pip install -r requirements.txt
```
<br />To run web application stay in the main directory and run the command:
```bash
uvicorn main:app --reload 
After this you get Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
open http://127.0.0.1:8000 in the browser to get the html page
open http://127.0.0.1:8000/docs in the browser to get the swagger docs web page

```



## Practical Applications

## Milestones
- Returning some of the reviews also along with the predictions in the result
- Modify the entire code using classes



## References
<br />[Multiclass text classification](https://www.analyticsvidhya.com/blog/2021/11/a-guide-to-building-an-end-to-end-multiclass-text-classification-model/) 
<br />[Finetuning BERT model](https://medium.com/mlearning-ai/fine-tuning-bert-for-tweets-classification-ft-hugging-face-8afebadd5dbf)
<br />[Setting up html app with fastapi and jinja](https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/) 


