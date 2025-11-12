/*
This creates the table UsePerUnit, which assigns energy use per building dwelling unit (total area [ft2] divided by number of buildings). 
*/

DROP TABLE IF EXISTS UsePerUnit;
CREATE TABLE UsePerUnit AS

SELECT
Permutations.OfferingID,
Permutations.MAT,
Permutations.BldgLoc,
Permutations.BldgType,
Permutations.BldgVint,
Permutations.BldgHVAC,
Permutations.PreTechID,
Permutations.StdTechID,
Permutations.MeasTechID

FROM Permutations

LEFT JOIN simdata_long pre on 
  pre."TechID"   = Permutations."PreTechID" AND  
  pre."BldgType" = Permutations."BldgType" AND
  pre."BldgVint" = Permutations."BldgVint" AND  
  pre."BldgLoc"  = Permutations."BldgLoc" AND  
  pre."BldgHVAC" = Permutations."BldgHVAC"
  
 LEFT JOIN simdata_long std on 
  std."TechID"   = Permutations."StdTechID" AND  
  std."BldgType" = Permutations."BldgType" AND
  std."BldgVint" = Permutations."BldgVint" AND  
  std."BldgLoc"  = Permutations."BldgLoc" AND  
  std."BldgHVAC" = Permutations."BldgHVAC"
  
LEFT JOIN simdata_long msr on 
  msr."TechID"   = Permutations."MeasTechID" AND  
  msr."BldgType" = Permutations."BldgType" AND
  msr."BldgVint" = Permutations."BldgVint" AND  
  msr."BldgLoc"  = Permutations."BldgLoc" AND  
  msr."BldgHVAC" = Permutations."BldgHVAC";


