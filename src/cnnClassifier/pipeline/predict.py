import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model("C:/Users/ANSH/Desktop/Chicken-Disease-Classification/artifacts/training/trained_model.h5")

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]
        

'''
if __name__ == "__main__":
    test_image_path = "C:/Users/ANSH/Downloads/Chicken-fecal-images/Chicken-fecal-images/Coccidiosis/cocci.8.jpg"  # ← Change this to your image path

    if not os.path.exists(test_image_path):
        print(f"[ERROR] Image not found: {test_image_path}")
    else:
        pipeline = PredictionPipeline(test_image_path)
        result = pipeline.predict()
        print("Prediction result:", result)
        '''