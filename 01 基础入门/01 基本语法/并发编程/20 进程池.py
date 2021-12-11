"""
apply
apply_async
map
map_async
starmap
starmap_async

join
close
terminate

imap
imap_unordered
"""
from multiprocessing import Pool

pool = Pool(processes=4)

print(dir(pool))
