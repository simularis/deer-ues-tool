-- creates permutations based on the available offering IDs


DROP TABLE IF EXISTS Permutations;
CREATE TABLE Permutations AS 

SELECT DISTINCT
MeasDef.OfferingID,
MeasDef.MAT,
simdata.BldgLoc,
simdata.BldgType,
simdata.BldgVint,
simdata.BldgHVAC,
MeasDef.PreTechID,
MeasDef.StdTechID,
MeasDef.MeasTechID

From MeasDef

JOIN simdata on simdata.BldgHVAC = MeasDef.BldgHVAC and simdata.BldgVint = MeasDef.BldgVint;
