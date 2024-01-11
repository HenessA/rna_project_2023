#Import the dataset containing the 3 values of ETA angle : 
train.eta.concatene <- read.delim("~/path/to/your/dataset/train-file.txt", header=FALSE)


#Change the header of the columns : 
colnames(train.eta.concatene)[1] <- "eta"
colnames(train.eta.concatene)[2] <- "eta1"
colnames(train.eta.concatene)[3] <- "eta2"

#Convert the values of the dataset, to make sure that we treat numeric values :
train.eta.concatene$eta <- as.numeric(as.character(train.eta.concatene$eta))
train.eta.concatene$eta1 <- as.numeric(as.character(train.eta.concatene$eta1))
train.eta.concatene$eta2 <- as.numeric(as.character(train.eta.concatene$eta2))

#Plot the distribution of each features : 

hist(train.eta.concatene$eta, main = "Histogram of eta distribution", xlab = "Valeurs", col = "skyblue", border = "black")
hist(train.eta.concatene$eta1, main = "Histogram of eta' distribution", xlab = "Values", col = "skyblue", border = "black")
hist(train.eta.concatene$eta2, main = "Histogram of eta'' distribution", xlab = "Values", col = "skyblue", border = "black")

#Observations : 
#We choosed, the eta torsion angle, which is a pseudo torsion angle, and we noticed that in the result of the DSSR calculation
#we got several values named eta, but with different degree. To get a better idea of what we should use, we processed
#several steps of pre processing the data, to finally get the distribution plot. 
#According to them, we can se 3 different distribution of the values (corresponding to the 3 eta angles). And because of
#those distribution we choosed to work with the eta" angle, because of the the higher number of intervals, that 
#will correspond to the classes, for the classification step. 


summary(train.eta.concatene$eta)
summary(train.eta.concatene$eta1)
summary(train.eta.concatene$eta2)


#PLot the distribution of the class | Train set 
train.fichier.concatene_20class <- read.delim("~/path/to/your/dataset/train-file-class.txt")
View(train.fichier.concatene_20class)

colnames(train.fichier.concatene_20class)[1] <- "class"
colnames(train.fichier.concatene_20class)[2] <- "base"
