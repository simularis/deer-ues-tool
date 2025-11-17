/*
This creates the table Permutations, which is based on the available offering IDs. 
*/

DROP TABLE IF EXISTS Permutations;
CREATE TABLE Permutations AS 

SELECT DISTINCT
MeasDef.OfferingID,
MeasDef.MAT,
simdata_story.BldgLoc,
simdata_story.BldgType,
simdata_story.BldgVint,
simdata_story.BldgHVAC,
simdata_story.Story,
MeasDef.PreTechID,
MeasDef.StdTechID,
MeasDef.MeasTechID

FROM MeasDef

JOIN simdata_story on simdata_story.BldgHVAC = MeasDef.BldgHVAC and simdata_story.BldgVint = MeasDef.BldgVint;





