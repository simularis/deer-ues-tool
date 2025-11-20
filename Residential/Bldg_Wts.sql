-- applies res building weights to savings
DROP TABLE If EXISTS UES_Wts;
CREATE TABLE UES_Wts AS

SELECT
UES.OfferingID,
UES.MAT,
UES.BldgLoc,
UES.BldgType,
UES.BldgVint,
UES.BldgHVAC,
UES.PreTechID,
UES.StdTechID,
UES.MeasTechID,
sum_bldg AS "wt_bldg",
UES.NormUnit,
UES.NumUnits * sum_bldg AS "NumUnits",
UES.PrekW * sum_bldg AS "PrekW",
UES.PrekWh * sum_bldg AS "PrekWh",
UES.Pretherm * sum_bldg AS "Pretherm",
UES.StdkW * sum_bldg AS "StdkW",
UES.StdkWh * sum_bldg AS "StdkWh",
UES.Stdtherm * sum_bldg AS "Stdtherm",
UES.MeaskW * sum_bldg AS "MeaskW",
UES.MeaskWh * sum_bldg AS "MeaskWh",
UES.Meastherm * sum_bldg AS "Meastherm",
UES.UESkW_1 * sum_bldg AS "UESkW_1",
UES.UESkWh_1 * sum_bldg AS "UESkWh_1",
UES.UEStherm_1 * sum_bldg AS "UEStherm_1",
UES.UESkW_2 * sum_bldg AS "UESkW_2",
UES.UESkWh_2 * sum_bldg AS "UESkWh_2",
UES.UEStherm_2 * sum_bldg AS "UEStherm_2"

FROM UES

INNER JOIN wts_res_bldg ON 
 wts_res_bldg."bldgtype" = UES."BldgType" AND 
 wts_res_bldg."era"      = UES."BldgVint" AND
 wts_res_bldg."bldgloc"  = UES."BldgLoc"

ORDER BY 
UES."OfferingID",
UES."BldgVint",
UES."BldgLoc",
UES."BldgHVAC";