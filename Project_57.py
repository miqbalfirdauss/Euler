{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project 57"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "153\n",
      "0.009083747863769531\n"
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
    "# p\n",
    "\n",
    "p = 1\n",
    "\n",
    "\n",
    "\n",
    "# q\n",
    "\n",
    "q = 1\n",
    "\n",
    "\n",
    "\n",
    "# counter\n",
    "\n",
    "counter = 0\n",
    "\n",
    "\n",
    "\n",
    "# 1000 iterations\n",
    "\n",
    "for i in range(1000):\n",
    "\n",
    "    a1 = p + 2*q\n",
    "\n",
    "    b1 = p + q\n",
    "\n",
    "    if len(str(a1)) > len(str(b1)):\n",
    "\n",
    "        counter += 1\n",
    "\n",
    "    p = a1\n",
    "\n",
    "    q = b1\n",
    "\n",
    "\n",
    "\n",
    "# printing the counter\n",
    "\n",
    "print (counter)\n",
    "\n",
    "\n",
    "\n",
    "# time at the end of program execution\n",
    "\n",
    "end = time.time()\n",
    "\n",
    "\n",
    "\n",
    "# total time of execution\n",
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
