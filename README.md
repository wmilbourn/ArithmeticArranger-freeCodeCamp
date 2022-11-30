# ArithmeticArranger.freeCodeCamp
 Project 1 in the Scientific Computing with Python certificate from freeCodeCamp.rg

The purpose of this project was to create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function has an optional second argument that when set to 'True' will display the answers. 

## Example
<a href = "https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter">Click Here</a> to see examples on the freeCodeCamp instruction page. 

  ## Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.
<ul>
<li>Situations that will return an error:</li>
 <ul>
 <li>If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.</li>
 <li>The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.</li>
 <li>Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.</li>
 <li>Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.</li>
 </ul>
<li>If the user supplied the correct format of problems, the conversion you return will follow these rules:</li>
 <ul>
 <li>There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).</li>
 <li>Numbers should be right-aligned.</li>
  <li>There should be four spaces between each problem.</li>
 <li>There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)</li>
 </ul>
</ul>
