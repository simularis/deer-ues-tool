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
meas.NormUnit as "NormUnit",
meas.NumUnits as "NumUnits",
((pre."Demand kW")/meas.NumUnits) as "PreUECkW",
(pre."HVAC kWh"/meas.NumUnits) as "PreUECkWh",
((pre."Natural Gas/Cooling")/meas.NumUnits) as "PreUECtherm",
((std."Demand kW")/meas.NumUnits) as "StdUECkW",
(std."HVAC kWh"/meas.NumUnits) as "StdUECkWh",
((std."Natural Gas/Cooling")/meas.NumUnits) as "StdUECtherm",
((meas."Demand kW")/meas.NumUnits) as "MeasUECkW",
(meas."HVAC kWh"/meas.NumUnits) as "MeasUECkWh",
((meas."Natural Gas/Cooling")/meas.NumUnits) as "MeasUECtherm"

FROM Permutations
LEFT JOIN simdata pre on 
  pre."TechID"   = Permutations."PreTechID" AND
  pre."BldgType" = Permutations."BldgType" AND
  pre."BldgVint" = Permutations."BldgVint" AND
  pre."BldgLoc"  = Permutations."BldgLoc" AND
  pre."BldgHVAC" = Permutations."BldgHVAC"
 LEFT JOIN simdata std on 
  std."TechID"   = Permutations."StdTechID" AND
  std."BldgType" = Permutations."BldgType" AND
  std."BldgVint" = Permutations."BldgVint" AND
  std."BldgLoc"  = Permutations."BldgLoc" AND
  std."BldgHVAC" = Permutations."BldgHVAC"
LEFT JOIN simdata meas on 
  meas."TechID"   = Permutations."MeasTechID" AND
  meas."BldgType" = Permutations."BldgType" AND
  meas."BldgVint" = Permutations."BldgVint" AND
  meas."BldgLoc"  = Permutations."BldgLoc" AND
  meas."BldgHVAC" = Permutations."BldgHVAC"
  
 ORDER BY 
  Permutations."OfferingID", Permutations."BldgType", Permutations."BldgHVAC", Permutations."BldgVint", Permutations."BldgLoc"




