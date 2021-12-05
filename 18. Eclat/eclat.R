#Eclat

library(arules)
dataset = read.csv('Market_Basket_Optimisation.csv',header = FALSE)
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)

rules = eclat(data = dataset, parameter = list(supp?rt = 0.004, minlen = 2 ))
inspect(sort(rules, by = 'support')[1:20])
