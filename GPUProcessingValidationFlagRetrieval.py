# Allocate memory on host and device for element data, flags, and temporary storage
num_elements = len(elements)
element_data_host = [(drv.In(e[0]), e[1]) for e in elements]  # Pack element and ID for kernel
flags_host = drv.mem_alloc(num_elements * drv.dtype('bool'))
temp_storage = drv.mem_alloc(num_elements * drv.dtype('int'))

# Launch the kernel for each chunk of elements
for chunk in element_chunks:
  chunk_data, chunk_ids = zip(*chunk)
  threadsPerBlock = chunk_size
  blocksPerGrid = (len(chunk_data) + threadsPerBlock - 1) // threadsPerBlock
  validate_elements.launch_grid_async(blocksPerGrid, 1, blocksPerGrid * threadsPerBlock, chunk_data, temp_storage)
  drv.memcpy_DtoH(flags_host, temp_storage)  # Copy flags back to host after each chunk

# Free temporary storage on GPU
drv.mem_free(temp_storage)
