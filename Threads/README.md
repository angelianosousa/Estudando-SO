# Project 01 - Learn and Working with Threads

## This project is for a subject Operational System on University State of Ceará.
<hr>
<b>Objectives:</b> learn how to use threads e apply strategies to avoid problemas with mutual exclusion and comparing the efficienci

## How i using the threads
1. Only One Thread
  * Using the thread to fill the vector and start a countage on the main thread.
2. Working with more Threads
  * The first threads is responsible to fill the vetor and the others are responsible to count numbers comparing the key of the dictionary with the value of the vector populate previously.

## About mutual exclusion (Mutex)
* Was utilized the semaphore strategies to prevent errors with index out of range
* Strategies like <b>Busy Waiting</b> and <b>Lock</b> are badly because our algorithm works looking for the len of the vector that we pass so for garantee that we don't acess a region that was not populate the strategie with semaphore is more smarter

# My Results

Running the script 30 time in the fourth cases we have:

* 01 Thread : 41.14557249546051 seconds
* 02 Threads: 
* 05 Threads: 
* 10 Threads: 

> Observations: 