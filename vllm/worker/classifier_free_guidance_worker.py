
from vllm.worker.worker_base import LoraNotSupportedWorkerBase, WorkerBase



def create_cfg_worker(*arg, **kwargs):
    pass


class CFGWorker(LoraNotSupportedWorkerBase):
    @classmethod
    def create_worker():
        pass

    def __init__(self) -> None:
        super().__init__()












