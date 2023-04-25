{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c18f13a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#this function parses from between any pair of characters,and if char is the same parses to end or next occurance\n",
    "def parse_comp_pair(str,start_ch,stop_ch):\n",
    "    parsed_out=''\n",
    "    flag=False\n",
    "    for i,ch in enumerate(str):\n",
    "        if ch==start_ch:\n",
    "            flag=True\n",
    "            index=i+1\n",
    "            continue\n",
    "        if flag==True and i==index and ch!=stop_ch:\n",
    "            index+=1\n",
    "            parsed_out+=ch\n",
    "    return parsed_out\n",
    "#print(parse_comp_pair('abc<hello you>def','<','>'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49155eed",
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
