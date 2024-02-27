@drv.vectorize(length=chunk_size)
def validate_elements(element_data, flags):
  """
  Validates elements concurrently on the GPU.

  Args:
      element_data (list): List of tuples containing element objects and IDs.
      flags (drv.mem_int): Device memory to store validation flags (one per element).
  """
  i = drv.threadIdx.x
  element, _ = element_data[i]
  flags[i] = int(validate_element(element))
