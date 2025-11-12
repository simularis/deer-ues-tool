/*
This creates the table UsePerUnit, which assigns energy use per building dwelling unit (total area [ft2] divided by number of buildings). 
*/

DROP TABLE IF EXISTS UsePerUnitStd;
CREATE TABLE UsePerUnitStd AS

SELECT DISTINCT
Permutations.OfferingID,
Permutations.MAT,
Permutations.BldgLoc,
Permutations.BldgType,
Permutations.BldgVint,
simdata.BldgHVAC,
Permutations.PreTechID,
Permutations.StdTechID,
Permutations.MeasTechID,
("Area/CLASSROOM G.E1"+"Area/CLASSROOM G.NNE2"+"Area/CLASSROOM G.SSE3"+"Area/CLASSROOM G.W4"+"Area/CLASSROOM E1 WEST PERIM (G.W1)"+"Area/CLASSROOM E2 NORTH PERIM (G.N3)"+"Area/CLASSROOM E2 SOUTH PERIM (G.S2)"+"Area/CLASSROOM E2 WEST PERIM (G.W1)"+"Area/CLASSROOM E4 CORE (G.C6)"+"Area/CLASSROOM E4 EAST PERIM (G.E2)"+"Area/CLASSROOM E4 NORTH PERIM (G.N3)"+"Area/CLASSROOM E4 SOUTH PERIM (G.S1)"+"Area/CLASSROOM E4 WEST PERIM (G.W4)"+"Area/COMPUTER CLASSROOM E4 CORE SPC (G.C5)"+"Area/CLASSROOM EL1 SPC (G.1)")*10.764 as area_sqft,
simdata."Electricity/Cooling" as std_kwh,
simdata."Natural Gas/Cooling" as std_therm,
simdata."Electricity:Facility [J](Hourly)"*0.000000277778 as std_kw

FROM Permutations

JOIN simdata on simdata.BldgType = Permutations.BldgType and simdata.BldgVint = Permutations.BldgVint and simdata.BldgLoc = Permutations.BldgLoc and simdata.TechID = Permutations.StdTechID;




