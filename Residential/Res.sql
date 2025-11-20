-- inserts Res building type rows
DELETE FROM UES WHERE "BldgType" = 'Res';
INSERT INTO UES

SELECT
OfferingID,
MAT,
BldgLoc,
'Res' AS "BldgType",
BldgVint,
BldgHVAC,
PreTechID,
StdTechID,
MeasTechID,
NormUnit,
(SUM(NumUnits) / SUM(wt_bldg)) AS NumUnits,
(SUM(PrekW) / SUM(wt_bldg)) AS "PrekW",
(SUM(PrekWh) / SUM(wt_bldg)) AS "PrekWh",
(SUM(Pretherm) / SUM(wt_bldg)) AS "Pretherm",
(SUM(StdkW) / SUM(wt_bldg)) AS "StdkW",
(SUM(StdkWh) / SUM(wt_bldg)) AS "StdkWh",
(SUM(Stdtherm) / SUM(wt_bldg)) AS "Stdtherm",
(SUM(MeaskW) / SUM(wt_bldg)) AS "MeaskW",
(SUM(MeaskWh) / SUM(wt_bldg)) AS "MeaskWh",
(SUM(Meastherm) / SUM(wt_bldg)) AS "Meastherm",
(SUM(UESkW_1) / SUM(wt_bldg)) AS "UESkW_1",
(SUM(UESkWh_1) / SUM(wt_bldg)) AS "UESkWh_1",
(SUM(UEStherm_1) / SUM(wt_bldg)) AS "UEStherm_1",
(SUM(UESkW_2) / SUM(wt_bldg)) AS "UESkW_2",
(SUM(UESkWh_2) / SUM(wt_bldg)) AS "UESkWh_2",
(SUM(UEStherm_2) / SUM(wt_bldg)) AS "UEStherm_2"

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
