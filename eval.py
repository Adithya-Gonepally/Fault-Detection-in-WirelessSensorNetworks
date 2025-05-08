import pandas as pd
import numpy as np
import pickle

# load the test data from disk
testing_df = pd.read_pickle("testing_df.pkl")
normal, dos, r2l, u2r, probe = [], [], [], [], []
print(testing_df.values)
data = testing_df.values
for row in data:
    if row[38]== "normal":
        row = np.delete(row, 38)
        normal.append(row.reshape(1,122))
    if row[38]=="dos":
        row = np.delete(row, 38)
        dos.append(row.reshape(1,122))
    if row[38]== "r2l":
        row = np.delete(row, 38)
        r2l.append(row.reshape(1,122))
    if row[38]== "u2r":
        row = np.delete(row, 38)
        u2r.append(row.reshape(1,122))
    if row[38]== "probe":
        row = np.delete(row, 38)
        probe.append(row.reshape(1,122))


# load the trained model from disk
filename = "LSTMModel.sav"
LSTM_model = pickle.load(open(filename, 'rb'))


def main(class_name):   
    print(class_name)   
    if class_name=="3":
        ind = np.random.randint(0,9709)
        test = normal[ind]    
    if class_name=="1":
        ind = np.random.randint(0,2708)
        test = r2l[ind]
    if class_name=="2":
        ind = np.random.randint(0,66)
        test = u2r[ind]
    if class_name=="4":
        ind = np.random.randint(0,2420)
        test = probe[ind]
    if class_name=="0":
        ind = np.random.randint(0,1000)
        test = probe[ind]
    #print(ind)
    predictions = LSTM_model.predict(test)
    probabilities = LSTM_model.predict_proba(test)
    probabilities = probabilities[0]
    for i in range(5):
        probabilities[i] = "{:.2f}".format(probabilities[i]*100)
    print(predictions[0], list(probabilities))
    return(predictions[0], list(probabilities))

