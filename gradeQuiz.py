import sys
from imageio import imread
from skimage.metrics import structural_similarity
from skimage.transform import resize

height = 2000
width = 1700
blankMapStructuralSim = 0.95 #TODO update this once final answer key is done.

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

if __name__ == '__main__':
  img_a = sys.argv[1]
  img_b = sys.argv[2]
  # get the similarity values
  structural_sim = structural_sim(img_a, img_b)
  print(normalizeScore(structural_sim))