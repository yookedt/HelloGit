import cv2

def __main():
    img = cv2.imread('zinzya.jpg')
    img = getResize(img)
    
    org = img.copy()
    img = cv2.bitwise_not(img)

    cv2.imshow('Original',org)
    cv2.imshow('Final result',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getResize(src):
    basePixSize = 1280

    height = src.shape[0]
    width = src.shape[1]

    largeSize = max(height,width)

    resizeRate = basePixSize / largeSize

    dst = cv2.resize(src,(int(width*resizeRate),int(height*resizeRate)))
    
    return dst

if __name__ == '__main__':
    __main()
