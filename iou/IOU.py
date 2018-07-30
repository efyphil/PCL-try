import pcl
parser = argparse.ArgumentParser(description='IOU')
parser.add_argument('--input_PC1', type=str, required=True, help="input PC, need file path")
parser.add_argument('--input_PC2', type=str, required=True, help="input PC, need file path")
opt = parser.parse_args()

print(opt)
cloud1 = pcl.load('input_PC1')
cloud2 = pcl.load('input_PC2')
print ('load')
def bb_intersection_over_union(cloud1, cloud2):
	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(cloud1[0], cloud2[0])
	yA = max(cloud1[1], cloud2[1])
	xB = min(cloud1[2], cloud2[2])
	yB = min(cloud1[3], cloud2[3])
 
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
 
	# compute the area of both the prediction and ground-truth
	# rectangles
	cloudAArea = (cloud1[2] - cloud1[0] + 1) * (cloud1[3] - cloud1[1] + 1)
	cloudBArea = (cloud2[2] - cloud2[0] + 1) * (cloud2[3] - cloud2[1] + 1)
 
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(cloudAArea + cloudBArea - interArea)
 
	# return the intersection over union value
	return iou
print(bb_intersection_over_union(cloud1, cloud2))
