-- calculates unit energy savings
DROP TABLE IF EXISTS UES;
CREATE TABLE UES AS

SELECT
  UEC.OfferingID,
  UEC.MAT,
  UEC.BldgLoc,
  UEC.BldgType,
  UEC.BldgVint,
  UEC.BldgHVAC,
  UEC.PreTechID,
  UEC.StdTechID,
  UEC.MeasTechID,
  UEC.NormUnit,
  UEC.NumUnits,
  UEC.PreUECkW,
  UEC.PreUECkWh,
  UEC.PreUECtherm,
  UEC.StdUECkW,
  UEC.StdUECkWh,
  UEC.StdUECtherm,
  UEC.MeasUECkW,
  UEC.MeasUECkWh,
  UEC.MeasUECtherm,
  UEC.PreUECkW    - UEC.MeasUECkW    AS "UESkW_1",
  UEC.PreUECkWh   - UEC.MeasUECkWh   AS "UESkWh_1",
  UEC.PreUECtherm - UEC.MeasUECtherm AS "UEStherm_1",
  UEC.StdUECkW    - UEC.MeasUECkW    AS "UESkW_2",
  UEC.StdUECkWh   - UEC.MeasUECkWh   AS "UESkWh_2",
  UEC.StdUECtherm - UEC.MeasUECtherm AS "UEStherm_2"

FROM UEC;