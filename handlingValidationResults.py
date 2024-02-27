# Combine flags from all chunks
flags = drv.to_host(flags_host)

# Iterate through elements and check validation flags
for i, element_id in enumerate(elements):
  if not flags[i]:
    print(f"Element {element_id} failed validation")

# Free memory on GPU
drv.mem_free(flags_host)
