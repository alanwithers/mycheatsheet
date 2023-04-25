{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f7a3d8f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 p\n",
      "2 p\n",
      "abble\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def alt_str(str,index=-1,existing_char='',new_char='',no_of_replacements=2):\n",
    "    new_str=''\n",
    "    for i,ch in enumerate(str):\n",
    "        if i==index:\n",
    "            new_str+=new_char\n",
    "            continue\n",
    "        elif ch==existing_char:\n",
    "            new_str+=new_char\n",
    "            print(i,ch)\n",
    "            if no_of_replacements==1:\n",
    "                existing_char=''\n",
    "            continue\n",
    "        new_str+=ch   \n",
    "    return new_str\n",
    "        \n",
    "    #return str,index,char\n",
    "print(alt_str('apple',-1,'p','b'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa997c69",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
