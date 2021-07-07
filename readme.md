# NYC Subway Line Drawing Quiz

## Motivation
I wanted a quiz where you have to draw the NYC subway lines as precisely as possible, since I am trying to learn their paths.

![Example](https://raw.githubusercontent.com/markd315/NYC-Subway-Line-Drawing-Quiz/master/test/testCase123AccurateRendition.png)
For example, this would be a decent (but not perfect) start to the quiz. The 123 (red) line is bang on in the right areas, covers the correct territory with the correct shape, and is the proper color.

It's not "perfect" because, for example, the 1 fork goes all the way through the financial district and into the Hudson river. But because this image is so similar to the answer key, it will earn a quite high score if you can draw all lines this accurately.

## Instructions
It is suggested that you use the following settings when you draw your map in an image editing application (I used GIMP which is free):
- Pencil tool 5 pixels wide.
- Copy the colors from `palette.png` with an eyedropper tool before you draw each line.
- It is recommended to go in the color order listed in palette: first left to right and then down the rows since that is how the answer key was generated.

To grade your quiz run:
`python gradeQuiz.py answerKey.png yourAnswer.png`
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

This is solved using computer vision (structural similarity scores). The code could easily be applied to other similar quizzes, potentially even using different similarity algorithms.

### Viability Testing
```
python gradeQuiz.py test/123.png test/testCase123AccurateRendition.png
python gradeQuiz.py test/123.png test/testCase123BadColor.png
python gradeQuiz.py test/123.png test/testCase123SloppyLine.png
python gradeQuiz.py test/123.png test/testCase123PerfectStructureBadPosition.png
```

![Example](https://raw.githubusercontent.com/markd315/NYC-Subway-Line-Drawing-Quiz/master/test/testResults.png)
Here are some example scores comparing various attempts with different problems to validate the reasonableness of the SSIM approximate grading. Note that the curving may have changed since the screenshot was taken.

As you can see from the results, mix-ups are mostly forgiven by the algorithm, which may not be desirable for learners, but drawing lines in the wrong place is heavily punished. The sloppier your lines are, the worse you will score, but you will still get a good amount of partial credit for effort from this algorithm. Good luck!

### Partial quiz

If you go in the recommended order, you can opt to have your quiz graded against an incomplete answer key like this, to assess what you have so far.

```
python gradeQuiz.py versions/123.png yourAnswer.png
python gradeQuiz.py versions/123456.png yourAnswer.png
python gradeQuiz.py versions/1234567.png yourAnswer.png
python gradeQuiz.py versions/1234567ACE.png yourAnswer.png
python gradeQuiz.py versions/1234567ACEBDFM.png yourAnswer.png
python gradeQuiz.py versions/1234567ACEBDFML.png yourAnswer.png
python gradeQuiz.py versions/1234567ACEBDFMLG.png yourAnswer.png
python gradeQuiz.py versions/1234567ACEBDFMLGNQRW.png yourAnswer.png
python gradeQuiz.py versions/1234567ACEBDFMLGNQRWJZ.png yourAnswer.png
```

### Cheating
```
python gradeQuiz.py answerKey.png answerKey.png
100.0
```

Well that wasn't too hard.


#### Credits
I borrowed some code shamelessly from here https://gist.github.com/duhaime/211365edaddf7ff89c0a36d9f3f7956c