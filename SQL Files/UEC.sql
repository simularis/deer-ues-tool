/*
This creates the table UEC, which calculates unit energy consumption for each case for the MeasureID. 
*/

DROP TABLE IF EXISTS UEC;
CREATE TABLE UEC AS

SELECT
UsePerUnitMeas.OfferingID,
UsePerUnitMeas.MAT,
UsePerUnitMeas.BldgLoc,
UsePerUnitMeas.BldgType,
UsePerUnitMeas.BldgVint,
UsePerUnitMeas.BldgHVAC,
UsePerUnitMeas.PreTechID,
UsePerUnitMeas.StdTechID,
UsePerUnitMeas.MeasTechID,
UsePerUnitMeas.area_sqft,
UsePerUnitMeas.std_kwh/UsePerUnitMeas.area_sqft as std_kwh_EC,
UsePerUnitMeas.std_therm/UsePerUnitMeas.area_sqft as std_therm_EC,
UsePerUnitMeas.std_kw/UsePerUnitMeas.area_sqft as std_kw_EC,
UsePerUnitMeas.meas_kwh/UsePerUnitMeas.area_sqft as meas_kwh_EC,
UsePerUnitMeas.meas_therm/UsePerUnitMeas.area_sqft as meas_therm_EC,
UsePerUnitMeas.meas_kw/UsePerUnitMeas.area_sqft as meas_kw_EC

FROM UsePerUnitMeas

