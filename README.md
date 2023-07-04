# Fitness-tracker 🏀

Python

It is a fitness-tracker module in Python.

This module consists of different kinds of trainings:
- Running 🏃
- SportsWalking 🚶
- Swimming 🏊
Base class 'Training' includes a methods for counting distance, mean speed and then returns a message about the training.
Every kind of training has its own methods for countaing spent calories and mean speed with speacial formulas.
Module reads training data, checks if the training is in the available workouts types and then return a message about the training results.
Information in the message:
- training type,
- duration,
- distance,
- speed,
- calories.

# Instructions for working with the project

## Clone this repository to your PC

``` git@github.com:anastaciakaz/fitness_tracker_module.git ```

## Open the repository in your IDE and in terminal create and activate virtual environment:

### For Windows

``` python -m venv venv ```

``` source venv/Scripts/activate ```


### For MacOS

``` python3 -m venv venv ```

``` source venv/bin/activate ```

## Install requirements

``` pip install -r requirements.txt ```


