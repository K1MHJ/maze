import ctypes
import numpy as np

def DoMove(num_rows, num_cols, game_grid):
    PATH_TO_DLL = "./logic/bin/dllMain.so"
    dll = ctypes.CDLL(PATH_TO_DLL)
    func = dll.DllMain_Run
    func.restype = ctypes.c_int32
    func.argtypes = (ctypes.c_int32,
                     ctypes.c_int32,
                     ctypes.POINTER(ctypes.c_uint8), 
                     ctypes.POINTER(ctypes.c_int32), 
                     ctypes.POINTER(ctypes.c_int32))
    
    num_base_map = []
    for row in game_grid:
        for item in row:
            num_base_map.append(np.uint8(item))

    num_tmp_map  = (ctypes.c_uint8 * len(num_base_map))(*num_base_map)
    num_data_map = ctypes.cast(ctypes.pointer(num_tmp_map) , ctypes.POINTER(ctypes.c_uint8)) 
    
    num_tmp_x = (ctypes.c_int32)(0)
    num_tmp_y = (ctypes.c_int32)(0)

    result = func(num_cols, num_rows, num_data_map, 
                  ctypes.byref(num_tmp_x), 
                  ctypes.byref(num_tmp_y))
    print(result, num_tmp_x.value, num_tmp_y.value)
    return result,num_tmp_x.value, num_tmp_y.value
