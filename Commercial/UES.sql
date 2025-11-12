/*
This creates the table UES, unit energy savings. 
*/
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
UEC.PreUECkW - UEC.MeasUECkW as "UESkW_1",
UEC.PreUECkWh - UEC.MeasUECkWh as "UESkWh_1",
UEC.PreUECtherm - UEC.MeasUECtherm as "UEStherm_1",
UEC.StdUECkW - UEC.MeasUECkW as "UESkW_2",
UEC.StdUECkWh - UEC.MeasUECkWh as "UESkWh_2",
UEC.StdUECtherm - UEC.MeasUECtherm as "UEStherm_2"

FROM UEC
