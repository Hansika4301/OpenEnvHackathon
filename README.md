---
title: OpenEnv Task Scheduler
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# OpenEnv Task Scheduler Environment

This project implements a real-world task scheduling environment using the OpenEnv framework. An AI agent interacts with the environment to schedule tasks based on deadlines, duration, and priority.

## Environment Overview

The environment provides three core methods:

- `reset()` initializes the environment with a new set of tasks  
- `step(action)` allows the agent to select a task  
- `state()` returns the current state of tasks  

## Action Space

Discrete action space:
- The agent selects a task ID from the available tasks

## Observation Space

The environment returns:
- A list of tasks, where each task contains:
  - id
  - deadline
  - duration
  - priority
- Current step count

## Tasks

The environment includes three levels of difficulty:

- Easy: Few tasks with flexible deadlines  
- Medium: Moderate number of tasks with tighter deadlines and mixed priorities  
- Hard: Larger number of tasks with strict deadlines and priority conflicts  

## Reward Function

The reward is calculated as follows:

- +1.0 if a task is completed within its deadline  
- +0.1 multiplied by task priority as a bonus  
- -0.2 penalty if the task misses its deadline  
- Final reward is clipped between 0.0 and 1.0  

## Grading

The grader evaluates performance based on total accumulated reward and normalizes it between 0.0 and 1.0.

## How to Run

Run the inference script:

```bash
python inference.py