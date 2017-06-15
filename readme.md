Introduction
================

This is a solution to the coding challenge as indicated in the wiki.

Setup
============

```
pip install -r requirements.txt
```

Running Unit Tests
==================

This will test the solution against the values form the api.

```
cd ./src
python -m unittest unit_tests
```

To determine the accuracy of the calculate function, I exported the https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json to and excel file on the ./data folder.


Constraints
=============

The question required the application to return the following

- The number of water points that are functional,
- The number of water points per community,
- The rank for each community by the percentage of broken water points.

and the expected results was

```
{
  "number_functional": 50,
  "communityA": {
    "number_functional": 8,
    "ranking": 1,
  },
  "communityB": {
    "number_functional": 6,
    "ranking": 2,
  },
  ...
}
```

As you can see the, data structure shown does not indicate total number per community. I had to include it anyway because it was part of the question. The output is a s follows

![Results](/img/results_json.png)