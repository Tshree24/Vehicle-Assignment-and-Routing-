# Vehicle-Assignment-and-Routing-
Automating and Optimizing manager's task of allotting and planning schedule/time-table for service providers.

## Problem Statement
The task is to attempt finding a way that could automate your (Service Manager's) manual work of creating a plan for Technicians. Also, the solution should consider how to handle the scenarios of callouts and emergencies.

## Solution
Automating the given task can be divided into two following steps:
1. Firstly assigning which technician will visit which customers and how many (say for a particular day)
2. Then the next job is to choose the most optimal route taken by the technician to minimize cost.
 In our case the cost can be: reducing time to reach the cutomers and completing all the visits in the given time frame.
 As provided in the document that the the opening hours for the buildings are between 07.00 am to 04.00 pm. and a visit takes about 60 minutes. So the technician will have to   cover all the visit all the place and provide maintaince within the timed window.
 
I am using Google OR tools to perform the above tasks.

## Data Used
I have used the sample data provided for <a href="https://drive.google.com/file/d/1nGQHCBZ7U3QKyr0X8jnpekZiVrtMIwhV/view">Mainteny Elevator services</a>
This data consits of customer details and the last visit made. The latest last visit date is what we need to use to plan for next month. 
On performing initial analysis on the given data, we observe that the number of cutomers visited in latest last month are 100. 
Let us assume that we have to visit 12 customers in one day and we have 3 technician available that day. 

## Automating Assignment 
The assignment is easy and can be done randomly when all technician are considered equal and their cost for providing services is same.
Howwever, this can change depending on their time in the organization. Their cost can vary by either the distance they have to travel to reach the cutomer or by the importance if task they are doing or by experience etc. 

As it is stated that these tasks are related to mandatory monthly checkup, let us assume that technician's are given same cost for a set of distances. Now, in case of emergency, depending on the task, their cost can differ. 
More assumptions:
each technician has to visit 4 cutomers 
each technician should travel more or less the same distance

## Vehicle Routing Problem
In this task, the technicians have to visit the cutomers in a time constrain. So, we have to add a time window constains for reaching each location and assuming that the job takes 60 min of time. 
As, the buildings are open between 07.00 am to 04.00 pm, i am assuming that they can visit these places anytime between the given time window.
For this task, we will need to get a time matrix which will comprise of the duration required to travel between the respective locations. The google distance matrix api provides both distance and time between locations, so we can use time in this case. 

The address need to be preprocessed in a certain manner in order to request the api data. 



