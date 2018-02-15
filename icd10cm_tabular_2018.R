# Extract <name> and <inclusionTerm> from Icd10cm_tabular_2018.xml

# This script assumes <name> precedes corresponding <desc> and <inclusionTerm> in xml lines

# extract xml from zipFile
if(!file.exists("icd10cm_tabular_2018.xml")){
	unzip("ICD-10-CM-Codes-Tables-and-Index-2018.zip"), files="icd10cm_tabular_2018.xml")
}

# read xml file
library(XML)
DF <- xmlParse("icd10cm_tabular_2018.xml")

# Convert to list
DF <- xmlToList(DF)

# Convert to (named) vector
DF <- unlist(DF)

# Convert to data frame
DF <- data.frame(XML=names(DF),Value=DF, xmlLevels=unlist(lapply(strsplit(names(DF),"\\."),length)),
		stringsAsFactors=F) # enable cell-based data extraction by avoiding factors

# Built 'target' data frame
tarDF  <-  data.frame(name=DF[grepl("name$",DF$XML),"Value"],
			desc="",
			inclusionTerm="",
			ref=grep("name$",DF$XML), # provide row to corresponding DF
			stringsAsFactors=F) # enable cell-based data insertion by avoiding factors

# insert desc variables from DF to tarDF
for(n in 1:nrow(tarDF)){

	# build range by defining stopper
	stopper <- tarDF[n,"ref"]+1
	while(stopper<=nrow(DF) & !grepl("name$",DF[stopper,"XML"])){stopper <- stopper+1}
	Range <- tarDF[n,"ref"]:(stopper-1)

	# Extracting values for desc and inclusionTerm relies on subset within subset
	## 1st subset is Range, defining XML values from name to name
	## 2nd subset is grepl(<pattern>, <XML paths>), defining rows of DF that match the pattern
	### Patterns for desc and inclusionTerm are "desc$" and "inclusionTerm.note$", respectively
	# Process only works because <name> always precedes <desc> and <inclusionTerm> in xml File
	desc <- DF[Range[grepl("desc$",DF[Range,"XML"])],"Value"]
	inclusionTerm <- DF[Range[grepl("inclusionTerm.note$", DF[Range,"XML"])],"Value"]

	# insert description
	tarDF[n,"desc"] <- paste(desc,collapse = " \n ")

	# insert InclusionTerm
	tarDF[n,"inclusionTerm"] <- paste(inclusionTerm, collapse = " \n ")
	print(tarDF[n,])
}

# store csv file
write.csv(tarDF, "icd10cm_tabular_2018.csv")

