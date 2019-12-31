#datapreprocessing
dataset = read.csv('Position_Salaries.csv')
dataset_fin = dataset[2]

#Splitting dataset into train-set and test-set
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
train_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)





