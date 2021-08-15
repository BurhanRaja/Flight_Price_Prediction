# import pickle
# data=pickle.load(open("Price_Regression.pkl","rb"))
# output=open("write.txt","w")
# output.write(str(data))
# output.flush()
# output.close()

import joblib
model = joblib.load('Price_Regression.pkl')
joblib.dump(model, 'Price_Regression.pkl',compress=3)