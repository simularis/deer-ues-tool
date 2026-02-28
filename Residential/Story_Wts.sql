-- applies residential story weights
DROP TABLE IF EXISTS simdata_story;
CREATE TABLE simdata_story AS

-- SFm
SELECT
  normunits_simdata1.TechID,
  normunits_simdata1.BldgLoc,
  normunits_simdata1.BldgType,
  normunits_simdata1.BldgVint,
  normunits_simdata1.BldgHVAC,
  0 AS Story,
  normunits_simdata1.NormUnit,
  normunits_simdata1.NumUnits,
  normunits_simdata1."Value Name",
  ((normunits_simdata1."Value" * (2 - numstor)) + (normunits_simdata2."Value" * (numstor - 1))) / normunits_simdata1.NumUnits AS "Value"

FROM normunits_simdata normunits_simdata1

JOIN normunits_simdata normunits_simdata2 ON 
  normunits_simdata1.TechID       = normunits_simdata2.TechID   AND
  normunits_simdata1.BldgLoc      = normunits_simdata2.BldgLoc  AND
  normunits_simdata1.BldgType     = normunits_simdata2.BldgType AND
  normunits_simdata1.BldgVint     = normunits_simdata2.BldgVint AND
  normunits_simdata1.BldgHVAC     = normunits_simdata2.BldgHVAC AND
  normunits_simdata1."Value Name" = normunits_simdata2."Value Name"

JOIN numstor ON
  numstor.BldgType = normunits_simdata1.BldgType AND
  numstor.VintYear = normunits_simdata1.BldgVint AND
  numstor.BldgLoc  = normunits_simdata1.BldgLoc

WHERE normunits_simdata1.Story = 1 AND normunits_simdata2.Story = 2

UNION

-- DMo and MFm

SELECT
  normunits_simdata.TechID,
  normunits_simdata.BldgLoc,
  normunits_simdata.BldgType,
  normunits_simdata.BldgVint,
  normunits_simdata.BldgHVAC,
  normunits_simdata.Story,
  normunits_simdata.NormUnit,
  normunits_simdata.NumUnits,
  normunits_simdata."Value Name",
  normunits_simdata."Value" / normunits_simdata.NumUnits AS "Value"

FROM normunits_simdata

WHERE normunits_simdata.Story = 0;

