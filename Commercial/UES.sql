/*
This creates the table UES, which calculates unit energy savings for each case for the MeasureID. 
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
UEC.area_sqft,
UEC.std_kwh_EC,
UEC.std_therm_EC,
UEC.std_kw_EC,
UEC.meas_kwh_EC,
UEC.meas_therm_EC,
UEC.meas_kw_EC,
UEC.std_kwh_EC - UEC.meas_kwh_EC as kwh_UES,
UEC.std_therm_EC - UEC.meas_therm_EC as therm_UES,
UEC.std_kw_EC - UEC.meas_kw_EC as kw_peak

FROM UEC
