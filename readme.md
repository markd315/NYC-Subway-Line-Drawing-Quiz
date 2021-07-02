# NYC Subway Line Drawing Quiz

## Motivation
I wanted a quiz where you have to draw the NYC subway lines as precisely as possible, since I am trying to learn their paths.

## Instructions
It is suggested that you use the following settings when you draw your map in an image editing application:
- Pencil tool 5 pixels wide.
- Copy the colors from `palette.png` with an eyedropper tool before you draw each line.
- It is recommended to go in the color order listed in palette: first left to right and then down the rows since that is how the answer key was generated.

To grade your quiz run:
`python gradeQuiz.py yourAnswer.png answerKey.png`
## Prior to grading, install all the dependencies:
```
pip install pytest
pip install fits2bitmap
pip install imageio
pip install tifffile
pip install numpy
pip install lsm2bin
pip install f2py
pip install scikit_image
python -m pip install -U scikit-image[optional]
```
Some of these may not be necessary but I was getting environment issues setting it up on mine and am ultimately rather lazy.

### Scoring
The test is scored from a baseline derived from comparing the **blank** map to the answer key and making that the minimum score possible.
You could potentially score worse than zero by destroying the map worse than a blank. I recommend not doing that though.
It is not possible to score higher than 100.0

Note: The answer key itself will not be "perfect" since it is also drawn by hand (painstakingly with the aid of other reference maps)

### Approach
I used a "real" geographical map with neighborhood lines as the base, not the distorted one used on official MTA maps that disregards the surface scale to focus on underground clarity.

This is solved using computer vision and structural similarity scores. The code could easily be applied to other similar quizzes, potentially even using different similarity algorithms.

#### Credits
I borrowed some code shamelessly from here https://gist.github.com/duhaime/211365edaddf7ff89c0a36d9f3f7956c