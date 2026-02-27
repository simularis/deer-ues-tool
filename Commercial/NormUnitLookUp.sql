-- applies norm units from lookup TABLE
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
 NormUnits.Value AS "NumUnits",
 simdata."Value Name",
 simdata.Value


FROM simdata

JOIN NormUnits ON
 (NormUnits.MeasureType IS NULL OR simdata.MeasureType = NormUnits.MeasureType) AND
 (NormUnits.BldgType IS NULL OR simdata.BldgType = NormUnits.BldgType) AND
 (NormUnits.BldgLoc IS NULL OR simdata.BldgLoc = NormUnits.BldgLoc) AND
 (NormUnits.BldgVint IS NULL OR simdata.BldgVint = NormUnits.BldgVint) AND
 simdata.NormUnit = NormUnits.NormUnit;





