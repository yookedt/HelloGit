import cv2
import numpy as np

if __name__ == '__main__':
    size = np.array([480,640,3])

    img = np.array([480,640,3])

    img = np.full(size,(255,255,255),dtype=np.uint8)

    color = np.array([0.,0.,255.])
    
    xcenter = 300
    ycenter = 240
    
    times = 1
    for i in range(50):
        rate = 10 * times
        print(xcenter)
        print(ycenter)
        for j in range(1):
            if(times%2==0):
                cv2.line(img=img,pt1=(xcenter,ycenter),pt2=(xcenter+rate,ycenter),color=color,thickness=2)
                xcenter += rate
                cv2.line(img=img,pt1=(xcenter,ycenter),pt2=(xcenter,ycenter+rate),color=color,thickness=2)
                ycenter += rate
            else:
                cv2.line(img=img,pt1=(xcenter,ycenter),pt2=(xcenter-rate,ycenter),color=color,thickness=2)
                xcenter -= rate
                cv2.line(img=img,pt1=(xcenter,ycenter),pt2=(xcenter,ycenter-rate),color=color,thickness=2)
                ycenter -= rate 
        times += 1

    cv2.imshow('guruguru',img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ =='__main__':
    __main__
