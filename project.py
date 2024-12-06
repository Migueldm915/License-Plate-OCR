import pytesseract
import cv2
import glob
import os

path = os.getcwd() + "/license-plates/**/*.jpg"
lp_list = []
pred_list = []

for lp_path in glob.glob(path, recursive=True):
    lp_file = os.path.basename(lp_path)
    lp, _ = os.path.splitext(lp_file)
    lp_list.append(lp)
    
    img = cv2.imread(lp_path)
    if img is None:
        print(f"Error loading image: {lp_path}")
        continue
    
    pred = pytesseract.image_to_string(img, lang='eng', 
        config='--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    
    clean_pred = "".join(pred.split()).replace(":", "").replace("-", "")
    pred_list.append(clean_pred)

print("Actual License Plate", "\t", "Predicted License Plate", "\t", "Accuracy")
print("--------------------", "\t", "-----------------------", "\t", "--------")

def calc_acc(actual, pred):
    for a, p in zip(actual, pred):
        acc = "0 %"
        matches = 0
        
        a_clean = a.strip().upper()
        p_clean = p.strip().upper()

        if a_clean == p_clean:
            acc = "100 %"
        else:
            if len(a_clean) == len(p_clean):
                for x, y in zip(a_clean, p_clean):
                    if x == y:
                        matches += 1
                acc = str(round((matches / len(a_clean)) * 100, 2)) + "%"
        print(f"      {a}\t\t\t{p}\t\t\t  {acc}")

calc_acc(lp_list, pred_list)
