# Feedback | Group 7

## Milestone 1

### Problem Definition | 20 points

The problem is defined correctly, and the structure is kept.

- Broad Area of Interest
- Preliminary Research
  - Current trends
  - Opportunities
- Solution with Methodology
  - Data Collection
  - Analytical Techniques
  - Implementation Plan
- Expected Outcomes
- Evaluation Metrics

<span style="color: green;">Grade: 20</span>

### Roadmap | 10 points

The roadmap seems realistic.

<span style="color: green;">Grade: 10</span>

### Administrative Tasks | 5 points

- Roles are assigned
- Preliminary discussion with me was done
- Slack channel is created
- Github Repo is created

<span style="color: green;">Grade: 5</span>

### Technical Tasks | 5 points

- Proper `.gitignore` file is available
- The Requirments.txt file is available, indicating that `venv` was created
- The first chapter of the Package Development course is done by **everyone**

<span style="color: green;">Grade: 5</span>

### Grade

Overall, you did a really great job during the M1. Keep it like that!

<span style="color: green;">Final Grade: 40/40</span>

---

# Milestone 2 | Tasks

## Product and Project Manager | 40 points


1. Name your Python package: register to [pypi](Pypi.org)
2. Install `mkdocs` package to start with the documentation
3. Database schema: Provide your product database structure (ERD)
4. Transform your project file structure according to the below tree

```bash
PythonPackageProject/ #githhub repo
├── yourpackagename/
│   ├── __init__.py
│   └── submodule1/ #database related
│       ├── __init__.py
│       └── submodule1_1.py
│   └── submodule2/ #model related
│       ├── __init__.py
│       └── submodule1_2.py
|    └── submodule3/ # api related
│       ├── __init__.py
│       └── submodule1_2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
|── example.ipynb # showing how it works
|── run.py # in order to run an API
|── docs/ #this folder we need for documentation
|── .gitignore
|── requirments.txt 
├── README.md
├── LICENSE
└── setup.py
```

## Data Scientist and Data Analyst | 20 points

1. Simulate the data if you need
2. Try to use the CRUD functionality done by DB Developer
3. Work on modeling part using simple models 
  
```python
from yourpackage.submodule2 import modelname

```

## Database Developer | 30 points

1. Create a DB and respective tables suggested by the Product Manager
2. Connect to SQL with Python
3. Push data from flat files to DB
4. Test the code provided [here](https://github.com/hovhannisyan91/DS223_SQL) and complete the missing components 
5. Add extra `methods` that you might need throughout the project:
   1. Communicate with PM and API Developer for custom functionality

```python
from yourpackage.submodule1 import sqlinteractions
```

## API Developer | 30 points

1. Communicate with DB Developer and PM in order to design the API
2. You can create dummy endpoints in the beginning, then communicate with PM as well
3. The following endpoints must be available:
   1. GET
   2. POST
   3. UPDATE

Check out this [this repo.](https://github.com/hovhannisyan91/fastapi)

```python
from yourpackage.submodule2 import api
```

---

# Milestone 2 | Feedback

- Add some description in `README.MD`, which is going to be a description on pypi
- Make sure to add minimal requirements for the `setup.py`
- I would also recommend to keep `logger` module and use it instead of `print()` function
- I removed apivenv, no need to have it in the repo, put it in gitignore

## DataCamp

Done by everyone.

## Product and Project Manager | 40 points

1. The package is <span style='color:red'>not</span> registered in Pypi or I couldn't find it
2. `mkdocs` package is <span style='color:red'>not</span> in the requirments.txt
3. The schema is provided 
4. <span style='color:orange'>Partially done</span>:
   1.  Note: you need to provide the references in the `__init__.py` files
   2.  Call `generate_data` externally.
   3.  From project's point of you there is no difference how to insert the **simulated data** into SQL, however I'd recommend first generate csv files (let's say in data folder: out of the package), then insert it into db. From application point of you that makes sense ans the potential user of your package is going to provide either csv/flat file or db connection string.

<span style='color:green'>Grade: 40/40</span>

## Data Scientist and Data Analyst | 20 points

- The data was successfully simulated/ingested
- modeling module was initiated and tested properly 


<span style='color:green'>Grade 20/20</span>

## Database Developer | 30 points

- DB and schema was successfully implemented
- Connection between SQL and Python is available
- The Data is loaded
- Custom functions are available in `db_interactions.py` file

<span style='color:green'>Grade: 30/30</span>


## API Developer | 30 Points

- `run.py` is working properly
- Requests:
  - POST request is available 
  - GET request is  available
  - PUT(update) request is not available

<span style='color:green'>Grade: 30/30 Good Job!</span>


<span style='color:green'>M2 Grade: 120/120</span>

---

# Milestone 3 | Tasks

## Remaining tasks from M2

- fix `__init__.py` files

## DataCamp

Complete the third chapter. 

## Product and Project Manager | 30 points

1. Design the final endpoints:

  - the outputs you need for modeling
  - the outputs you need to analyze the study
  
2. Communicate the outputs with the team in order to help them create/modify final classes/methods, etc.

  - design query functions according to your needs
  - design modeling components according to your needs
  
3. Create sample documentation using [mkdocs](https://www.youtube.com/watch?v=Q-YA_dA8C20&ab_channel=JamesWillett). Once you have the final version of a package, you'll update it. For now, push to GitHub the following:
    - a selected template
    - index.md page1 and page2 with dummy content (though you are free to provide actual documentation as well)
    
## Data Scientist and Data Analyst | 30 points

- Create a model based on the Product Manager's requirements (or improve the existing file and ingest the output to DB)
- Insert the outcome into the respective SQL folder. (communicate with the Product Manager and DB developer in case you need extra table and/or functionality)
- Data Analyst must try to:
  -  interpret the model 
  -  create custom visualizations
  -  suggest/support Product Manager to make decisions about product's final design


## Database Developer | 30 points

- Based on the new/updated requirements, provide functionality in order to interact with the DB
  - API developer might need customer functionality for the final endpoints
  - Data Scientist/Analyst developer 


## API Developer | 30 Points

- make your requests directly from the Database (you have this!) and update based on Product Manager's request
- Note: you can make endpoints to test the data as well `get_something().` (you have this!)