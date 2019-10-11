import pandas as pd

# fill cell value in the right_file_name into left_file_name based on pk_right
def left_fill(left_file_name, right_file_name, column_map, pk_right):
    right_file = pd.read_excel(right_file_name, dtype={k: str for k in column_map.keys()})
    left_file = pd.read_excel(left_file_name, dtype={k: str for k in column_map.values()})
    
    res_column_key = column_map[pk_right]
    for index, row in left_file.iterrows():
        key = row[res_column_key]
        info = right_file.loc[right_file[pk_right] == key,:]
        assert(len(info) < 2)
        if not info.empty:
            r = info.iloc[0]
            for k,v in column_map.items():
                left_file.set_value(index, v, r[k])
    return left_file
