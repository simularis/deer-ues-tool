/*
This creates the table UsePerUnitMeas, which assigns energy use for MeasTechIDs. 
*/

DROP TABLE IF EXISTS UsePerUnitMeas;
CREATE TABLE UsePerUnitMeas AS

SELECT DISTINCT
UsePerUnitStd.OfferingID,
UsePerUnitStd.MAT,
UsePerUnitStd.BldgLoc,
UsePerUnitStd.BldgType,
UsePerUnitStd.BldgVint,
UsePerUnitStd.BldgHVAC,
UsePerUnitStd.PreTechID,
UsePerUnitStd.StdTechID,
UsePerUnitStd.MeasTechID,
UsePerUnitStd.area_sqft,
UsePerUnitStd.std_kwh,
UsePerUnitStd.std_therm,
UsePerUnitStd.std_kw,
simdata."Electricity/Cooling" as meas_kwh,
simdata."Natural Gas/Cooling" as meas_therm,
simdata."Electricity:Facility [J](Hourly)"*0.000000277778 as meas_kw

FROM UsePerUnitStd

JOIN simdata on simdata.BldgType = UsePerUnitStd.BldgType and simdata.BldgVint = UsePerUnitStd.BldgVint and simdata.BldgLoc = UsePerUnitStd.BldgLoc and simdata.TechID = UsePerUnitStd.MeasTechID;