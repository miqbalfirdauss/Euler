{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project 56"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "972\n",
      "0.5237793922424316\n"
     ]
    }
   ],
   "source": [
    "# time module\n",
    "\n",
    "import time\n",
    "\n",
    "\n",
    "\n",
    "# time at the start of program execution\n",
    "\n",
    "start = time.time()\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def sum_of_digits(n):\n",
    "\n",
    "    \"\"\"sum of digits of given number\"\"\"\n",
    "\n",
    "    sod = 0\n",
    "\n",
    "    while n != 0:\n",
    "\n",
    "        sod += n % 10\n",
    "\n",
    "        n //= 10\n",
    "\n",
    "    return sod\n",
    "\n",
    "\n",
    "\n",
    "# largest sum of digits\n",
    "\n",
    "largest = 0\n",
    "\n",
    "\n",
    "\n",
    "# for loop to get a and b\n",
    "\n",
    "for a in range(0, 100):\n",
    "\n",
    "    for b in range(0, 100):\n",
    "\n",
    "        sod = sum_of_digits(a**b)\n",
    "\n",
    "        if sod > largest:\n",
    "\n",
    "            largest = sod\n",
    "\n",
    "\n",
    "\n",
    "# printing the largest sum of digits\n",
    "\n",
    "print (largest)\n",
    "\n",
    "\n",
    "\n",
    "# time at the end of program execution\n",
    "\n",
    "end = time.time()\n",
    "\n",
    "\n",
    "\n",
    "# total time for execution\n",
    "\n",
    "print (end - start)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
