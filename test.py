from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

customdataobj = CustomData(0.73,'Very Good','G','VS2',63.1,57.0,5.77,5.75,3.63)
data = customdataobj.get_data_as_dataframe()
print(data)