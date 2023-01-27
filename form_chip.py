"""Script to FORM a chip"""
import argparse
from ember import EMBERDriver

# Get arguments
parser = argparse.ArgumentParser(description="FORM a chip.")
parser.add_argument("chipname", help="chip name for logging")
parser.add_argument("--config", type=str, default="config/form.json", help="config file")
parser.add_argument("--outfile", type=str, default="log/form.json", help="file to output to")
parser.add_argument("--start-addr", type=int, default=0, help="start address")
parser.add_argument("--end-addr", type=int, default=65536, help="end address")
parser.add_argument("--step-addr", type=int, default=1, help="address stride")
args = parser.parse_args()

# Initialize NI system and open outfile
with EMBERDriver(args.chipname, args.config) as ember:
  # Do operation across cells
  for addr in range(args.start_addr, args.end_addr, args.step_addr):
    ember.set_addr(addr)
    ember.write(0xFFFFFFFFFFFF)
    print("Address", addr, "DONE")