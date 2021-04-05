#imported pandas as pd
import pandas as pd
#created listof dictionary with given data
data_list=[{"id":"data1","last_updated":"18-03-2021","frequency":"96"},
           {"id":"data2","last_updated":"17-03-2021","frequency":"80"},
           {"id":"data3","last_updated":"24-03-2021","frequency":"63"},
           {"id":"data4","last_updated":"16-03-2021","frequency":"61"},
           {"id":"data5","last_updated":"22-01-2021","frequency":"59"},
           {"id":"data6","last_updated":"19-03-2021","frequency":"55"},
           {"id":"data7","last_updated":"20-03-2021","frequency":"78"},
           {"id":"data8","last_updated":"17-03-2021","frequency":"89"},
           {"id":"data9","last_updated":"22-03-2021","frequency":"62"},
           {"id":"data10","last_updated":"24-03-2021","frequency":"82"},
           {"id":"data11","last_updated":"21-03-2021","frequency":"69"},
           {"id":"data12","last_updated":"24-03-2021","frequency":"85"},
           ]
#converted listof dictionary in to DataFrame named data1
data_1 =pd.DataFrame.from_dict(data_list,orient="columns")
print(data_1)
#sorted the dataframe with frequency
sorted_data=data_1.sort_values('frequency')
print("SORTED DATA ")
print(sorted_data)