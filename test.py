import torch
import torch.distributed as dist
from torch.multiprocessing import Process
import os

os.environ['MASTER_ADDR'] = 'localhost'
os.environ['MASTER_PORT'] = '6000'
os.environ['IPV4']='1'


def init_process(rank, size, fn, backend='gloo'):
    """ Initialize the distributed environment. """
    dist.init_process_group(backend, rank=rank, world_size=size)
    fn(rank, size)

def example_distributed_function(rank, size):
    """ Example function for distributed processing. """
    # Create a random tensor on each process
    local_tensor = torch.rand(5) + rank

    # Sum the tensors across all processes
    dist.all_reduce(local_tensor, op=dist.ReduceOp.SUM)

    print(f"Rank {rank}: Sum of tensors across all processes: {local_tensor}")

def main():
    # Number of processes
    world_size = 2

    # Spawn processes
    processes = []
    for rank in range(world_size):
        p = Process(target=init_process, args=(rank, world_size, example_distributed_function))
        p.start()
        processes.append(p)

    # Wait for processes to finish
    for p in processes:
        p.join()

if __name__ == "__main__":
    main()

