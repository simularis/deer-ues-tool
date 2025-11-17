/*
This creates the table UEC, unit energy consumption. 
*/
DROP TABLE IF EXISTS UEC;
CREATE TABLE UEC AS

SELECT
Permutations.OfferingID,
Permutations.MAT,
Permutations.BldgLoc,
Permutations.BldgType,
Permutations.BldgVint,
Permutations.BldgHVAC,
Permutations.PreTechID,
Permutations.StdTechID,
Permutations.MeasTechID,
meas.NormUnit AS "NormUnit",
meas.NumUnits AS "NumUnits",
meas."Value Name" AS "Value Name",
pre.Value/meas.NumUnits AS "preValue",
std.Value/meas.NumUnits AS "stdValue",
meas.Value/meas.NumUnits AS "measValue"

FROM Permutations

LEFT JOIN simdata_story pre on 
  pre."TechID"   = Permutations."PreTechID" AND
  pre."BldgType" = Permutations."BldgType" AND
  pre."BldgVint" = Permutations."BldgVint" AND
  pre."BldgLoc"  = Permutations."BldgLoc" AND
  pre."BldgHVAC" = Permutations."BldgHVAC"
 LEFT JOIN simdata_story std on 
  std."TechID"   = Permutations."StdTechID" AND
  std."BldgType" = Permutations."BldgType" AND
  std."BldgVint" = Permutations."BldgVint" AND
  std."BldgLoc"  = Permutations."BldgLoc" AND
  std."BldgHVAC" = Permutations."BldgHVAC"
LEFT JOIN simdata_story meas on 
  meas."TechID"   = Permutations."MeasTechID" AND
  meas."BldgType" = Permutations."BldgType" AND
  meas."BldgVint" = Permutations."BldgVint" AND
  meas."BldgLoc"  = Permutations."BldgLoc" AND
  meas."BldgHVAC" = Permutations."BldgHVAC"
  
 ORDER BY 
  Permutations."OfferingID", Permutations."BldgType", Permutations."BldgHVAC", Permutations."BldgVint", Permutations."BldgLoc"



