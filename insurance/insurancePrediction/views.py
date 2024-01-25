from django.shortcuts import render
from src.mlproject.pipelines.prediction_pipeline import CustomData, PredictionPipeline

# Create your views here.

def predictView(request):
    if request.method == 'GET':
        print('s')
        predicted = 0
        context = {
            'prediction': 0 
        }
        return render(request, "views/predict.html", context)
        

    
def predict(request):
    print('hello')
    age = request.GET['Age']
    height = request.GET['Height']
    weight = request.GET['Weight']
    gender = request.GET['Gender']
    region = request.GET['region']
    children = request.GET['Children']
    smoker = request.GET['Smoker']
    bmi = int(weight)/(int(height)*int(height))

    data = CustomData(
        age, gender, bmi, children, smoker, region
    )

    pred_df=data.get_data_as_df()
    print(pred_df)
    print("Before Prediction")

    predict_pipeline=PredictionPipeline()
    print("Mid Prediction")
    results=predict_pipeline.predict(pred_df)
    print("after Prediction")
    context = {
        'prediction': round(results[0], 2)
    }
    return render(request, 'views/predict.html',context)
        