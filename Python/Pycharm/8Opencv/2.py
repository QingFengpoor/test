import cv2
img=cv2.imread('test.png',0)
cv2.putText(img,"Cokie race",(100,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27: #等待 ESC 键
    cv2.destroyAllWindows()
elif k==ord('s'): #等待 's' 键来保存和退出
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
