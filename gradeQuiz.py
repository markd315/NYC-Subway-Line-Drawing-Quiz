import sys
from imageio import imread
from skimage.metrics import structural_similarity
from skimage.transform import resize

height = 2000
width = 1700
blankMapStructuralSim = 0.9500506656399518

def structural_sim(path_a, path_b):
  '''
  Measure the structural similarity between two images
  @args:
    {str} path_a: the path to an image file
    {str} path_b: the path to an image file
  @returns:
    {float} a float {-1:1} that measures structural similarity
      between the input images
  '''
  img_a = get_img(path_a)
  img_b = get_img(path_b)
  sim, diff = structural_similarity(img_a, img_b, full=True, multichannel=True)
  return sim

def normalizeScore(structuralSim):
	maxScore = 1 - blankMapStructuralSim
	yourScore = structuralSim - blankMapStructuralSim
	return 100.0*yourScore/maxScore

def get_img(path, norm_size=True, norm_exposure=False):
  '''
  Prepare an image for image processing tasks
  '''
  # flatten returns a 2d grayscale array
  img = imread(path).astype(int)
  # resizing returns float vals 0:255; convert to ints for downstream tasks
  if norm_size:
    img = resize(img, (height, width), anti_aliasing=True, preserve_range=True)
  if norm_exposure:
    img = normalize_exposure(img)
  return img

def interpretScore(score):
  if(score < -80.0):
    print("Wow. That was really bad (F)")
  if(score < -60.0):
    print("Poor effort (D)")
  elif(score < -55.0):
    print("Not good (C-)")
  elif(score < -50.0):
    print("Not your best attempt (C)")
  elif(score < -45.0):
    print("Mediocre (C+)")
  elif(score < -40.0):
    print("Keep practicing (B-)")
  elif(score < -35.0):
    print("You're finally getting somewhere (B)")
  elif(score < -25.0):
    print("Solid effort (B+)")
  elif(score < 0.0 ):
    print("Okay (A-)")
  elif(score == 0.0):
    print("Pretty sure you used the blank map")
  elif(score < 30.0):
    print("Good (A)")
  elif(score < 60.0):
    print("Very good (A+)")
  elif(score < 70.0):
    print("Amazing (A+)")
  elif(score < 75.0):
    print("Incredible effort (A+)")
  elif(score >= 100.0):
    print("Looks like you used the answer key")
  else:
    print("Inhuman effort, assuming this is cheating")

if __name__ == '__main__':
  img_a = sys.argv[1]
  img_b = sys.argv[2]
  # get the similarity values
  structural_sim = structural_sim(img_a, img_b)
  #print(structural_sim)
  score = normalizeScore(structural_sim)
  print(score)
  interpretScore(score)