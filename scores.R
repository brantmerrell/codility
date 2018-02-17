# A script for aggregating the scores listed in scripts within this repo

scores <- data.frame(exercise=list.files(pattern="^\\d+\\.\\d+_.+\\.(js|py|R)$"),
		link="",
		performance="",
		correctness="",
		stringsAsFactors=F)
for(n in 1:nrow(scores)){
	script <- readLines(scores[n,"exercise"])
	scores[n,"link"] <- paste(script[grepl("app.codility.com/",script,ignore.case=T)],
				collapse="\n")
	scores[n,"performance"] <- paste(script[grepl("performance",script,ignore.case=T)],
					collapse="\n")
	scores[n,"correctness"] <- paste(script[grepl("correctness",script,ignore.case=T)],
					collapse="\n")
}

scores$link <- sub("^[[:punct:]]+ +","",scores$link)
#library(stringr)
scores$performance <- as.numeric(gsub("[[:alpha:]]|[[:punct:]]| ","",scores$performance))
scores$correctness <- as.numeric(gsub("[[:alpha:]]|[[:punct:]]| ","",scores$correctness))
scores <- scores[order(scores$correctness+scores$performance),]
write.csv(scores,"scores.csv",row.names=F)
