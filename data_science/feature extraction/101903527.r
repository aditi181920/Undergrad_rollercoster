#ADITI
#101903527
#3CO20

library(Peptides)
library(peptider)
library(xfun)
#set current working directory peoperly before proceeding
f=file("log.txt")
args = commandArgs(trailingOnly=TRUE)
inp=args[1]

#checking for correct number of parameters
if(length(args)>1){
  cat("Incorrect number of parameters. Only 1 required, provided more",file=f,append=TRUE,sep="\n")
  cat("Please provide only input file as parameter and nothing more")
  quit()
}

#checking for correct file extension
if(file_ext(inp)!="csv"){
  cat("File extension not correct",file=f,append=TRUE,sep="\n")
  cat("Check file extension and try again\n")
  quit()
}

#checking for existence of input file
mtry<-try(read.csv(inp))
if(class(mtry)=="try-error"){
  cat("File not found",file=f,append=TRUE,sep="\n")
  cat("File doesn't exist, please check and try again")
  quit()
}

#read in the input file
data=read.csv(inp)
head(data)
df<-data.frame(data)
head(df)

#now handle missing sequences in the input file
miss=sum(is.na(df))
cat("There are ",miss," missing values in the dataframe. These will be ignored",file=f, append=TRUE,sep=" ")

df=na.omit(df)
miss=sum(is.na(df))
cat("Now there are ",miss," missing values remaining")

#creating output csv file
col<-c('Peptide Sequence','len','Aliphatic_index','Boman_index','hmoment_index','insta_index','peptide_charge','molecular_weight','ProbabilityDetectionPeptide','#possibleneigh','#tinyamino','#smallamino','#aliphaticamino','#aromaticamino','#nonpolaramino','#polaramino','#chargedamino','#basicamino','#acidicamino','%tinyamino','%smallamino','%aliphaticamino','%aromaticamino','%nonpolaramino','%polaramino','%chargedamino','%basicamino','%acidicamino','hydrophobicity','KideraFactor','isoelectric pt.','target')
dfout=data.frame(matrix(nrow=0,ncol=length(col)))
colnames(dfout)=col

#insert values in output csv file
for( i in 1:nrow(df)){
  seq<-df[i,1]
  tar<-df[i,2]
  f1<-seq
  f2<-nchar(seq)
  f3<-aIndex(seq)
  f4<-boman(seq)
  f5<-hmoment(seq)
  f6<-instaIndex(seq)
  f7<-charge(seq)
  f8<-mw(seq)
  f9<-ppeptide(seq, libscheme = "NNK", N=10^8)
  f10<-getNofNeighbors(seq)
  amino<-aaComp(seq)
  for( x in amino){
    f11<-x[1]
    f12<-x[2]
    f13<-x[3]
    f14<-x[4]
    f15<-x[5]
    f16<-x[6]
    f17<-x[7]
    f18<-x[8]
    f19<-x[9]
    f20<-x[10]
    f21<-x[11]
    f22<-x[12]
    f23<-x[13]
    f24<-x[14]
    f25<-x[15]
    f26<-x[16]
    f27<-x[17]
    f28<-x[18]
    break
  }
  f29<-hydrophobicity(seq)
  f30<-kideraFactors(seq)
  f31<-pI(seq)
  f32<-tar
  dfout[nrow(dfout)+1,]=c(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32)
}

write.csv(dfout,"output-101903527.csv",row.names =F)