import cv2
import numpy as np
from matplotlib import pyplot as plt

from sklearn.preprocessing import PolynomialFeatures   
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

LUT2 = np.zeros((492))
for y in range(22500,25500):
    x = int(round((y/100-225)/1 + 1/(1.2**(225-y/100))+225))
    LUT2[x-226] = int(round(y/100.0))
print(x)
#asdf
#print(LUT2)  ## INPUT-230 = LUTindex; min INDEX = 230, higher than ~345 input is just 255 output
#LUT1 = np.zeros_like(LUT2)
LUT1 = 255-np.flip(LUT2)
#print(LUT1) ## INPUT+120 = LUTINDEX; max INPUT 25; min -94 ?
#print(LUT1[119])
#asdf
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
img2 = img2.astype(np.float32, copy=False)
tb=np.zeros(3)
tm=np.zeros(3)
tc=np.zeros(3)
for rgb in range(3):
	tb[rgb]=0
	tm[rgb]=1
	tt = 999
	tc[rgb]=0
	for cc in range(-10,50):
		c=cc/3000.0
		#print(cc)
		for mm in range(1,40):
			m = mm/10000.0
			for b in range(-100,20):
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

#mb = np.min(tb)+np.min(img2)
#print("min b",mb)
#if (mb<0):  ## Darken a bit; just a safe amount
#    print("Darkening not applied; will need to crop sub black values")
#    mb=0
#else:
#    print("Darking APPLIED! - no sub 0 cropping needed")
mb=0## TMP

for rgb in range(3):
	img2[:,:,rgb] = img2[:,:,rgb]*tm[rgb] + tb[rgb] + np.power(img2[:,:,rgb],2)*tc[rgb] - mb
# print(np.min(img2))
# img2-=np.min(img2)
#mh=255-np.max(img2)
#if (mh<0):
#    mh=0;
#mh = mh-mb/2
#img2+=mh
where = np.where(img2>225)
out = LUT2[np.uint16(np.round(img2[where]-225))]
img2[where] = out
#print(np.shape(where))
#print(LUT1) ## INPUT+120 = LUTINDEX; max INPUT 25; min -94 ?
where = np.where((img2<=30) & (img2>-461))
out = LUT1[np.uint16(np.round(img2[where]+461))]
print(out)
img2[where] = out

img2[np.where(img2>255)]=255 # cut out highlights
img2[np.where(img2<0)]=0
img2 = img2.astype(np.uint8, copy=False)

#cv2.imshow("image",cv2.cvtColor(cv2.resize(img2,(1920,1080)), cv2.COLOR_RGB2BGR))
#cv2.waitKey(1)

cap = cv2.VideoCapture('P1002881.MOV')
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame,(1280,720))
        frame = frame.astype(np.float32, copy=False)

        for rgb in range(3):
            frame[:,:,rgb] = frame[:,:,rgb]*tm[rgb] + tb[rgb] + np.power(frame[:,:,rgb],2)*tc[rgb] - mb
            
        frame+=35 ########## BRIGHTNESS
        print(".")
        ##########  TAPER OFF ENDS
        where = np.where(frame>225)
        out = LUT2[np.uint16(np.round(frame[where]-225))]
        frame[where] = out
        ##
        where = np.where((frame<=30) & (frame>-461))
        out = LUT1[np.uint16(np.round(frame[where]+461))]
        frame[where] = out
        ###########
        frame[np.where(frame>255)]=255 # cut out highlights
        frame[np.where(frame<0)]=0 # cut out shadows
        frame = frame.astype(np.uint8, copy=False)

        cv2.imshow("image",cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        cv2.waitKey(1)
 
