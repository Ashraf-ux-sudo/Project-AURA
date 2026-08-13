# Student Manager V2

## Overview

Student Manager V2 is an improved version of the original Student Manager.

The purpose of this version is to create a structured system that can store and manage a student's academic information and provide the foundation for Project AURA.

## Features

### Student Management
- Stores student name and grade.
- Manages subjects, tasks, schedules, and test records.

### Subject Management
Each subject stores:
- Subject name
- Completed topics
- Current topic
- Next topic
- Topic mastery

### Task Management
Each task stores:
- Subject
- Topic
- Description
- Deadline
- Priority
- Completion status

### Schedule Management
Each schedule item stores:
- Day
- Start time
- End time
- Activity
- Subject
- Topic

### Test Records
Each test record stores:
- Subject
- Test name
- Marks obtained
- Maximum marks
- Automatically calculated percentage

## Object-Oriented Design

Student Manager V2 uses Python Object-Oriented Programming.

The main classes are:

- `Student`
- `Subject`
- `Task`
- `ScheduleItem`
- `TestRecord`

Tasks, schedules, and test records can reference the same `Subject` object instead of storing the subject name separately.

This creates a connected data structure that can later be accessed by Project AURA.

## Example Architecture

Student
├── Subjects
├── Tasks
├── Schedule
└── Test Records

Subject
├── Completed Topics
├── Current Topic
├── Next Topic
└── Mastery

## Current Status

Student Manager V2 core architecture is complete.

The project currently focuses on data storage and organization.

## Future Development

Student Manager will eventually act as the data layer for Project AURA.

AURA will be responsible for analyzing this information and making intelligent recommendations based on the student's goals, progress, tasks, schedule, and test performance.