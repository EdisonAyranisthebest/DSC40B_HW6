{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f1c200fc-7b0e-4b64-bc8f-1f8362e9a584",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import deque\n",
    "\n",
    "def assign_good_and_evil(graph):\n",
    "    color = {}\n",
    "\n",
    "    def bfs(start):\n",
    "        color[start] = True\n",
    "        q = deque([start])\n",
    "        while q:\n",
    "            u = q.popleft()\n",
    "            for v in graph.neighbors(u):\n",
    "                if v not in color:\n",
    "                    color[v] = not color[u]\n",
    "                    q.append(v)\n",
    "                elif color[v] == color[u]:\n",
    "                    return False\n",
    "        return True\n",
    "\n",
    "    for node in graph.nodes:\n",
    "        if node not in color:\n",
    "            if not bfs(node):\n",
    "                return None\n",
    "\n",
    "    return {node: ('good' if color[node] else 'evil') for node in color}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5848bb65-d65f-429a-815b-17dfaa7b6442",
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
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
