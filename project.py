import pytesseract
import cv2
import glob
import os

# specify path to the license plate images folder
path_for_license_plates = os.getcwd() + "/license-plates/**/*.jpg"
list_license_plates = [] 
predicted_license_plates = []

for path_to_license_plate in glob.glob(path_for_license_plates, recursive=True): 
    license_plate_file = os.path.basename(path_to_license_plate)  # Get file name only
    license_plate, _ = os.path.splitext(license_plate_file) 
    list_license_plates.append(license_plate)  # Store actual license plate names
    
    # Read each license plate image file using OpenCV 
    img = cv2.imread(path_to_license_plate)
    if img is None:  # Check if the image is loaded correctly
        print(f"Error loading image: {path_to_license_plate}")
        continue
    
    # Pass image to Tesseract OCR engine
    predicted_result = pytesseract.image_to_string(img, lang='eng', 
        config='--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    
    # Clean and store the predicted result
    filter_predicted_result = "".join(predicted_result.split()).replace(":", "").replace("-", "")
    predicted_license_plates.append(filter_predicted_result)

# Print headers once
print("Actual License Plate", "\t", "Predicted License Plate", "\t", "Accuracy") 
print("--------------------", "\t", "-----------------------", "\t", "--------") 

# Function to calculate and display predicted accuracy
def calculate_predicted_accuracy(actual_list, predicted_list): 
    for actual_plate, predict_plate in zip(actual_list, predicted_list): 
        accuracy = "0 %"
        num_matches = 0
        
        # Clean up both actual and predicted results for comparison
        actual_plate_clean = actual_plate.strip().upper()  # Remove spaces and convert to uppercase
        predicted_plate_clean = predict_plate.strip().upper()  # Same for predicted plate

        if actual_plate_clean == predicted_plate_clean: 
            accuracy = "100 %"
        else: 
            if len(actual_plate_clean) == len(predicted_plate_clean): 
                for a, p in zip(actual_plate_clean, predicted_plate_clean): 
                    if a == p: 
                        num_matches += 1
                accuracy = str(round((num_matches / len(actual_plate_clean)) * 100, 2)) + "%"  # Ensure proper formatting
        print(f"      {actual_plate}\t\t\t{predict_plate}\t\t\t  {accuracy}") 

calculate_predicted_accuracy(list_license_plates, predicted_license_plates)
