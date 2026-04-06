-- apply norm units from model data
DROP TABLE IF EXISTS normunits_simdata;
CREATE TABLE normunits_simdata AS

SELECT
  simdata.MeasureName,
  simdata.MeasureType,
  simdata.BldgLoc,
  simdata.BldgType,
  simdata.Story,
  simdata.BldgHVAC,
  simdata.BldgVint,
  simdata.TechGroup,
  simdata.TechType,
  simdata.TechID,
  simdata.NormUnit,
  CASE 
    WHEN simdata.NormUnit = 'Cap-Tons' THEN normunit.Value * 0.0002843451
	WHEN simdata.NormUnit = 'Area/Conditioned Total' THEN normunit.Value * 10.7639
	END AS "NumUnits",
  simdata."Value Name",
  simdata.Value

FROM simdata

LEFT JOIN simdata normunit on 
  normunit."TechID"     = simdata."TechID"     AND
  normunit."BldgType"   = simdata."BldgType"   AND
  normunit."BldgVint"   = simdata."BldgVint"   AND
  normunit."BldgLoc"    = simdata."BldgLoc"    AND
  normunit."BldgHVAC"   = simdata."BldgHVAC"   AND
  normunit."Value Name" = simdata."Measuretype"



