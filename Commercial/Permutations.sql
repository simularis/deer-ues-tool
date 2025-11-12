/*
This creates the table Permutations, which is based on the available offering IDs. 
*/

DROP TABLE IF EXISTS Permutations;
CREATE TABLE Permutations AS 

SELECT DISTINCT
MeasDef.OfferingID,
MeasDef.MAT,
simdata_long.BldgLoc,
simdata_long.BldgType,
simdata_long.BldgVint,
simdata_long.BldgHVAC,
MeasDef.PreTechID,
MeasDef.StdTechID,
MeasDef.MeasTechID,
"Area [m2]" as "NormUnits",
simdata_long."Value" AS "NumUnits"

From MeasDef

JOIN simdata_long on simdata_long.BldgType = MeasDef.BldgType and simdata_long.BldgVint = MeasDef.BldgVint

WHERE simdata_long."Value Name" LIKE "Area/Classrooms";





