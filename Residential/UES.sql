-- calculated unit energy savings

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
UEC.PrekW,
UEC.PrekWh,
UEC.Pretherm,
UEC.StdkW,
UEC.StdkWh,
UEC.Stdtherm,
UEC.MeaskW,
UEC.MeaskWh,
UEC.Meastherm,
UEC.PrekW - UEC.MeaskW as "UESkW_1",
UEC.PrekWh - UEC.MeaskWh as "UESkWh_1",
UEC.Pretherm - UEC.Meastherm as "UEStherm_1",
UEC.StdkW - UEC.MeaskW as "UESkW_2",
UEC.StdkWh - UEC.MeaskWh as "UESkWh_2",
UEC.Stdtherm - UEC.Meastherm as "UEStherm_2"

FROM UEC;