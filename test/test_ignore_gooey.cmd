pip install -e .[ui]
python -m deer_ues_tool.UIgooey --ignore-gooey --MeasureName SWHC012 --MeasureType "Cooling Capacity" --Sector Commercial --NormalizingUnit "Cap-Tons" --SimdataFile .\simdata_SWHC012.csv --MeasDefFile .\MeasDef_SWHC012.csv --ComResOption
