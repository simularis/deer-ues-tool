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

FROM MeasDef

JOIN simdata ON 
  simdata.BldgHVAC = MeasDef.BldgHVAC AND 
  simdata.BldgVint = MeasDef.BldgVint;





