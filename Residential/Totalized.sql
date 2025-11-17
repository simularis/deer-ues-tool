-- run after UEC/UES
-- run before bldg_wts, res_wts
DROP TABLE IF EXISTS totalized;
CREATE TABLE totalized AS

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
SUM(prekW.Value) as "PrekW",
SUM(prekWh.Value) as "PrekWh",
SUM(pretherm.Value) as "Pretherm"
-- SUM(StdkW.Value) as "StdkW",
-- SUM(StdkWh.Value) as "StdkWh",
-- SUM(Stdtherm.Value) as "Stdtherm",
-- SUM(MeaskW.Value) as "MeaskW",
-- SUM(MeaskWh.Value) as "MeaskWh",
-- SUM(Meastherm.Value) as "Meastherm"

FROM Permutations

-- outline
LEFT JOIN simdata_story prekW on 
  prekW."TechID" = Permutations."PreTechID" AND
  prekW."BldgType" = Permutations."BldgType" AND
  prekW."BldgVint" = Permutations."BldgVint" AND
  prekW."BldgLoc"  = Permutations."BldgLoc" AND
  prekW."BldgHVAC" = Permutations."BldgHVAC" AND
  prekW."Value Name" LIKE 'Electricity Demand'
LEFT JOIN simdata_story prekWh on 
  prekWh."TechID"   = Permutations."PreTechID" AND
  prekWh."BldgType" = Permutations."BldgType" AND
  prekWh."BldgVint" = Permutations."BldgVint" AND
  prekWh."BldgLoc"  = Permutations."BldgLoc" AND
  prekWh."BldgHVAC" = Permutations."BldgHVAC" AND
  prekWh."Value Name" LIKE 'Electricity/%'
LEFT JOIN simdata_story pretherm on 
  pretherm."TechID"   = Permutations."PreTechID" AND
  pretherm."BldgType" = Permutations."BldgType" AND
  pretherm."BldgVint" = Permutations."BldgVint" AND
  pretherm."BldgLoc"  = Permutations."BldgLoc" AND
  pretherm."BldgHVAC" = Permutations."BldgHVAC" AND
  pretherm."Value Name" LIKE 'Natural Gas/%'

GROUP BY
Permutations.OfferingID,
Permutations.MAT,
Permutations.BldgLoc,
Permutations.BldgType,
Permutations.BldgVint,
Permutations.BldgHVAC,
Permutations."Value Name"
 
ORDER BY 
  Permutations."OfferingID", Permutations."BldgType", Permutations."BldgHVAC", Permutations."BldgVint", Permutations."BldgLoc"
