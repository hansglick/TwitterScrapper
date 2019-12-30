# config
rm(list=ls())

# Liste de Datasets
FolderNames = c("trackIdentity/","trackRetraites/")
root = "/home/osboxes/proj/twitter/"
DatasSetsChoices = paste0(root,FolderNames,"graph.csv")
names(DatasSetsChoices) = FolderNames

# load functions
source(file = "fun.R",encoding = "UTF-8")