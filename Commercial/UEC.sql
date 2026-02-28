-- calculates unit energy consumption
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
  measkW.NormUnit AS "NormUnit",
  measkW.NumUnits AS "NumUnits",
  prekW.Value     / measkW.NumUnits AS "PreUECkW",
  prekWh.Value    / measkW.NumUnits AS "PreUECkWh",
  pretherm.Value  / measkW.NumUnits AS "PreUECtherm",
  stdkW.Value     / measkW.NumUnits AS "StdUECkW",
  stdkWh.Value    / measkW.NumUnits AS "StdUECkWh",
  stdtherm.Value  / measkW.NumUnits AS "StdUECtherm",
  measkW.Value    / measkW.NumUnits AS "MeasUECkW",
  measkWh.Value   / measkW.NumUnits AS "MeasUECkWh",
  meastherm.Value / measkW.NumUnits AS "MeasUECtherm"

FROM Permutations

LEFT JOIN normunits_simdata prekW on 
  prekW."TechID"   = Permutations."PreTechID" AND
  prekW."BldgType" = Permutations."BldgType"  AND
  prekW."BldgVint" = Permutations."BldgVint"  AND
  prekW."BldgLoc"  = Permutations."BldgLoc"   AND
  prekW."BldgHVAC" = Permutations."BldgHVAC"  AND
  prekW."Value Name" LIKE 'Demand kW'
--  prekW."Value Name" LIKE 'Electricity Demand'
LEFT JOIN normunits_simdata prekWh on 
  prekWh."TechID"   = Permutations."PreTechID" AND
  prekWh."BldgType" = Permutations."BldgType"  AND
  prekWh."BldgVint" = Permutations."BldgVint"  AND
  prekWh."BldgLoc"  = Permutations."BldgLoc"   AND
  prekWh."BldgHVAC" = Permutations."BldgHVAC"  AND
  prekWh."Value Name" LIKE 'HVAC kWh'
--  prekWh."Value Name" LIKE 'Electricity/%'
LEFT JOIN normunits_simdata pretherm on 
  pretherm."TechID"   = Permutations."PreTechID" AND
  pretherm."BldgType" = Permutations."BldgType"  AND
  pretherm."BldgVint" = Permutations."BldgVint"  AND
  pretherm."BldgLoc"  = Permutations."BldgLoc"   AND
  pretherm."BldgHVAC" = Permutations."BldgHVAC"  AND
  pretherm."Value Name" LIKE 'HVAC therm'
--  pretherm."Value Name" LIKE 'Natural Gas/%'
LEFT JOIN normunits_simdata stdkW on 
  stdkW."TechID"   = Permutations."StdTechID" AND
  stdkW."BldgType" = Permutations."BldgType"  AND
  stdkW."BldgVint" = Permutations."BldgVint"  AND
  stdkW."BldgLoc"  = Permutations."BldgLoc"   AND
  stdkW."BldgHVAC" = Permutations."BldgHVAC"  AND
  stdkW."Value Name" LIKE 'Demand kW'
--  stdkW."Value Name" LIKE 'Electricity Demand'
LEFT JOIN normunits_simdata stdkWh on 
  stdkWh."TechID"   = Permutations."StdTechID" AND
  stdkWh."BldgType" = Permutations."BldgType"  AND
  stdkWh."BldgVint" = Permutations."BldgVint"  AND
  stdkWh."BldgLoc"  = Permutations."BldgLoc"   AND
  stdkWh."BldgHVAC" = Permutations."BldgHVAC"  AND
  stdkWh."Value Name" LIKE 'HVAC kWh'
--  stdkWh."Value Name" LIKE 'Electricity/%'
LEFT JOIN normunits_simdata stdtherm on 
  stdtherm."TechID"   = Permutations."StdTechID" AND
  stdtherm."BldgType" = Permutations."BldgType"  AND
  stdtherm."BldgVint" = Permutations."BldgVint"  AND
  stdtherm."BldgLoc"  = Permutations."BldgLoc"   AND
  stdtherm."BldgHVAC" = Permutations."BldgHVAC"  AND
  stdtherm."Value Name" LIKE 'HVAC therm'
--  stdtherm."Value Name" LIKE 'Natural Gas/%'
 LEFT JOIN normunits_simdata measkW on 
  measkW."TechID"   = Permutations."MeasTechID" AND
  measkW."BldgType" = Permutations."BldgType"   AND
  measkW."BldgVint" = Permutations."BldgVint"   AND
  measkW."BldgLoc"  = Permutations."BldgLoc"    AND
  measkW."BldgHVAC" = Permutations."BldgHVAC"   AND
  measkW."Value Name" LIKE 'Demand kW'
--  measkW."Value Name" LIKE 'Electricity Demand'
LEFT JOIN normunits_simdata measkWh on 
  measkWh."TechID"   = Permutations."MeasTechID" AND
  measkWh."BldgType" = Permutations."BldgType"   AND
  measkWh."BldgVint" = Permutations."BldgVint"   AND
  measkWh."BldgLoc"  = Permutations."BldgLoc"    AND
  measkWh."BldgHVAC" = Permutations."BldgHVAC"   AND
  measkWh."Value Name" LIKE 'HVAC kWh'
--  measkWh."Value Name" LIKE 'Electricity/%'
LEFT JOIN normunits_simdata meastherm on 
  meastherm."TechID"   = Permutations."MeasTechID" AND
  meastherm."BldgType" = Permutations."BldgType"   AND
  meastherm."BldgVint" = Permutations."BldgVint"   AND
  meastherm."BldgLoc"  = Permutations."BldgLoc"    AND
  meastherm."BldgHVAC" = Permutations."BldgHVAC"   AND
  meastherm."Value Name" LIKE 'HVAC therm'
--  meastherm."Value Name" LIKE 'Natural Gas/%'

GROUP BY
  Permutations.OfferingID,
  Permutations.MAT,
  Permutations.BldgLoc,
  Permutations.BldgType,
  Permutations.BldgVint,
  Permutations.BldgHVAC
 
ORDER BY 
  Permutations.OfferingID,
  Permutations.BldgLoc,
  Permutations.BldgType,
  Permutations.BldgHVAC,
  Permutations.BldgVint;