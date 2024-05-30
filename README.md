# Table-From-Image-DL (Work-In-Progress)

## Introduction
Imagine you're trying to scrape data from a website and all their tables are in images. What do you do then? A quick search online you can pay $2 per 50 images to turn your images into tables. Well, some of us are trying to scrape a lot of data and aren't willing to spend that much. Also, that seems like the easiest ML problem ever. First there's no need to adjust colors since the tables are in B&W, the words are nicely spaced and there's no glare or anything to adjust. 


## Basic structure

### What is CNN?



## How to run?

### STEPS:

1. Clone the repository

```bash
git clone https://github.com/luizamfsantos/Table-From-Image-DL-MLflow-DVC
```

2. Create a virtual environment

```bash
python3 -m venv cnncls
```
or 
```bash
conda create -n cnncls python=3.12 -y
```

3. Activate the virtual environment

```bash
source cnncls/bin/activate
```
or 
```bash
conda activate cnncls
```

4. Install the requirements

```bash
pip install -r requirements.txt
```