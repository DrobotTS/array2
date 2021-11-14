def multiplication_avarage(list_data):
   everage_res = sum(list_data)/float(len(list_data)) if len(list_data) > 0 else list_data
   return [list_data[numb] * everage_res for numb in range(len(list_data))]