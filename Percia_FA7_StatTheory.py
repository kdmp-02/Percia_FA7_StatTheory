{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e089bf84-32b2-4d06-bf07-99142f1d5bc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Participant</th>\n",
       "      <th>Cloak</th>\n",
       "      <th>Mischief</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>13</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>14</td>\n",
       "      <td>1</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>16</td>\n",
       "      <td>1</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>17</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>22</td>\n",
       "      <td>1</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>23</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>24</td>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Participant  Cloak  Mischief\n",
       "0             1      0         5\n",
       "1             2      1         9\n",
       "2             3      0         7\n",
       "3             4      1        10\n",
       "4             5      0         6\n",
       "5             6      1        11\n",
       "6             7      0         6\n",
       "7             8      1        12\n",
       "8             9      0         5\n",
       "9            10      1        10\n",
       "10           11      0         7\n",
       "11           12      1        11\n",
       "12           13      0         5\n",
       "13           14      1        12\n",
       "14           15      0         6\n",
       "15           16      1        13\n",
       "16           17      0         4\n",
       "17           18      1        10\n",
       "18           19      0         6\n",
       "19           20      1         9\n",
       "20           21      0         5\n",
       "21           22      1        12\n",
       "22           23      0         6\n",
       "23           24      1        11"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Participant\": list(range(1, 24+1)), \n",
    "    \"Cloak\": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  \n",
    "    \"Mischief\": [5, 9, 7, 10, 6, 11, 6, 12, 5, 10, 7, 11, 5, 12, 6, 13, 4, 10, 6, 9, 5, 12, 6, 11]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d45a9331-a5c8-4218-b29e-3a86526e3867",
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.stats as stats\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "132a3bef-b4a9-4f62-8af7-73c083d2f42a",
   "metadata": {},
   "source": [
    "### Assumptions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4428b091-3552-4874-a22f-ece10373bbd6",
   "metadata": {},
   "source": [
    "Assumption 1: The dependent variable (Mischief) is measured on a continuous scale.\n",
    "No additional code required, as the Mischief variable is already continuous."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ec13665-4f10-4592-a5ad-dcdddbf9c48d",
   "metadata": {},
   "source": [
    "Assumption 2: The independent variable (Cloak) consists of two independent groups.\n",
    "\n",
    "Group 0: Without Cloak, Group 1: With Cloak\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "20c7c6d9-abd9-479e-8421-3aeaa581ea14",
   "metadata": {},
   "outputs": [],
   "source": [
    "group_no_cloak = df[df['Cloak'] == 0]['Mischief']\n",
    "group_cloak = df[df['Cloak'] == 1]['Mischief']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84df6d3d-9570-4810-b7ea-67c957140010",
   "metadata": {},
   "source": [
    "Assumption 3: Random sampling from the population.\n",
    "\n",
    "We assume random sampling."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "290a5ab4-f8e8-475b-a4c7-68077bfed3d8",
   "metadata": {},
   "source": [
    "Assumption 4: Homogeneity of variances (Levene's Test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e48e5a6b-f721-4000-b48a-d78ae69b6100",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Levene's Test for equality of variances: p-value = 0.2534958132161763\n"
     ]
    }
   ],
   "source": [
    "levene_test = stats.levene(group_no_cloak, group_cloak)\n",
    "print(f\"Levene's Test for equality of variances: p-value = {levene_test.pvalue}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6bb4c647-b886-446f-b329-981742de4064",
   "metadata": {},
   "source": [
    "Assumption 5: The dependent variable is approximately normally distributed (Shapiro-Wilk Test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "184c7282-9ed7-4d4f-8f39-99c695dae76b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shapiro-Wilk Test for No Cloak group: p-value = 0.15990817831809984\n",
      "Shapiro-Wilk Test for Cloak group: p-value = 0.44934886234911725\n"
     ]
    }
   ],
   "source": [
    "shapiro_no_cloak = stats.shapiro(group_no_cloak)\n",
    "shapiro_cloak = stats.shapiro(group_cloak)\n",
    "\n",
    "print(f\"Shapiro-Wilk Test for No Cloak group: p-value = {shapiro_no_cloak.pvalue}\")\n",
    "print(f\"Shapiro-Wilk Test for Cloak group: p-value = {shapiro_cloak.pvalue}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e5e0a39-292c-43ae-81a3-9ea6a6bb75ea",
   "metadata": {},
   "source": [
    "#### Visualization of the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "06b73e6f-626b-4f3a-b8aa-93e2d2a83bf3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0EAAAIhCAYAAACIfrE3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABzTElEQVR4nO3dd3gU9cLF8bPphYQEEkIiSei9hI4BpIs0AenSwXbFgqhXxRcFVBCuIveqIHopIgqI0hRFQZpIkSI9NCmhk9AC6cnO+8deojGAEJJMkvl+nmefzM7O7JzdLCEnM/Mbm2EYhgAAAADAIpzMDgAAAAAAeYkSBAAAAMBSKEEAAAAALIUSBAAAAMBSKEEAAAAALIUSBAAAAMBSKEEAAAAALIUSBAAAAMBSKEEAAAAALIUSBKBAmjVrlmw2W8bNw8NDJUuWVIsWLTR+/HidP38+yzqjR4+WzWa7o+0kJCRo9OjRWrNmzR2td6NtlS5dWh07dryj5/k7X3zxhSZPnnzDx2w2m0aPHp2j28tpP/30k+rVqydvb2/ZbDYtXrz4hssdO3Ys43t9s9c0ZMiQjGX+rHnz5mrevHnOBpe0Zs0a2Ww2ffXVV3+77KBBg1S6dOkcz5Df7d69WzabTa6urjpz5ky2n2fcuHE3/WwAQHZQggAUaDNnztTGjRu1YsUKffjhh4qIiNCECRNUpUoVrVy5MtOyjzzyiDZu3HhHz5+QkKAxY8bccQnKzray41YlaOPGjXrkkUdyPUN2GYahnj17ytXVVUuXLtXGjRvVrFmzW67j4+OjWbNmyW63Z5p/7do1LViwQL6+vlnWmTJliqZMmZKj2e/UqFGjtGjRIlMzmOG///2vJCktLU2zZ8/O9vNQggDkNEoQgAKtevXqatSokZo2bapu3brpvffe065du+Tt7a2HHnpI586dy1i2VKlSatSoUa7mSUhIyLNt/Z1GjRqpVKlSpma4ldOnT+vixYvq2rWrWrVqpUaNGsnf3/+W6/Tq1UvHjx/XTz/9lGn+/PnzlZ6ergcffDDLOlWrVlXVqlVzNPudKleunGrXrm1qhryWnJyszz//XLVq1dI999yjGTNmmB0JADJQggAUOmFhYXr33Xd19epVTZs2LWP+jQ5RW7VqlZo3b67ixYvL09NTYWFh6tatmxISEnTs2DEFBgZKksaMGZNxqNWgQYMyPd/27dvVvXt3+fv7q1y5cjfd1nWLFi1SzZo15eHhobJly+o///lPpsevH+p37NixTPOvH351fa9U8+bNtWzZMh0/fjzToYHX3ejQsT179qhz587y9/eXh4eHIiIi9Omnn95wO3PnztWrr76qkJAQ+fr6qnXr1jpw4MDN3/g/Wb9+vVq1aiUfHx95eXkpMjJSy5Yty3h89OjRGQXtpZdeks1mu63DxSpVqqTIyMgsv1DPmDFDDz30kIoWLZplnRsdDjd16lTVqlVLRYoUkY+PjypXrqyRI0dmWubUqVN67LHHFBoaKjc3N4WEhKh79+6ZirUkpaam/u37dKPD4QzD0JQpUxQRESFPT0/5+/ure/fuOnLkSMYyw4cPl7e3t+Li4rK8rl69eikoKEipqamSJLvdrokTJ6py5cpyd3dXiRIlNGDAAJ08eTLTeqVLl874DN/qfbLb7XrzzTdVqVIleXp6ys/PTzVr1tS///3vLOveyOLFi3XhwgU98sgjGjhwoA4ePKj169dnWS45OVljx45VlSpV5OHhoeLFi6tFixbasGGDJMfnOD4+Xp9++mnGZ/x6zoSEBL3wwgsqU6aMPDw8VKxYMdWrV09z5869rYwArIsSBKBQat++vZydnbVu3bqbLnPs2DF16NBBbm5umjFjhpYvX663335b3t7eSklJUXBwsJYvXy5JGjp0qDZu3KiNGzdq1KhRmZ7noYceUvny5bVgwQJ99NFHt8y1Y8cODR8+XM8995wWLVqkyMhIPfvss3rnnXfu+DVOmTJFjRs3VsmSJTOy3eoQvAMHDigyMlJ79+7Vf/7zHy1cuFBVq1bVoEGDNHHixCzLjxw5UsePH9d///tfffzxxzp06JA6deqk9PT0W+Zau3atWrZsqStXrmj69OmaO3eufHx81KlTJ82fP1+S43DBhQsXSpKefvppbdy48bYPFxs6dKgWL16sS5cuZbyuDRs2aOjQobe1/rx58/Tkk0+qWbNmWrRokRYvXqznnntO8fHxGcucOnVK9evX16JFizRixAh9//33mjx5sooWLZqx3bt9nx5//HENHz5crVu31uLFizVlyhTt3btXkZGRGUVryJAhSkhI0Jdffplp3cuXL2vJkiXq16+fXF1dJUn/+Mc/9NJLL6lNmzZaunSp3njjDS1fvlyRkZGKjY29rffmzyZOnKjRo0er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kqK2bdtq586deuONN9S4cWP5+vpq06ZNeuedd1S7dm1FRETk2PbMxsAIAAAAQAHRunVrlSxZUuPHj7/lcl9//bWqVasmd3d3lS5dWu++++4tl588ebLWrVunn376ScOGDVNERITKli2rhx9+WJs3b1aFChVuuN6lS5c0YMAA+fv7y8vLS+3atdOhQ4cyHr9w4YL69OmjUqVKycvLSzVq1NDcuXNvmWX58uUqWrSoZs+efcvl7gYlCAAAACggnJ2dNW7cOL3//vs6efLkDZfZtm2bevbsqd69e2v37t0aPXq0Ro0apVmzZt30eT///HO1bt1atWvXzvKYq6urvL29b7jeoEGDtHXrVi1dulQbN26UYRhq3769UlNTJUlJSUmqW7euvv32W+3Zs0ePPfaY+vfvr82bN9/w+ebNm6eePXtq9uzZGjBgwN+8G9lnagkaPXq0bDZbplvJkiXNjAQAAADka127dlVERIRef/31Gz4+adIktWrVSqNGjVLFihU1aNAgPfXUU/rXv/510+c8dOiQKleufEc5Dh06pKVLl+q///2vmjZtqlq1aunzzz/XqVOntHjxYknSPffcoxdeeCFjz9LTTz+ttm3basGCBVmeb8qUKXriiSe0ZMkSde7c+Y6y3CnTzwmqVq2aVq5cmXHf2dnZxDQAAABA/jdhwgS1bNlSzz//fJbHoqKispSIxo0ba/LkyUpPT7/h79uGYchms91RhqioKLm4uKhhw4YZ84oXL65KlSopKipKkpSenq63335b8+fP16lTp5ScnKzk5OQse5a+/vprnTt3TuvXr1eDBg3uKEd2mH44nIuLi0qWLJlxCwwMNDsSAAAAkK/dd999atu2rUaOHJnlsRsVmr8bOa5ixYoZxeV23ew5/7z9d999V++9957++c9/atWqVdqxY4fatm2rlJSUTOtEREQoMDBQM2fOvOtR7m6H6XuCDh06pJCQELm7u6thw4YaN26cypYte8NlrzfH6+Li4vIqJpAr8vKibDmNi7wBAGCut99+WxEREapYsWKm+VWrVtX69eszzduwYYMqVqx406OuHn74YY0cOVK//fZblvOC0tLSbrj3pmrVqkpLS9PmzZsVGRkpyTEQwsGDB1WlimOY8Z9//lmdO3dWv379JEl2u12HDh3KePy6cuXK6d1331Xz5s3l7OysDz744A7fjTtj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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "sns.histplot(group_no_cloak, kde=True, label='No Cloak', color='blue')\n",
    "sns.histplot(group_cloak, kde=True, label='Cloak', color='green')\n",
    "plt.legend()\n",
    "plt.title(\"Distribution of Mischievous Acts\")\n",
    "plt.xlabel(\"Mischievous Acts\")\n",
    "plt.ylabel(\"Frequency\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5807ff79-94af-4060-9e0b-df17c4f88656",
   "metadata": {},
   "source": [
    "#### Independent Samples T-Test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5d2eac23-0391-4c6e-b667-61ba2c30bbba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "T-statistic = -11.567632712974532, p-value = 8.017065864530486e-11\n"
     ]
    }
   ],
   "source": [
    "t_stat, p_value = stats.ttest_ind(group_no_cloak, group_cloak)\n",
    "print(f\"T-statistic = {t_stat}, p-value = {p_value}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "197f2923-f7e8-4705-a069-4fb135b48f09",
   "metadata": {},
   "source": [
    "#### Results of Report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b2254cf8-1c80-4582-8ad7-20332b64a99f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The result of the t-test is significant (p-value = 8.017065864530486e-11)\n"
     ]
    }
   ],
   "source": [
    "if p_value < 0.05:\n",
    "    result = \"significant\"\n",
    "else:\n",
    "    result = \"not significant\"\n",
    "\n",
    "print(f\"The result of the t-test is {result} (p-value = {p_value})\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d42b484a-6168-4a66-93d5-e78e333f2bc1",
   "metadata": {},
   "source": [
    "### Invisibility Cloak Experiment: Independent Sampels T-Test\n",
    "\n",
    "#### Dataset Description:\n",
    "\n",
    "##### Independent Variable (IV):\n",
    "Invisibility Cloak (0 = without cloak, 1 = with cloak)\n",
    "\n",
    "##### Dependent Variable (DV):\n",
    "Mischievous Acts committed by participants\n",
    "\n",
    "\n",
    "#### Assumptions:\n",
    "1. Continuous Variable: The dependent variable (Mischief) is measured on a continuous scale (number of mischievous acts).\n",
    "2. Independent Groups: The dataset contains two independent groups (participants with and without the invisibility cloak).\n",
    "3. Random Sampling: Assumed that the participants were randomly selected.\n",
    "4. Homogeneity of Variances:\n",
    " - Levene’s Test: p-value > 0.05 (assumption of equal variances is met if p-value > 0.05).\n",
    "5. Normality of Data:\n",
    "   - Shapiro-Wilk Test: The normality assumption for each group is tested (both p-values should be > 0.05 to assume normality).\n",
    "  \n",
    "#### Statistical Test:\n",
    "##### Independent Samples T-Test:\n",
    "T-statistic and p-value are computed for the difference in mischievous acts between participants with and without the invisibility cloak.\n",
    "\n",
    "##### Results:\n",
    "The p-value of the t-test is compared to a significance level of 0.05 to determine if there is a statistically significant difference in the number of mischievous acts."
   ]
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
