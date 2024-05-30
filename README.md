# Table-From-Image-DL (Work-In-Progress)

## Introduction
Imagine you're trying to scrape data from a website and all their tables are in images. What do you do then? A quick search online you can pay $2 per 50 images to turn your images into tables. Well, some of us are trying to scrape a lot of data and aren't willing to spend that much. Also, that seems like the easiest ML problem ever. First there's no need to adjust colors since the tables are in B&W, the words are nicely spaced and there's no glare or anything to adjust. 


## Basic structure

### What is CNN?



## Workflows

1. Update config.yaml with the path to the image you want to convert to a table
2. Update secrets.yaml 
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Add app.py

## How to run?

### STEPS:

1. Clone the repository

```bash
git clone https://github.com/luizamfsantos/Table-From-Image-DL-MLflow-DVC
```

2. Create a virtual environment

```bash
python3 -m venv tbldtc
```
or 
```bash
conda create -n tbldtc python=3.12 -y
```

3. Activate the virtual environment

```bash
source tbldtc/bin/activate
```
or 
```bash
conda activate tbldtc
```

4. Install the requirements

```bash
pip install -r requirements.txt
```