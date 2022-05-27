# WordleSolver

WordleSolver is a simple Wordle solution finder. It will often find the solution in only 4 guesses.

# Usage
The file "wordle.py" must be edited and run to give results. <br>
The program will print a list of the top 300 words that it thinks you should guess next. <br><br>
To tell it what letters to exclude, edit line 28 and fill the array with any letters that are gray in Wordle. <br>Example : exclude=[a,b,c]<br><br>
To tell it what letters are yellow, edit line 29 and fill the array with any letters that are yellow followed by the INDEX of where it is. <br>Example : yellow=[a,2,b,1,c,0]<br><br>
To tell it what letters are green, edit line 30 and replace any zero with the letter that should go there. <br>Example : green=[0,a,0,b,c]
