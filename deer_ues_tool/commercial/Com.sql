-- inserts Com building type rows
DELETE FROM UES WHERE "BldgType" = 'Com';
INSERT INTO UES

SELECT
  OfferingID,
  MAT,
  BldgLoc,
  'Com' AS "BldgType",
  BldgVint,
  BldgHVAC,
  PreTechID,
  StdTechID,
  MeasTechID,
  NormUnit,
  (SUM(NumUnits)     / SUM(wt_bldg)) AS "NumUnits",
  (SUM(PreUECkW)     / SUM(wt_bldg)) AS "PreUECkW",
  (SUM(PreUECkWh)    / SUM(wt_bldg)) AS "PreUECkWh",
  (SUM(PreUECtherm)  / SUM(wt_bldg)) AS "PreUECtherm",
  (SUM(StdUECkW)     / SUM(wt_bldg)) AS "StdUECkW",
  (SUM(StdUECkWh)    / SUM(wt_bldg)) AS "StdUECkWh",
  (SUM(StdUECtherm)  / SUM(wt_bldg)) AS "StdUECtherm",
  (SUM(MeasUECkW)    / SUM(wt_bldg)) AS "MeasUECkW",
  (SUM(MeasUECkWh)   / SUM(wt_bldg)) AS "MeasUECkWh",
  (SUM(MeasUECtherm) / SUM(wt_bldg)) AS "MeasUECtherm",
  (SUM(UESkW_1)      / SUM(wt_bldg)) AS "UESkW_1",
  (SUM(UESkWh_1)     / SUM(wt_bldg)) AS "UESkWh_1",
  (SUM(UEStherm_1)   / SUM(wt_bldg)) AS "UEStherm_1",
  (SUM(UESkW_2)      / SUM(wt_bldg)) AS "UESkW_2",
  (SUM(UESkWh_2)     / SUM(wt_bldg)) AS "UESkWh_2",
  (SUM(UEStherm_2)   / SUM(wt_bldg)) AS "UEStherm_2"

FROM UES_Wts

GROUP BY
  OfferingID,
  BldgVint,
  BldgLoc,
  BldgHVAC,
  NormUnit

ORDER BY 
  OfferingID,
  BldgVint,
  BldgHVAC;
