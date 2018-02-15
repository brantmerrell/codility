
MaxDW <- read.delim("CTconditionCondition_browseMaxDW.csv",stringsAsFactors=F)
UNNEST <- readRDS("EveryConditionORcondition_browseUNNEST.rds")
UNNEST <- UNNEST[,!grepl("^X",colnames(UNNEST))]

for(Col in colnames(UNNEST)){
	if(class(UNNEST[,Col])=="factor"){
		UNNEST[,Col] <- as.vector(UNNEST[,Col])
	}
}

for(n in 1:nrow(MaxDW)){
	Match <- which(MaxDW[n,"HTMLconverted"]==UNNEST$conditionUTF8)
	if(0<length(Match)){
		for(Col in colnames(MaxDW)){
			UNNEST[Match,Col] <- MaxDW[n,Col]
		}
		UNNEST[Match,"matches"] <- length(Match)
		#print(UNNEST[Match,c("HTMLconverted","conditionUTF8","matches")])
	}#else{print(n)}
	print(paste(n,n/nrow(MaxDW)))
}

write.csv(UNNEST,"CTcondition2CUIdw.csv")
