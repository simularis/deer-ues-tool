/*
This creates the table Story_Wts, residential building considerations for stories.
Run prior to Permutations to join simdata 1 and 2 story rows together.
*/
DROP TABLE IF EXISTS simdata_story;
CREATE TABLE simdata_story AS

-- for SFm
SELECT
simdata1.TechID,
simdata1.BldgLoc,
simdata1.BldgType,
simdata1.BldgVint,
simdata1.BldgHVAC,
0 AS Story,
simdata1.NormUnit,
simdata1.NumUnits,
simdata1."Value Name",
(simdata1."Value" * (2 - numstor) + simdata2."Value" * (numstor - 1))/simdata1.NumUnits AS "Value"

FROM simdata simdata1

JOIN simdata simdata2 ON 
simdata1.TechID = simdata2.TechID AND
simdata1.BldgLoc = simdata2.BldgLoc AND
simdata1.BldgType = simdata2.BldgType AND
simdata1.BldgVint = simdata2.BldgVint AND
simdata1.BldgHVAC = simdata2.BldgHVAC

JOIN numstor ON
numstor.BldgType = simdata1.BldgType AND
numstor.VintYear = simdata1.BldgVint AND
numstor.BldgLoc = simdata1.BldgLoc

WHERE simdata1.Story = 1 and simdata2.Story = 2

UNION

-- for DMo and MFm

SELECT
simdata.TechID,
simdata.BldgLoc,
simdata.BldgType,
simdata.BldgVint,
simdata.BldgHVAC,
simdata.Story,
simdata.NormUnit,
simdata.NumUnits,
simdata."Value Name",
simdata."Value"/simdata.NumUnits AS "Value"

FROM simdata

WHERE simdata.Story = 0;

