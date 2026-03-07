# CVL_Assignment01: Image Enhancement

## Methodology
To correct the dark image, I used a **Linear Transformation** method with Python and the OpenCV library. This improvement relies on the following mathematical formula:

$$g(x) = \alpha \cdot f(x) + \beta$$

* $f(x)$ represents the original pixel value.
* $g(x)$ represents the new, improved pixel value.
* **$\alpha$ (Alpha = 1.3):** This controls the contrast. Multiplying the pixels by a number larger than 1.0 increases the **contrast**, making the difference between the light and dark areas more noticeable.
* **$\beta$ (Beta = 30):** This controls the brightness. Adding a positive number increases the overall **brightness**, bringing out details from the dark areas.

I used the `cv2.convertScaleAbs()` function in OpenCV to apply this formula. This function is highly useful because it automatically keeps the final pixel values within the standard 0 to 255 range, which prevents visual errors in the final picture.

## Results

Below is a comparison between the original dark photo and the improved result after applying the linear transformation:

### Before (Original Underexposed Image)
![Original Image](underexpose_photo.jpg) 

### After (Enhanced Image)
![Enhanced Image](enhanced_result.jpg)
