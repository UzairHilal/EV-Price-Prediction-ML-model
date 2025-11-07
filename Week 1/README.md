# Week 1

In the first week the raw data is processed by deleting the null, duplicate, or any unwanted data and a new clean data file is created.

LabelEncoder is used to convert the text (like car names) into numbers. This is done because the model cannot understand/process text. So the text is converted to numbers which the model can process. - this encoder is saved for later use so that the car names can be converted to the same numbers again (not a different number).