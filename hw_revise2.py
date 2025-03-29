import cv2

def process_image():
    # Load the image
    image = cv2.imread("open_cv/image/cat.jpg")
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection (Canny)
    edges = cv2.Canny(gray_image, 100, 200)
    
    # Convert to HSV format
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Display results
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imshow("Edge Detection", edges)
    cv2.imshow("HSV Image", hsv_image)
    
    # Save the processed images
    cv2.imwrite("gray_cat.png", gray_image)
    cv2.imwrite("edges_cat.png", edges)
    cv2.imwrite("hsv_cat.png", hsv_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with the image filename
process_image()