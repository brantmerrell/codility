# A script for aggregating the scores listed in scripts within this repo

scores <- data.frame(exercise=list.files(pattern="^\\d+\\.\\d+_.+\\.(js|py)$"),
		link="",
		performance="",
		correctness="",
		difficulty="",
		stringsAsFactors=F)
for(n in 1:nrow(scores)){
	script <- readLines(scores[n,"exercise"])
	scores[n,"link"] <- paste(script[grepl("app.codility.com/",script,ignore.case=T)],
				collapse="\n")
	scores[n,"performance"] <- paste(script[grepl("performance",script,ignore.case=T)],
					collapse="\n")
	scores[n,"correctness"] <- paste(script[grepl("correctness",script,ignore.case=T)],
					collapse="\n")
	scores[n,"difficulty"] <- paste(script[grepl("difficulty:",script,ignore.case=T)],
					collapse="\n")
}

scores$link <- sub("^[[:punct:]]+ +","",scores$link)
#library(stringr)
scores$performance <- as.numeric(gsub("[[:alpha:]]|[[:punct:]]| ","",scores$performance))
scores$correctness <- as.numeric(gsub("[[:alpha:]]|[[:punct:]]| ","",scores$correctness))
scores$difficulty <- tolower(gsub("^([[:punct:]]| )+[Dd]ifficulty: ","",scores$difficulty))
scores <- scores[!grepl("R$",scores$exercise),]
scores <- scores[order(!is.na(scores$correctness),
			!is.na(scores$performance),
			scores$correctness,
			scores$performance,
			scores$difficulty,
			decreasing=T),]
write.csv(scores,"scores.csv",row.names=F)
DF <- rbind(	py.correctness=summary(scores[grepl("py$",scores$exercise),"correctness"]),
		js.correctness=summary(scores[grepl("js$",scores$exercise),"correctness"]),
		py.performance=summary(scores[grepl("py$",scores$exercise),"performance"]),
		js.performance=summary(scores[grepl("js$",scores$exercise),"performance"]))
print(DF)
write.csv(DF,"scoreSummary.csv")
