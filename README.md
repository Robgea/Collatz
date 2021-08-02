#Just screwing around with the Collatz Conjecture and code efficiency.# Collatz


The goal of this is to create a program that runs through the Collatz conjecture and *only* searches numbers that have not appeared in previous runs of the program.

So, for instance, the program should run sequentially:

- 1 (Stopping immediately)
- 2 -> 1 
- 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2, halting there because it already had 2 in the system.
- then the program will skip 4 and 5 because they have already been encountered in previous hunts.


Updated program now ignores numbers that are 2x a previously searched number that has not otherwise been encountered because that will be a one-step equation. 

Goals:

Index every number found in order of finding, and make the search function more efficient.

Notes:

First run takes 8 minutes and 52 seconds.
Eliminating 2X searched numbers reduces this to 6 minutes 38 seconds.
