from aux.cypher.aes.operations import add_sub_key, break_in_grids_of_16, expand_key, extract_key_for_round, mix_columns, rotate_row_left, sbox_reverse_lookup 

class AES():

    def __init__(self, key, mode="ECB"):
        self.key = key
        self.mode = mode

    def decrypt(self, data, iv=b''):

        input_grids = break_in_grids_of_16(data)
    
        iv_grid = break_in_grids_of_16(iv)
        expanded_key = expand_key(self.key, 11)
        grids = []
    
        for i in range(len(input_grids)):
    
    
            grid = input_grids[i]
    
            round_key = extract_key_for_round(expanded_key, 10)
            add_sub_key_step = add_sub_key(grid, round_key)
            shift_rows_step = [rotate_row_left(
                add_sub_key_step[i], -1 * i) for i in range(4)]
            sub_bytes_step = [[sbox_reverse_lookup(val) for val in row]
                              for row in shift_rows_step]
            grid = sub_bytes_step
    
            for round in range(9, 0, -1):
    
                round_key = extract_key_for_round(expanded_key, round)
                add_sub_key_step = add_sub_key(grid, round_key)
    
                # Doing the mix columns three times is equal to using the reverse matrix
                mix_column_step = mix_columns(add_sub_key_step)
                mix_column_step = mix_columns(mix_column_step)
                mix_column_step = mix_columns(mix_column_step)
                shift_rows_step = [rotate_row_left(
                    mix_column_step[i], -1 * i) for i in range(4)]
                sub_bytes_step = [
                    [sbox_reverse_lookup(val) for val in row] for row in shift_rows_step]
    
                grid = sub_bytes_step
    
    
            # Reversing the first add sub key
            round_key = extract_key_for_round(expanded_key, 0)
            grid = add_sub_key(grid, round_key)
    
            if self.mode == "CBC":
                if i == 0:
                    grid = add_sub_key(grid, self.iv_grid[0])
                else:
                    grid = add_sub_key(grid, input_grids[i-1])
            
            grids.append(grid)
           
    
        # Just transform the grids back to bytes
        int_stream = []
    
        for grid in grids:
            for column in range(4):
                for row in range(4):
                    int_stream.append(grid[row][column])
    
        return bytes(int_stream)
