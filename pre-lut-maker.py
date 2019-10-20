import cv2
import numpy as np
from matplotlib import pyplot as plt

from sklearn.preprocessing import PolynomialFeatures   
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


img = cv2.imread("image1.png", 1)

w,h,_ = np.shape(img);

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


right = [[147,163,96],[154,64,73],[0,166,153],
		[61,65,93],[96,102,102],[247,185,48],
		[62,63,64],[245,243,236],[138,83,129]]

wrong = np.zeros_like(right)

color = ('r','g','b')
for x in range(3):
	for y in range(3):
		print()
		for i,col in enumerate(color):
			seg = img[int(x*w/3):int((x+1)*w/3),int(y*h/3):int((y+1)*h/3),:]
			histr = cv2.calcHist([seg],[i],None,[256],[0,256])
			j = x*3+y+1
			print(np.where(np.max(histr)==histr)[0][0], right[j-1][i])
			wrong[j-1][i]=np.where(np.max(histr)==histr)[0][0]
			plt.subplot(3,3,j)
			plt.plot(histr,color = col)
			plt.xlim([0,256])
			

img2 = cv2.imread("image2.png", 1)	
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#print(np.ravel(right)[::3])
img2 = img2.astype("uint16")
tb=np.zeros(3)
tm=np.zeros(3)
tc=np.zeros(3)
for rgb in range(3):
	tb[rgb]=0
	tm[rgb]=1
	tt = 999
	tc[rgb]=0
	for cc in range(-10,10):
		c=cc/2000.0
		#print(cc)
		for mm in range(50,200):
			m = mm/100.0
			for b in range(-100,100):
				delta = np.ravel(right)[rgb::3]-np.ravel(wrong*m+b+np.power(wrong,2)*c)[rgb::3]
				#print(delta)
				power = np.power(delta,2)
				#print(power)
				mean = np.mean(power)
				#print(mean)
				final = np.sqrt(mean)
				if (final<tt):
					tb[rgb] = b
					tm[rgb] = m
					tt = final
					tc[rgb] = c
				else:
					continue
				#print(final,m,b)
	print("Best:",tt,"m:",tm[rgb],"b:",tb[rgb],"c:",tc[rgb])

mb = np.min(tb)+np.min(img2)
print("min b",mb)
if (mb<0):  ## Darken a bit; just a safe amount
	mb=0


for rgb in range(3):
	img2[:,:,rgb] = img2[:,:,rgb]*tm[rgb] + tb[rgb] + np.power(img2[:,:,rgb],2)*tc[rgb] - mb
print(np.max(img2))

img2[np.where(img2>255)]=255 # cut out highlights
img2=img2.astype("uint8")
cv2.imshow("image",cv2.cvtColor(cv2.resize(img2,(640,480)), cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
